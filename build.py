#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baut dns.kaipfstr.de aus content.py.

    python3 build.py

Erzeugt index.html (Deutsch), en/index.html (Englisch) und sitemap.xml.
Beide Sprachfassungen werden aus derselben Datenquelle gerendert, damit die
technischen Angaben nicht auseinanderlaufen koennen.
"""

import html
import os
import re

import content as C

BASE = C.DOMAIN
OUT_DE = "index.html"
OUT_EN = os.path.join("en", "index.html")
URL_DE = BASE + "/"
URL_EN = BASE + "/en/"

T = {
    "de": {
        "lang": "de", "locale": "de_DE", "other_locale": "en_GB",
        "title": "Sichere DNS-Server: geprüfte Anbieter und Selbsthosting",
        "brand": "Sichere DNS-Server",
        "desc": ("Elf öffentliche DNS-Resolver und sechs Wege zum Selbsthosten, am 6. September 2026 "
                 "an der Primärquelle geprüft: Adressen, Trägerschaft, Einschränkungen."),
        "tagline": "Welchen Namensauflöser Sie benutzen, entscheidet, wer mitliest.",
        "switch": "English version", "switch_url": URL_EN,
        "nav": "Inhalt",
        "toc": [("was", "Was DNS verrät"), ("grenzen", "Was verschlüsseltes DNS nicht leistet"),
                ("protokolle", "Die Protokolle"), ("auswahl", "Woran man einen guten Anbieter erkennt"),
                ("anbieter", "Die Anbieter im Einzelnen"), ("warnung", "Nicht mehr verwenden"),
                ("kommerziell", "Die großen kommerziellen Dienste"), ("selbst", "Selbst betreiben"),
                ("einrichten", "Einrichten"), ("recht", "Rechtlicher Rahmen in Deutschland"),
                ("faq", "Häufige Fragen"), ("methode", "Wie diese Seite geprüft wurde"),
                ("quellen", "Quellen")],
        "h_was": "Was DNS über Sie verrät",
        "h_grenzen": "Was verschlüsseltes DNS nicht leistet",
        "h_protokolle": "Die Protokolle, kurz und richtig",
        "h_auswahl": "Woran man einen guten Anbieter erkennt",
        "h_anbieter": "Die Anbieter im Einzelnen",
        "h_warnung": "Nicht mehr verwenden",
        "h_kommerziell": "Die großen kommerziellen Dienste",
        "h_selbst": "Selbst betreiben",
        "h_einrichten": "Einrichten",
        "h_recht": "Rechtlicher Rahmen in Deutschland",
        "h_faq": "Häufige Fragen",
        "h_methode": "Wie diese Seite geprüft wurde",
        "h_quellen": "Quellen",
        "l_operator": "Betreiber", "l_carrier": "Trägerschaft", "l_endpoints": "Endpunkte",
        "l_doq": "DNS over QUIC", "l_dnssec": "DNSSEC", "l_filter": "Filterung",
        "l_logging": "Protokollierung", "l_strengths": "Wofür er spricht",
        "l_caveats": "Was dagegen spricht", "l_sources": "Belege",
        "l_ipv4": "IPv4", "l_ipv6": "IPv6", "l_doh": "DoH", "l_dot": "DoT",
        "l_license": "Lizenz", "l_kind": "Was es ist", "l_by": "Herausgeber",
        "l_state": "Status", "l_addresses": "Adressen",
        "overview": "Überblick",
        "table_caption": "Die elf geprüften Resolver im Überblick",
        "th_name": "Dienst", "th_carrier": "Trägerschaft", "th_country": "Sitz",
        "th_filter": "Ungefilterte Adresse", "th_plain": "Klartext-DNS",
        "yes": "ja", "no": "nein", "limited": "mit Vorbehalt",
        "table_note": ("„Mit Vorbehalt“ heißt: Es gibt eine Adresse ohne Inhaltsfilter, aber der Betreiber setzt "
                       "gerichtlich oder gesetzlich angeordnete Sperren auch dort um. Die Einzelheiten stehen in "
                       "der jeweiligen Karte. „Klartext-DNS“ meint, ob der Dienst auf Port 53 unverschlüsselt "
                       "antwortet; wo nicht, ist er nur über DoT oder DoH nutzbar."),
        "updated": "Stand", "updated_val": "6. September 2026",
        "footer_note": ("Diese Seite ist eine technische Darstellung und keine Rechtsberatung. Sie führt kein Skript aus, "
                        "setzt kein Cookie und lädt nichts von fremden Servern."),
        "src_intro": "Alle Quellen wurden am 6. September 2026 abgerufen.",
        "source_link": "Quelltext auf GitHub",
    },
    "en": {
        "lang": "en", "locale": "en_GB", "other_locale": "de_DE",
        "title": "Secure DNS servers: verified providers and self-hosting",
        "brand": "Secure DNS servers",
        "desc": ("Eleven public DNS resolvers and six ways to self-host, checked against the primary "
                 "source on 6 September 2026: addresses, who runs them, caveats."),
        "tagline": "Which resolver you use decides who gets to read every name you look up.",
        "switch": "Deutsche Fassung", "switch_url": URL_DE,
        "nav": "Contents",
        "toc": [("was", "What DNS reveals"), ("grenzen", "What encrypted DNS does not do"),
                ("protokolle", "The protocols"), ("auswahl", "How to recognise a good provider"),
                ("anbieter", "The providers in detail"), ("warnung", "Do not use these any more"),
                ("kommerziell", "The large commercial services"), ("selbst", "Running your own"),
                ("einrichten", "Setting it up"), ("recht", "The legal framework in Germany"),
                ("faq", "Frequently asked questions"), ("methode", "How this page was checked"),
                ("quellen", "Sources")],
        "h_was": "What DNS reveals about you",
        "h_grenzen": "What encrypted DNS does not do",
        "h_protokolle": "The protocols, briefly and correctly",
        "h_auswahl": "How to recognise a good provider",
        "h_anbieter": "The providers in detail",
        "h_warnung": "Do not use these any more",
        "h_kommerziell": "The large commercial services",
        "h_selbst": "Running your own",
        "h_einrichten": "Setting it up",
        "h_recht": "The legal framework in Germany",
        "h_faq": "Frequently asked questions",
        "h_methode": "How this page was checked",
        "h_quellen": "Sources",
        "l_operator": "Operator", "l_carrier": "Legal form", "l_endpoints": "Endpoints",
        "l_doq": "DNS over QUIC", "l_dnssec": "DNSSEC", "l_filter": "Filtering",
        "l_logging": "Logging", "l_strengths": "What speaks for it",
        "l_caveats": "What speaks against it", "l_sources": "Evidence",
        "l_ipv4": "IPv4", "l_ipv6": "IPv6", "l_doh": "DoH", "l_dot": "DoT",
        "l_license": "Licence", "l_kind": "What it is", "l_by": "Published by",
        "l_state": "Status", "l_addresses": "Addresses",
        "overview": "Overview",
        "table_caption": "The eleven verified resolvers at a glance",
        "th_name": "Service", "th_carrier": "Legal form", "th_country": "Based in",
        "th_filter": "Unfiltered address", "th_plain": "Plaintext DNS",
        "yes": "yes", "no": "no", "limited": "with caveats",
        "table_note": ("“With caveats” means there is an address without a content filter, but the operator also "
                       "implements court-ordered or statutory blocks on it. The details are in the respective card. "
                       "“Plaintext DNS” indicates whether the service answers unencrypted on port 53; where it does "
                       "not, it can only be used over DoT or DoH."),
        "updated": "Last checked", "updated_val": "6 September 2026",
        "footer_note": ("This page is a technical description, not legal advice. It runs no script, sets no cookie "
                        "and loads nothing from third-party servers."),
        "src_intro": "All sources were retrieved on 6 September 2026.",
        "source_link": "Source code on GitHub",
    },
}


def e(s):
    return html.escape(str(s), quote=False)


def para(text):
    """Absätze aus einem Rohtext, Zeilenumbrüche innerhalb eines Absatzes werden geglättet."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        out.append("<p>" + e(" ".join(block.split())) + "</p>")
    return "\n".join(out)


