#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prueft die erzeugte Seite. Ohne Argumente laeuft alles ausser dem Netzzugriff.

    python3 check.py            # Struktur, Inhalt, Konsistenz
    python3 check.py --links    # zusaetzlich jede Quell-URL auf HTTP 200

Der Exit-Code ist 0, wenn alles besteht, sonst 1. Die Seite behauptet von sich,
belegt und widerspruchsfrei zu sein. Dieses Skript macht die Behauptung pruefbar.
"""

import html.parser
import json
import os
import re
import sys

import build
import content as C

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

fails = []
passes = []


def ok(msg):
    passes.append(msg)


def bad(msg):
    fails.append(msg)


def check(cond, msg, detail=""):
    if cond:
        ok(msg)
    else:
        bad(msg + (": " + str(detail) if detail else ""))


class TagBalance(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("schliessendes </%s> ohne Gegenstueck bei %s" % (tag, self.getpos()))
            return
        top, pos = self.stack.pop()
        if top != tag:
            self.errors.append("<%s> bei %s wird von </%s> bei %s geschlossen" % (top, pos, tag, self.getpos()))


def visible_text(src):
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", src, flags=re.S)
    return re.sub(r"<[^>]+>", " ", body)


def tech_tokens(src):
    """Sprachneutrale Angaben, die in beiden Fassungen identisch sein muessen."""
    return {
        "IPv4": set(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", src)),
        "IPv6": set(re.findall(r"\b(?:[0-9a-f]{0,4}:){2,7}[0-9a-f]{0,4}\b", src)),
        "DoH": set(re.findall(r"https://[a-z0-9.\-]+/(?:dns-query|query)", src)),
        "RFC": set(re.findall(r"RFC \d{3,4}", src)),
    }


def main():
    do_links = "--links" in sys.argv
    pages = {}

    for page in build.PAGES:
        for lang in ("de", "en"):
            path = build.page_path(page, lang)
            check(os.path.exists(path), "Datei vorhanden: %s" % path)
            if not os.path.exists(path):
                continue
            pages[(page, lang)] = open(path, encoding="utf-8").read()

    # ---- 1. Struktur jeder einzelnen Seite -------------------------------
    for (page, lang), src in pages.items():
        tag = "%s/%s" % (page, lang)

        p = TagBalance()
        p.feed(src)
        check(not p.stack and not p.errors, "%s: HTML wohlgeformt" % tag,
              (["nicht geschlossen: " + t for t, _ in p.stack] + p.errors)[:3])

        heads = [int(m) for m in re.findall(r"<h([1-6])", src)]
        check(heads.count(1) == 1, "%s: genau eine h1" % tag, heads.count(1))
        jumps = [(a, b) for a, b in zip(heads, heads[1:]) if b > a + 1]
        check(not jumps, "%s: Ueberschriften ohne Sprung" % tag, jumps[:3])

        check(('<html lang="%s"' % lang) in src, "%s: lang-Attribut gesetzt" % tag)

        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
        check(m is not None, "%s: JSON-LD vorhanden" % tag)
        if m:
            try:
                graph = json.loads(m.group(1))["@graph"]
                types = [g["@type"] for g in graph]
                check("WebPage" in types and "BreadcrumbList" in types,
                      "%s: JSON-LD gueltig (%s)" % (tag, ", ".join(types)))
                ids = [g["@id"] for g in graph if "@id" in g]
                check(len(ids) == len(set(ids)), "%s: JSON-LD ohne doppelte @id" % tag, ids)
            except Exception as ex:
                bad("%s: JSON-LD kaputt: %s" % (tag, ex))

        url = build.page_url(page, lang)
        canon = re.findall(r'rel="canonical" href="([^"]+)"', src)
        check(canon == [url], "%s: canonical zeigt auf sich selbst" % tag, canon)

        hl = dict((a, b) for a, b in re.findall(r'hreflang="([^"]+)" href="([^"]+)"', src))
        check(hl.get("de") == build.page_url(page, "de")
              and hl.get("en") == build.page_url(page, "en")
              and hl.get("x-default") == build.page_url(page, "de"),
              "%s: hreflang vollstaendig und absolut" % tag, hl)
        check(url in hl.values(), "%s: hreflang nennt die Seite selbst" % tag)

        text = visible_text(src)
        dashes = text.count("—") + text.count("–")
        check(dashes == 0, "%s: keine Gedankenstriche" % tag, dashes)

        # Escaped ausgegebene Auszeichnung ist gueltiges HTML und faellt keinem
        # Parser auf. Dem Leser faellt sie sofort auf.
        stray = re.findall(r"&lt;/?(?:code|strong|em|a|p|br|span)\b[^&]{0,40}&gt;", src)
        check(not stray, "%s: keine escaped ausgegebene Auszeichnung" % tag, stray[:3])

        assets = re.findall(r'<(?:script|img)[^>]*src="(https?://[^"]+)"', src)
        assets += [u for u in re.findall(r'<link[^>]*href="(https?://[^"]+)"', src)
                   if "dns.kaipfstr.de" not in u]
        check(not assets, "%s: laedt nichts von fremden Servern" % tag, assets[:3])

        check("<script" not in src.replace('<script type="application/ld+json">', ""),
              "%s: kein ausfuehrbares Skript" % tag)

        desc = re.findall(r'name="description" content="([^"]*)"', src)
        check(len(desc) == 1 and 80 <= len(desc[0]) <= 165,
              "%s: description in Snippet-Laenge" % tag, len(desc[0]) if desc else 0)

        title = re.findall(r"<title>([^<]*)</title>", src)
        check(len(title) == 1 and 20 <= len(title[0]) <= 75,
              "%s: title vorhanden und nicht zu lang" % tag, title)

    # ---- 2. Gleichstand beider Sprachfassungen ---------------------------
    for page in build.PAGES:
        de = pages.get((page, "de"))
        en = pages.get((page, "en"))
        if not (de and en):
            continue
        for name, a in tech_tokens(de).items():
            b = tech_tokens(en)[name]
            check(a == b, "%s: %s in beiden Fassungen gleich (%d)" % (page, name, len(a)),
                  "nur DE %s / nur EN %s" % (sorted(a - b)[:4], sorted(b - a)[:4]))

    # ---- 3. Eindeutige Titel und Beschreibungen --------------------------
    for lang in ("de", "en"):
        titles = [re.findall(r"<title>([^<]*)</title>", pages[(p, lang)])[0] for p in build.PAGES]
        descs = [re.findall(r'name="description" content="([^"]*)"', pages[(p, lang)])[0] for p in build.PAGES]
        check(len(set(titles)) == len(titles), "%s: alle title eindeutig" % lang, titles)
        check(len(set(descs)) == len(descs), "%s: alle description eindeutig" % lang)

    # ---- 4. Stylesheet ---------------------------------------------------
    css = build.CSS
    check(css.count("{") == css.count("}"), "CSS: Klammern ausgeglichen")
    used = set()
    for src in pages.values():
        used |= {c for g in re.findall(r'class="([^"]+)"', src) for c in g.split()}
    defined = set(re.findall(r"\.([a-zA-Z][\w-]*)", css))
    check(not (used - defined), "CSS: jede benutzte Klasse ist gestaltet", sorted(used - defined))
    check(not (defined - used), "CSS: keine toten Klassen", sorted(defined - used))
    uv = set(re.findall(r"var\((--[\w-]+)\)", css))
    dv = set(re.findall(r"(--[\w-]+)\s*:", css))
    check(not (uv - dv), "CSS: keine undefinierten Variablen", sorted(uv - dv))
    check(not (dv - uv), "CSS: keine ungenutzten Variablen", sorted(dv - uv))

    # ---- 5. Sitemap und robots.txt ---------------------------------------
    sm = open("sitemap.xml", encoding="utf-8").read()
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    want = [build.page_url(p, l) for p in build.PAGES for l in ("de", "en")]
    check(sorted(locs) == sorted(want), "sitemap.xml nennt genau die erzeugten Seiten",
          "fehlt %s / zuviel %s" % (sorted(set(want) - set(locs)), sorted(set(locs) - set(want))))
    check(sm.count('xmlns:xhtml="http://www.w3.org/1999/xhtml"') == 1, "sitemap.xml: xhtml-Namensraum gesetzt")
    check(sm.count("<xhtml:link") == 3 * len(locs), "sitemap.xml: jede URL nennt alle Sprachvarianten")
    rb = open("robots.txt", encoding="utf-8").read()
    check("Sitemap: %s/sitemap.xml" % build.BASE in rb, "robots.txt verweist auf die Sitemap")

    # ---- 6. IndexNow -----------------------------------------------------
    keys = [f for f in os.listdir(".") if re.fullmatch(r"[0-9a-f]{8,128}\.txt", f)]
    check(len(keys) == 1, "IndexNow: genau eine Schluesseldatei", keys)
    if len(keys) == 1:
        check(open(keys[0], encoding="utf-8").read().strip() == keys[0][:-4],
              "IndexNow: Dateiname und Inhalt stimmen ueberein")

    # ---- 7. Belege -------------------------------------------------------
    all_src = "".join(pages.values())
    body = re.sub(r'<ul class="src">.*?</ul>', "", all_src, flags=re.S)
    # "RFC 4033, 4034, 4035" nennt drei Normen, nicht eine. Die Fortsetzungszahlen
    # gehoeren genauso ins Quellenverzeichnis wie die erste.
    cited = set()
    for run in re.findall(r"RFC\s+\d{3,4}(?:\s*,\s*\d{3,4})*", visible_text(body)):
        cited |= {int(n) for n in re.findall(r"\d{3,4}", run)}
    listed = set(int(x) for x in re.findall(r"rfc(\d{3,4})\.txt", all_src))
    check(cited <= listed, "jeder im Text zitierte RFC steht im Quellenverzeichnis",
          sorted(cited - listed))
    check(listed <= cited, "kein RFC im Verzeichnis, der nirgends zitiert wird",
          sorted(listed - cited))

    for p in C.PROVIDERS:
        pid = p["id"]
        check(bool(p["sources"]), "Anbieter %s hat Belege" % pid)
        for field in ("operator", "carrier", "dnssec", "doq", "filtering", "logging", "strengths", "caveats"):
            check(field + "_en" in p, "Anbieter %s: %s hat englische Fassung" % (pid, field))
        check(p["unfiltered"] in ("yes", "limited", "no"), "Anbieter %s: Filterstatus gesetzt" % pid)

    # ---- 8. Uebersichtstabelle gegen die Karten --------------------------
    de_index = pages[("index", "de")]
    for p in C.PROVIDERS:
        row = re.search(r'<th scope="row"><a href="#p-%s">.*?</tr>' % re.escape(p["id"]), de_index, re.S)
        check(row is not None, "Tabelle enthaelt Zeile fuer %s" % p["id"])
        if row:
            want_plain = build.T["de"]["yes"] if p["plain53"] else build.T["de"]["no"]
            check(want_plain in row.group(0),
                  "Tabelle: Klartext-DNS fuer %s stimmt mit der Karte" % p["id"])

    # ---- 9. Optional: jede Quelle erreichbar -----------------------------
    if do_links:
        import concurrent.futures
        import ssl
        import urllib.request
        urls = sorted({u for u in re.findall(r'<a href="(https?://[^"]+)"', all_src)
                       if "dns.kaipfstr.de" not in u})

        def fetch(u):
            try:
                r = urllib.request.urlopen(
                    urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 dns.kaipfstr.de link-check",
                                                       "Accept": "*/*"}),
                    timeout=30, context=ssl.create_default_context())
                return u, r.status
            except Exception as ex:
                return u, getattr(ex, "code", None) or type(ex).__name__

        broken = []
        with concurrent.futures.ThreadPoolExecutor(12) as ex:
            for u, st in ex.map(fetch, urls):
                if st != 200:
                    broken.append("%s %s" % (st, u))
        check(not broken, "alle %d Quell-URLs liefern HTTP 200" % len(urls), broken[:5])

    # ---- Bericht ---------------------------------------------------------
    print("%d Pruefungen bestanden" % len(passes))
    if fails:
        print("\n%d FEHLGESCHLAGEN:" % len(fails))
        for f in fails:
            print("  x " + f)
        return 1
    print("Alles in Ordnung.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