def src_title(entry, lang):
    """Quelleneintrag ist (url, titel_de, titel_en); zweistellige Eintraege gelten fuer beide Sprachen."""
    url, de = entry[0], entry[1]
    en = entry[2] if len(entry) > 2 else de
    return url, (en if lang == "en" else de)


def pick(d, key, lang):
    """Sprachvariante holen: key für Deutsch, key_en für Englisch, mit Rückfall."""
    if lang == "en":
        return d.get(key + "_en") or d.get(key)
    return d.get(key)


# WCAG 2.2, Erfolgskriterium 3.1.2 "Language of Parts": Die Seite zitiert
# durchgehend woertlich, und diese Zitate stehen oft in der jeweils anderen
# Sprache. Ohne Auszeichnung liest ein Screenreader sie mit falscher Aussprache
# vor. Die folgende Funktion zeichnet genau die Zitatspannen aus, deren Sprache
# von der Seitensprache abweicht, und laesst alles Uneindeutige unberuehrt.

_DE_WORDS = set("""der die das und nicht kein keine wir ist im fuer für ohne wird dass bei eine einer
einen auf von zu mit sich auch nur oder als aber wenn man dem den des werden sind war haben hat
diese dieser dieses ihre ihren unsere unser alle beim durch nach vor über unter zum zur""".split())
_EN_WORDS = set("""the and not no we is are of to in for that with this does do you your our it its
be by on as at from can will would there their they has have was were any all other than which who
what when where how must should may""".split())
_QUOTES = [("\u201e", "\u201c", "de"), ("\u201c", "\u201d", "en")]


def _guess_lang(text):
    """Sprache einer Zitatspanne raten. Gibt None zurueck, wenn es nicht eindeutig ist."""
    plain = re.sub(r"<[^>]+>", " ", text)
    plain = re.sub(r"&[a-z]+;|&#\d+;", " ", plain)
    words = re.findall(r"[A-Za-zÄÖÜäöüß]+", plain)
    if not any(len(w) >= 3 for w in words):
        return None
    low = [w.lower() for w in words]
    de = sum(1 for w in low if w in _DE_WORDS) + sum(1 for w in words if re.search(r"[ÄÖÜäöüß]", w))
    en = sum(1 for w in low if w in _EN_WORDS)
    if de > en:
        return "de"
    if en > de:
        return "en"
    return None


def mark_quote_languages(body, page_lang):
    """Zitate in der jeweils anderen Sprache mit lang-Attribut versehen."""
    out = []
    for chunk in re.split(r"(<[^>]+>)", body):
        if chunk.startswith("<"):
            out.append(chunk)
            continue
        for open_q, close_q, _ in _QUOTES:
            def repl(m, o=open_q, c=close_q):
                inner = m.group(1)
                lang = _guess_lang(inner)
                if lang is None or lang == page_lang:
                    return m.group(0)
                return '%s<span lang="%s">%s</span>%s' % (o, lang, inner, c)
            chunk = re.sub(re.escape(open_q) + r"([^" + re.escape(open_q + close_q) + r"]{2,400}?)" + re.escape(close_q),
                           repl, chunk)
        out.append(chunk)
    return "".join(out)


CSS = """
:root{
  --bg:#fbfaf7; --panel:#ffffff; --ink:#22201d; --muted:#5c574f;
  --line:#e3ded4; --line-strong:#cec7b8;
  --accent:#0f5c4a; --accent-ink:#0b4436;
  --warn-bg:#fdf4ec; --warn-line:#d8a06a; --warn-ink:#7a4310;
  --stop-bg:#fcf0ef; --stop-line:#c98a84; --stop-ink:#7d2b23;
  --good:#0f5c4a; --code-bg:#f2efe8;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#14161a; --panel:#1b1e24; --ink:#e6e3dd; --muted:#a5a096;
    --line:#2c3038; --line-strong:#3d434d;
    --accent:#5fc0a4; --accent-ink:#8ad6bf;
    --warn-bg:#2a2118; --warn-line:#7a5628; --warn-ink:#e8b579;
    --stop-bg:#2b1a18; --stop-line:#7d3b34; --stop-ink:#f0a49a;
    --good:#5fc0a4; --code-bg:#22262d;
  }
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{
  margin:0;background:var(--bg);color:var(--ink);
  font-family:var(--serif);font-size:1.0625rem;line-height:1.72;
  text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;
}
.wrap{max-width:52rem;margin:0 auto;padding:0 1.25rem}
a{color:var(--accent-ink);text-underline-offset:.16em;text-decoration-thickness:.06em}
a:hover,a:focus-visible{text-decoration-thickness:.14em}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:2px}
h1,h2,h3,h4{font-family:var(--sans);line-height:1.22;text-wrap:balance;font-weight:700}
h1{font-size:clamp(2rem,5.2vw,3.05rem);letter-spacing:-.022em;margin:0 0 .6rem}
h2{font-size:clamp(1.42rem,3.1vw,1.95rem);letter-spacing:-.014em;margin:4.2rem 0 1.1rem;
   padding-bottom:.45rem;border-bottom:2px solid var(--line-strong)}
h3{font-size:1.2rem;margin:2.4rem 0 .7rem;letter-spacing:-.008em}
h4{font-size:.83rem;margin:1.5rem 0 .35rem;text-transform:uppercase;letter-spacing:.09em;color:var(--muted);font-weight:700}
p{margin:0 0 1.15rem;text-wrap:pretty;hyphens:auto}
ul,ol{margin:0 0 1.15rem;padding-left:1.3rem}
li{margin:0 0 .5rem}
strong{font-weight:700}
code,kbd{font-family:var(--mono);font-size:.855em;background:var(--code-bg);
  padding:.13em .38em;border-radius:4px;border:1px solid var(--line);word-break:break-all}
.skip{position:absolute;left:-9999px}
.skip:focus{left:1rem;top:1rem;z-index:20;background:var(--panel);padding:.6rem 1rem;
  border:2px solid var(--accent);border-radius:6px}

/* Kopf */
header.top{background:var(--panel);border-bottom:1px solid var(--line);padding:3.6rem 0 2.6rem}
.eyebrow{font-family:var(--sans);font-size:.76rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--accent);font-weight:700;margin:0 0 .9rem}
.lede{font-size:1.2rem;color:var(--muted);margin:0 0 1.5rem;max-width:40rem;font-style:italic}
.meta{font-family:var(--sans);font-size:.83rem;color:var(--muted);display:flex;flex-wrap:wrap;
  gap:.55rem 1.1rem;align-items:center;margin:0}
.langswitch{font-family:var(--sans);font-size:.85rem;font-weight:600;display:inline-block;
  border:1px solid var(--muted);border-radius:999px;padding:.3rem .9rem;text-decoration:none}
.langswitch:hover{border-color:var(--accent);background:var(--panel)}

/* Inhaltsverzeichnis */
nav.toc{background:var(--panel);border:1px solid var(--line);border-radius:10px;
  padding:1.4rem 1.5rem;margin:2.6rem 0}
nav.toc h2{font-size:.78rem;text-transform:uppercase;letter-spacing:.11em;color:var(--muted);
  border:0;margin:0 0 .7rem;padding:0}
nav.toc ol{columns:2;column-gap:2rem;margin:0;padding-left:1.15rem;font-family:var(--sans);font-size:.93rem}
nav.toc li{margin:0 0 .35rem;break-inside:avoid}
@media(max-width:34rem){nav.toc ol{columns:1}}

/* Karten */
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;
  padding:1.6rem 1.65rem;margin:1.6rem 0}
.card h3{margin-top:0;display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap}
.tag{font-family:var(--sans);font-size:.68rem;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;border:1px solid var(--line-strong);border-radius:999px;
  padding:.16rem .55rem;color:var(--muted);white-space:nowrap}
.card.warn{background:var(--warn-bg);border-color:var(--warn-line)}
.card.warn .tag{border-color:var(--warn-line);color:var(--warn-ink)}
.card.stop{background:var(--stop-bg);border-color:var(--stop-line)}
.card.stop .tag{border-color:var(--stop-line);color:var(--stop-ink)}

/* Definitionslisten */
dl.facts{margin:0 0 1rem;display:grid;grid-template-columns:auto 1fr;gap:.3rem 1.1rem;
  font-size:.97rem;align-items:baseline}
dl.facts dt{font-family:var(--sans);font-size:.74rem;text-transform:uppercase;letter-spacing:.07em;
  color:var(--muted);font-weight:700;padding-top:.18rem}
dl.facts dd{margin:0}
@media(max-width:36rem){dl.facts{grid-template-columns:1fr;gap:.1rem}
  dl.facts dd{margin:0 0 .7rem}}

/* Endpunkt-Blöcke */
.ep{border-left:3px solid var(--line-strong);padding:.1rem 0 .1rem .9rem;margin:.9rem 0}
.ep .epname{font-family:var(--sans);font-size:.86rem;font-weight:700;margin:0 0 .35rem}
.ep dl{display:grid;grid-template-columns:3.2rem 1fr;gap:.16rem .7rem;margin:0;font-size:.92rem}
.ep dt{font-family:var(--sans);font-size:.7rem;text-transform:uppercase;letter-spacing:.06em;
  color:var(--muted);font-weight:700;padding-top:.22rem}
.ep dd{margin:0}

/* Tabelle */
.tablewrap{overflow-x:auto;margin:1.5rem 0;border:1px solid var(--line);border-radius:10px;background:var(--panel)}
caption{caption-side:top;text-align:left;padding:.75rem .85rem .1rem;font-family:var(--sans);
  font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);font-weight:700}
table{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:.9rem;min-width:34rem}
th,td{padding:.62rem .85rem;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:.72rem;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);
  border-bottom:2px solid var(--line-strong);white-space:nowrap}
tbody tr:last-child td,tbody tr:last-child th{border-bottom:0}
tbody th{font-weight:400}
td.yes{color:var(--good);font-weight:700}
td.no{color:var(--muted)}

/* Listen mit Vor- und Nachteilen */
ul.pro,ul.con{list-style:none;padding-left:1.6rem}
ul.pro li,ul.con li{position:relative}
ul.pro li::before{content:"+";position:absolute;left:-1.25rem;color:var(--good);font-weight:700}
ul.con li::before{content:"!";position:absolute;left:-1.2rem;color:var(--warn-ink);font-weight:700}

/* Quellen */
ul.src{list-style:none;padding:0;font-family:var(--sans);font-size:.87rem}
ul.src li{margin:0 0 .42rem;padding-left:1.1rem;text-indent:-1.1rem}
.srcnote{font-family:var(--sans);font-size:.83rem;color:var(--muted)}

blockquote{margin:1.3rem 0;padding:.2rem 0 .2rem 1.1rem;border-left:3px solid var(--accent);
  color:var(--muted);font-style:italic}

footer{border-top:1px solid var(--line);margin-top:4.5rem;padding:2.4rem 0 3.5rem;
  font-family:var(--sans);font-size:.87rem;color:var(--muted)}
footer a{color:var(--accent-ink)}
"""


SETUP = {
    "de": [
        ("Android", "Einstellungen, Netzwerk und Internet, Privates DNS. Dort wird ein DoT-Hostname eingetragen, "
                    "zum Beispiel <code>dns.quad9.net</code>. Android nutzt ausschließlich DNS over TLS; eine "
                    "DoH-Adresse oder eine reine IP-Adresse funktioniert an dieser Stelle nicht. Die Einstellung "
                    "gilt systemweit und auch im Mobilfunknetz."),
        ("iOS, iPadOS und macOS", "Apple bietet keine Eingabemaske für DoH oder DoT. Verschlüsseltes DNS wird über "
                    "ein DNS-Konfigurationsprofil gesetzt, das ein Anbieter bereitstellt, oder über eine App, die ein "
                    "solches Profil installiert. Ein im Netzwerk-Dialog eingetragener DNS-Server bleibt unverschlüsseltes "
                    "Klartext-DNS."),
        ("Windows 11", "Einstellungen, Netzwerk und Internet, Adapter, DNS-Serverzuweisung bearbeiten. Nach dem Eintragen "
                    "einer IP-Adresse lässt sich die DNS-Verschlüsselung auf „Nur verschlüsselt“ stellen, sofern Windows "
                    "für diese Adresse einen DoH-Endpunkt kennt. Für die Adressen von Quad9 und Cloudflare ist das der Fall."),
        ("Linux mit systemd-resolved", "In <code>/etc/systemd/resolved.conf</code> die Werte <code>DNS=</code>, "
                    "<code>DNSOverTLS=yes</code> und <code>DNSSEC=</code> setzen, danach <code>systemctl restart "
                    "systemd-resolved</code>. Bei DoT gehört hinter die IP-Adresse der Hostname für die Zertifikatsprüfung, "
                    "etwa <code>9.9.9.9#dns.quad9.net</code>."),
        ("Firefox", "Einstellungen, Datenschutz und Sicherheit, DNS über HTTPS. Neben den vorgegebenen Anbietern lässt sich "
                    "unter „Benutzerdefiniert“ jede DoH-Adresse aus den Tabellen oben eintragen. Diese Einstellung gilt nur "
                    "für Firefox, nicht für das übrige System."),
        ("Router", "Der wirksamste Ort, denn die Einstellung erreicht jedes Gerät im Netz, auch Fernseher und Drucker. "
                    "Viele Router unterstützen nur Klartext-DNS. Dann gehören dort die IPv4- und IPv6-Adressen hinein, und "
                    "die Verschlüsselung übernimmt ein eigener Resolver im Netz, siehe den Abschnitt „Selbst betreiben“."),
    ],
    "en": [
        ("Android", "Settings, Network and internet, Private DNS. Enter a DoT hostname there, for example "
                    "<code>dns.quad9.net</code>. Android uses DNS over TLS exclusively; a DoH URL or a bare IP address "
                    "will not work in this field. The setting applies system-wide, including on mobile networks."),
        ("iOS, iPadOS and macOS", "Apple provides no input field for DoH or DoT. Encrypted DNS is set through a DNS "
                    "configuration profile supplied by a provider, or through an app that installs such a profile. A DNS "
                    "server entered in the network dialogue remains unencrypted plaintext DNS."),
        ("Windows 11", "Settings, Network and internet, Adapter, Edit DNS server assignment. After entering an IP address, "
                    "DNS encryption can be set to “Encrypted only”, provided Windows knows a DoH endpoint for that address. "
                    "It does for the Quad9 and Cloudflare addresses."),
        ("Linux with systemd-resolved", "In <code>/etc/systemd/resolved.conf</code> set <code>DNS=</code>, "
                    "<code>DNSOverTLS=yes</code> and <code>DNSSEC=</code>, then run <code>systemctl restart "
                    "systemd-resolved</code>. With DoT the hostname for certificate verification goes after the IP address, "
                    "for example <code>9.9.9.9#dns.quad9.net</code>."),
        ("Firefox", "Settings, Privacy and Security, DNS over HTTPS. Besides the preset providers, any DoH URL from the "
                    "tables above can be entered under “Custom”. This setting applies to Firefox only, not to the rest of "
                    "the system."),
        ("Router", "The most effective place, because the setting reaches every device on the network, including televisions "
                    "and printers. Many routers support plaintext DNS only. In that case the IPv4 and IPv6 addresses go there, "
                    "and a resolver of your own on the network handles the encryption; see the section on running your own."),
    ],
}


def provider_card(p, lang, t):
    o = []
    o.append('<article class="card" id="p-%s">' % e(p["id"]))
    o.append("<h3>%s <span class=\"tag\">%s</span></h3>" % (e(p["name"]), e(p["flag"])))
    o.append('<dl class="facts">')
    o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_operator"], e(pick(p, "operator", lang))))
    o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_carrier"], e(pick(p, "carrier", lang))))
    o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_dnssec"], e(pick(p, "dnssec", lang))))
    o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_doq"], e(pick(p, "doq", lang))))
    o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_filter"], e(pick(p, "filtering", lang))))
    o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_logging"], e(pick(p, "logging", lang))))
    o.append("</dl>")

    o.append("<h4>%s</h4>" % t["l_endpoints"])
    for label_de, label_en, v4, v6, doh, dot in p["endpoints"]:
        label = label_en if lang == "en" else label_de
        o.append('<div class="ep"><p class="epname">%s</p><dl>' % e(label))
        if v4:
            o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_ipv4"], " &middot; ".join("<code>%s</code>" % e(x) for x in v4)))
        if v6:
            o.append("<dt>%s</dt><dd>%s</dd>" % (t["l_ipv6"], " &middot; ".join("<code>%s</code>" % e(x) for x in v6)))
        if doh:
            o.append("<dt>%s</dt><dd><code>%s</code></dd>" % (t["l_doh"], e(doh)))
        if dot:
            o.append("<dt>%s</dt><dd><code>%s</code></dd>" % (t["l_dot"], e(dot)))
        o.append("</dl></div>")

    o.append("<h4>%s</h4><ul class=\"pro\">" % t["l_strengths"])
    for s in pick(p, "strengths", lang):
        o.append("<li>%s</li>" % e(s))
    o.append("</ul>")

    o.append("<h4>%s</h4><ul class=\"con\">" % t["l_caveats"])
    for s in pick(p, "caveats", lang):
        o.append("<li>%s</li>" % e(s))
    o.append("</ul>")

    o.append("<h4>%s</h4><ul class=\"src\">" % t["l_sources"])
    for entry in p["sources"]:
        url, title = src_title(entry, lang)
        o.append('<li><a href="%s" rel="noopener nofollow">%s</a></li>' % (e(url), e(title)))
    o.append("</ul></article>")
    return "\n".join(o)


def overview_table(lang, t):
    rows = []
    for p in C.PROVIDERS:
        unf = p["unfiltered"]
        cls = {"yes": "yes", "limited": "no", "no": "no"}[unf]
        label = {"yes": t["yes"], "limited": t["limited"], "no": t["no"]}[unf]
        plain = p["plain53"]
        rows.append(
            "<tr><th scope=\"row\"><a href=\"#p-%s\">%s</a></th><td>%s</td><td>%s</td>"
            "<td class=\"%s\">%s</td><td class=\"%s\">%s</td></tr>" % (
                e(p["id"]), e(p["name"]), e(pick(p, "carrier", lang)), e(p["flag"]),
                cls, e(label),
                "yes" if plain else "no", t["yes"] if plain else t["no"]))
    return ('<div class="tablewrap" tabindex="0" role="region" aria-label="%s">' % e(t["overview"])
            + '<table><caption>%s</caption><thead><tr>'
            '<th scope="col">%s</th><th scope="col">%s</th><th scope="col">%s</th>'
            '<th scope="col">%s</th><th scope="col">%s</th></tr></thead><tbody>%s</tbody></table></div>'
            '<p class="srcnote">%s</p>' % (
                e(t["table_caption"]),
                t["th_name"], t["th_carrier"], t["th_country"], t["th_filter"], t["th_plain"],
                "".join(rows), e(t["table_note"])))


INTRO = {
    "de": """Jedes Mal, wenn ein Gerät eine Adresse aufruft, fragt es zuerst einen Namensserver, welche IP-Adresse
dahintersteht. In der Voreinstellung ist das der Server des Zugangsanbieters, und in der Voreinstellung läuft diese
Frage im Klartext über das Netz.

Daraus entsteht eine vollständige, zeitlich sortierte Liste dessen, was ein Anschluss abruft. RFC 9076, das
IETF-Dokument zu den Datenschutzaspekten des DNS, beschreibt die Tragweite an einem Beispiel: Der Aufruf der Website
der Anonymen Alkoholiker sagt etwas über eine Person aus, das sie nicht notwendigerweise preisgeben wollte. Nicht der
einzelne Abruf ist das Problem, sondern die Verknüpfbarkeit vieler Abrufe über die Zeit.

Diese Seite listet Namensserver, die man statt des voreingestellten benutzen kann, und Wege, einen eigenen zu
betreiben. Sie nennt zu jedem Dienst auch, was gegen ihn spricht. Ein Verzeichnis, das nur Vorteile aufzählt, ist
Werbung und keine Hilfe bei einer Entscheidung.""",
    "en": """Every time a device connects to a domain name, it first asks a name server which IP address belongs to that name. By default
that is the access provider’s server, and by default the question travels across the network in the clear.

The result is a complete, chronologically ordered list of what a connection requests. RFC 9076, the IETF document on
DNS privacy considerations, illustrates the significance with an example: visiting the Alcoholics Anonymous website
says something about a person that they did not necessarily intend to disclose. The problem is not the single lookup
but the linkability of many lookups over time.

This page lists name servers you can use instead of the preset one, and ways to run your own. For each service it also
states what speaks against it. A directory that lists only advantages is advertising, not help with a decision.""",
}

SELF_INTRO = {
    "de": """Wer den Resolver selbst betreibt, tauscht einen fremden Betreiber gegen die eigene Verantwortung. Das ist ein
echter Gewinn, aber ein begrenzter, und die Projekte selbst sagen das am deutlichsten.

Bei echter Rekursion, also wenn die eigene Software ab den Root-Servern auflöst, gibt es keinen zentralen Dienst mehr,
der die gesamte Abfragehistorie sieht. Dafür laufen die einzelnen Anfragen nun an Root-, TLD- und autoritative Server,
und je kleiner das eigene Netz ist, desto weniger verschwinden sie in der Menge. Der Gewinn liegt in der Verteilung, nicht
in der Unsichtbarkeit.

Wichtig ist die Unterscheidung, die Werbetexte gern verwischen: Pi-hole, AdGuard Home und blocky sind Filter, keine
Resolver. Sie geben die Anfrage weiter. Nur Unbound, Knot Resolver und Technitium lösen selbst auf.""",
    "en": """Running the resolver yourself exchanges someone else’s operation for your own responsibility. That is a real gain,
but a limited one, and the projects themselves say so most clearly.

With real recursion, meaning your own software resolves from the root servers, there is no longer a central service that
sees the entire query history. In exchange the individual queries now go to root, TLD and authoritative servers, and the
smaller your network, the less they disappear into the crowd. The gain lies in distribution, not in invisibility.

The distinction that marketing copy likes to blur matters here: Pi-hole, AdGuard Home and blocky are filters, not
resolvers. They pass the query on. Only Unbound, Knot Resolver and Technitium resolve by themselves.""",
}

COMM_INTRO = {
    "de": """Diese drei sind die meistgenutzten öffentlichen Resolver. Sie stehen hier zur Einordnung, nicht als Empfehlung.
Alle drei gehören Unternehmen, die ihr Geld an anderer Stelle verdienen, und in allen drei Fällen ist die Zusage zum
Umgang mit den Daten eine Selbstauskunft des Unternehmens. Das macht sie nicht schlecht; es macht sie nur zu einer
anderen Art von Entscheidung.""",
    "en": """These three are the most widely used public resolvers. They appear here for context, not as a recommendation. All
three belong to companies that earn their money elsewhere, and in all three cases the commitment on data handling is the
company’s own declaration. That does not make them bad; it merely makes them a different kind of decision.""",
}


def build_page(lang):
    t = T[lang]
    url = URL_DE if lang == "de" else URL_EN
    o = []
    A = o.append

    A('<a class="skip" href="#main">%s</a>' % ("Zum Inhalt springen" if lang == "de" else "Skip to content"))
    A('<header class="top"><div class="wrap">')
    A('<p class="eyebrow">dns.kaipfstr.de</p>')
    A("<h1>%s</h1>" % e(t["brand"]))
    A('<p class="lede">%s</p>' % e(t["tagline"]))
    A('<p class="meta"><a class="langswitch" href="%s" hreflang="%s" lang="%s">%s</a>'
      "<span>%s: %s</span></p>" % (
          e(t["switch_url"]), "en" if lang == "de" else "de", "en" if lang == "de" else "de",
          e(t["switch"]), e(t["updated"]), e(t["updated_val"])))
    A("</div></header>")

    A('<main id="main"><div class="wrap">')

    A('<nav class="toc" aria-label="%s"><h2>%s</h2><ol>' % (e(t["nav"]), e(t["nav"])))
    for anchor, label in t["toc"]:
        A('<li><a href="#%s">%s</a></li>' % (anchor, e(label)))
    A("</ol></nav>")

    A('<section id="was"><h2>%s</h2>' % e(t["h_was"]))
    A(para(INTRO[lang]))
    A("</section>")

    A('<section id="grenzen"><h2>%s</h2>' % e(t["h_grenzen"]))
    A(para(C.LIMITS_DE if lang == "de" else C.LIMITS_EN))
    A("</section>")

    A('<section id="protokolle"><h2>%s</h2>' % e(t["h_protokolle"]))
    for p in C.PROTOCOLS:
        A('<article class="card"><h3>%s <span class="tag">%s</span> <span class="tag">%s</span></h3>' % (
            e(pick(p, "title", lang)), e(p["abbr"]), e(p["rfc"])))
        A('<p class="srcnote">%s</p>' % e(pick(p, "port", lang)))
        A(para(pick(p, "de", lang) if lang == "de" else p["en"]))
        A("</article>")
    A("</section>")

    A('<section id="auswahl"><h2>%s</h2>' % e(t["h_auswahl"]))
    for q_de, q_en, a_de, a_en in C.CRITERIA:
        A("<h3>%s</h3>" % e(q_en if lang == "en" else q_de))
        A("<p>%s</p>" % e(a_en if lang == "en" else a_de))
    A("</section>")

    A('<section id="anbieter"><h2>%s</h2>' % e(t["h_anbieter"]))
    A("<h3>%s</h3>" % e(t["overview"]))
    A(overview_table(lang, t))
    for p in C.PROVIDERS:
        A(provider_card(p, lang, t))
    A("</section>")

    A('<section id="warnung"><h2>%s</h2>' % e(t["h_warnung"]))
    for d in C.DISCONTINUED:
        A('<article class="card stop" id="p-%s"><h3>%s <span class="tag">%s</span></h3>' % (
            e(d["id"]), e(d["name"]), e(d["state_en"] if lang == "en" else d["state"])))
        A(para(d["en"] if lang == "en" else d["de"]))
        A('<h4>%s</h4><ul class="src">' % t["l_sources"])
        for entry in d["sources"]:
            u, ti = src_title(entry, lang)
            A('<li><a href="%s" rel="noopener nofollow">%s</a></li>' % (e(u), e(ti)))
        A("</ul></article>")
    A("</section>")

    A('<section id="kommerziell"><h2>%s</h2>' % e(t["h_kommerziell"]))
    A(para(COMM_INTRO[lang]))
    for c in C.COMMERCIAL:
        A('<article class="card"><h3>%s</h3>' % e(c["name"]))
        A('<dl class="facts"><dt>%s</dt><dd>%s</dd></dl>' % (
            t["l_addresses"], e(c["addresses_en"] if lang == "en" else c["addresses"])))
        A(para(c["en"] if lang == "en" else c["de"]))
        cu, cti = src_title(c["source"], lang)
        A('<ul class="src"><li><a href="%s" rel="noopener nofollow">%s</a></li></ul>' % (e(cu), e(cti)))
        A("</article>")
    A("</section>")

    A('<section id="selbst"><h2>%s</h2>' % e(t["h_selbst"]))
    A(para(SELF_INTRO[lang]))
    for s in C.SELFHOSTED:
        A('<article class="card"><h3>%s <span class="tag">%s</span></h3>' % (e(s["name"]), e(s["license"])))
        A('<dl class="facts"><dt>%s</dt><dd>%s</dd><dt>%s</dt><dd>%s</dd></dl>' % (
            t["l_kind"], e(pick(s, "kind", lang)), t["l_by"], e(pick(s, "by", lang))))
        A(para(s["en"] if lang == "en" else s["de"]))
        A('<ul class="src">')
        for entry in s["sources"]:
            u, ti = src_title(entry, lang)
            A('<li><a href="%s" rel="noopener nofollow">%s</a></li>' % (e(u), e(ti)))
        A("</ul></article>")
    A("</section>")

    A('<section id="einrichten"><h2>%s</h2>' % e(t["h_einrichten"]))
    A("<p>%s</p>" % e(
        "Die Menüpfade unterscheiden sich zwischen Versionen. Entscheidend ist, welches Protokoll das jeweilige System spricht."
        if lang == "de" else
        "Menu paths differ between versions. What matters is which protocol the system in question speaks."))
    for name, body in SETUP[lang]:
        A("<h3>%s</h3><p>%s</p>" % (e(name), body))
    A("</section>")

    A('<section id="recht"><h2>%s</h2>' % e(t["h_recht"]))
    A(para(C.LEGAL_DE if lang == "de" else C.LEGAL_EN))
    A('<h3>%s</h3><ul class="src">' % t["l_sources"])
    for entry in C.LEGAL_SOURCES:
        u, ti = src_title(entry, lang)
        A('<li><a href="%s" rel="noopener nofollow">%s</a></li>' % (e(u), e(ti)))
    A("</ul></section>")

    A('<section id="faq"><h2>%s</h2>' % e(t["h_faq"]))
    for q_de, q_en, a_de, a_en in C.FAQ:
        A("<h3>%s</h3><p>%s</p>" % (e(q_en if lang == "en" else q_de), e(a_en if lang == "en" else a_de)))
    A("</section>")

    A('<section id="methode"><h2>%s</h2>' % e(t["h_methode"]))
    A(para(C.METHOD_DE if lang == "de" else C.METHOD_EN))
    A("</section>")

    A('<section id="quellen"><h2>%s</h2>' % e(t["h_quellen"]))
    A('<p class="srcnote">%s</p>' % e(t["src_intro"]))
    seen, items = set(), []
    for p in C.PROVIDERS:
        items += p["sources"]
    for d in C.DISCONTINUED:
        items += d["sources"]
    for c in C.COMMERCIAL:
        items.append(c["source"])
    for s in C.SELFHOSTED:
        items += s["sources"]
    items += C.LEGAL_SOURCES
    items += [
        ("https://www.rfc-editor.org/rfc/rfc1035.txt", "RFC 1035, Domain Names, Implementation and Specification"),
        ("https://www.rfc-editor.org/rfc/rfc4033.txt", "RFC 4033, DNS Security Introduction and Requirements"),
        ("https://www.rfc-editor.org/rfc/rfc7816.txt", "RFC 7816, DNS Query Name Minimisation to Improve Privacy (überholt durch RFC 9156)",
         "RFC 7816, DNS Query Name Minimisation to Improve Privacy (obsoleted by RFC 9156)"),
        ("https://www.rfc-editor.org/rfc/rfc7830.txt", "RFC 7830, The EDNS(0) Padding Option"),
        ("https://www.rfc-editor.org/rfc/rfc7858.txt", "RFC 7858, Specification for DNS over Transport Layer Security"),
        ("https://www.rfc-editor.org/rfc/rfc7871.txt", "RFC 7871, Client Subnet in DNS Queries"),
        ("https://www.rfc-editor.org/rfc/rfc8484.txt", "RFC 8484, DNS Queries over HTTPS"),
        ("https://www.rfc-editor.org/rfc/rfc8932.txt", "RFC 8932, Recommendations for DNS Privacy Service Operators"),
        ("https://www.rfc-editor.org/rfc/rfc9076.txt", "RFC 9076, DNS Privacy Considerations"),
        ("https://www.rfc-editor.org/rfc/rfc9156.txt", "RFC 9156, DNS Query Name Minimisation to Improve Privacy"),
        ("https://www.rfc-editor.org/rfc/rfc9230.txt", "RFC 9230, Oblivious DNS over HTTPS"),
        ("https://www.rfc-editor.org/rfc/rfc9250.txt", "RFC 9250, DNS over Dedicated QUIC Connections"),
        ("https://www.rfc-editor.org/rfc/rfc9849.txt", "RFC 9849, TLS Encrypted Client Hello"),
    ]
    A('<ul class="src">')
    for entry in items:
        u, ti = src_title(entry, lang)
        if u in seen:
            continue
        seen.add(u)
        A('<li><a href="%s" rel="noopener nofollow">%s</a></li>' % (e(u), e(ti)))
    A("</ul></section>")

    A("</div></main>")

    A('<footer><div class="wrap"><p>%s</p>' % e(t["footer_note"]))
    A('<p><a href="%s" hreflang="%s" lang="%s">%s</a> &middot; '
      '<a href="https://github.com/Wasserpuncher/dns.kaipfstr.de" rel="noopener">%s</a></p>'
      % (e(t["switch_url"]), "en" if lang == "de" else "de", "en" if lang == "de" else "de",
         e(t["switch"]), e(t["source_link"])))
    A("</div></footer>")
    return "\n".join(o), t, url


def json_ld(lang, t, url):
    other = URL_EN if lang == "de" else URL_DE
    def q(s):
        return json_escape(s)
    items = ",".join(
        '{"@type":"ListItem","position":%d,"item":{"@type":"Organization","name":"%s","url":"%s"}}'
        % (i + 1, q(p["name"]), q(p["sources"][0][0]))
        for i, p in enumerate(C.PROVIDERS))
    faqs = ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
        % (q(a if lang == "en" else qd), q(d if lang == "en" else dd))
        for qd, a, dd, d in C.FAQ)
    return (
        '{"@context":"https://schema.org","@graph":['
        '{"@type":"WebSite","@id":"%(base)s/#website","url":"%(base)s/","name":"dns.kaipfstr.de",'
        '"inLanguage":["de","en"],"publisher":{"@id":"%(base)s/#person"}},'
        '{"@type":"Person","@id":"%(base)s/#person","name":"Kai Pfister","url":"https://github.com/Wasserpuncher"},'
        '{"@type":"WebPage","@id":"%(url)s#webpage","url":"%(url)s","name":"%(title)s",'
        '"description":"%(desc)s","inLanguage":"%(lang)s","isPartOf":{"@id":"%(base)s/#website"},'
        '"author":{"@id":"%(base)s/#person"},"dateModified":"%(mod)s",'
        '"breadcrumb":{"@id":"%(url)s#breadcrumb"},"license":"https://opensource.org/licenses/MIT"},'
        '{"@type":"BreadcrumbList","@id":"%(url)s#breadcrumb","itemListElement":[%(crumbs)s]},'
        '{"@type":"ItemList","@id":"%(url)s#providers","name":"%(listname)s",'
        '"numberOfItems":%(n)d,"itemListOrder":"https://schema.org/ItemListUnordered",'
        '"itemListElement":[%(items)s]},'
        '{"@type":"FAQPage","@id":"%(url)s#faq","inLanguage":"%(lang)s","mainEntity":[%(faqs)s]}'
        "]}" % {
            "base": BASE, "url": url, "other": other,
            "title": q(t["title"]), "desc": q(t["desc"]), "lang": t["lang"],
            "mod": "2026-09-06",
            "listname": q("Geprüfte öffentliche DNS-Resolver" if lang == "de"
                          else "Verified public DNS resolvers"),
            "n": len(C.PROVIDERS), "items": items, "faqs": faqs,
            "crumbs": ('{"@type":"ListItem","position":1,"name":"%s","item":"%s"}' % (q(t["title"]), BASE + "/")
                       if lang == "de" else
                       '{"@type":"ListItem","position":1,"name":"dns.kaipfstr.de","item":"%s"},'
                       '{"@type":"ListItem","position":2,"name":"%s","item":"%s"}'
                       % (BASE + "/", q(t["title"]), url)),
        })


def json_escape(s):
    return (s.replace("\\", "\\\\").replace('"', '\\"')
             .replace("\n", " ").replace("\r", " ").replace("\t", " "))


HEAD = """<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="author" content="Kai Pfister">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="theme-color" content="#0f5c4a">
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{URL}">
<link rel="alternate" hreflang="de" href="{URL_DE}">
<link rel="alternate" hreflang="en" href="{URL_EN}">
<link rel="alternate" hreflang="x-default" href="{URL_DE}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:site_name" content="dns.kaipfstr.de">
<meta property="og:locale" content="{LOCALE}">
<meta property="og:locale:alternate" content="{LOCALE_ALT}">
<link rel="icon" href="/icon.svg" type="image/svg+xml">
<style>{CSS}</style>
<script type="application/ld+json">{JSONLD}</script>"""


def write_page(lang):
    body, t, url = build_page(lang)
    head = (HEAD
            .replace("{TITLE}", html.escape(t["title"], quote=True))
            .replace("{DESC}", html.escape(t["desc"], quote=True))
            .replace("{URL_DE}", URL_DE)
            .replace("{URL_EN}", URL_EN)
            .replace("{URL}", url)
            .replace("{LOCALE_ALT}", t["other_locale"])
            .replace("{LOCALE}", t["locale"])
            .replace("{CSS}", CSS)
            .replace("{JSONLD}", json_ld(lang, t, url)))
    doc = ('<!DOCTYPE html>\n<html lang="%s" dir="ltr">\n<head>\n%s\n</head>\n<body>\n%s\n</body>\n</html>\n'
           % (t["lang"], head, mark_quote_languages(body, t["lang"])))
    path = OUT_DE if lang == "de" else OUT_EN
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(doc)
    return path, len(doc)


SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{DE}</loc>
    <lastmod>{MOD}</lastmod>
    <xhtml:link rel="alternate" hreflang="de" href="{DE}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{EN}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{DE}"/>
  </url>
  <url>
    <loc>{EN}</loc>
    <lastmod>{MOD}</lastmod>
    <xhtml:link rel="alternate" hreflang="de" href="{DE}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{EN}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{DE}"/>
  </url>
</urlset>
"""

ICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="dns.kaipfstr.de">
<rect width="64" height="64" rx="13" fill="#0f5c4a"/>
<path d="M32 13c-9 6-13 12-13 19 0 8 6 14 13 19 7-5 13-11 13-19 0-7-4-13-13-19z"
      fill="none" stroke="#fbfaf7" stroke-width="3.4" stroke-linejoin="round"/>
<path d="M23 30h18M32 13v38" fill="none" stroke="#fbfaf7" stroke-width="2.4" opacity=".75"/>
</svg>
"""


def main():
    for lang in ("de", "en"):
        path, size = write_page(lang)
        print("%-16s %6.1f KB" % (path, size / 1024))
    with open("sitemap.xml", "w", encoding="utf-8") as fh:
        fh.write(SITEMAP.replace("{DE}", URL_DE).replace("{EN}", URL_EN).replace("{MOD}", "2026-09-06"))
    print("sitemap.xml")
    with open("icon.svg", "w", encoding="utf-8") as fh:
        fh.write(ICON)
    print("icon.svg")


if __name__ == "__main__":
    main()
