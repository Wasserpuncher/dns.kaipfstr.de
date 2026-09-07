# dns.kaipfstr.de

*[Deutsche Fassung](README.md)*

**Twelve verified public DNS resolvers, six ways to self-host, fifteen commands to measure it yourself and a glossary
of thirty terms. Bilingual, every statement backed by a primary source.**

Live at [dns.kaipfstr.de](https://dns.kaipfstr.de/) and [dns.kaipfstr.de/en/](https://dns.kaipfstr.de/en/).

| Page | German | English |
| --- | --- | --- |
| Providers | [`/`](https://dns.kaipfstr.de/) | [`/en/`](https://dns.kaipfstr.de/en/) |
| Verify it yourself | [`/pruefen/`](https://dns.kaipfstr.de/pruefen/) | [`/en/verify/`](https://dns.kaipfstr.de/en/verify/) |
| Glossary | [`/glossar/`](https://dns.kaipfstr.de/glossar/) | [`/en/glossary/`](https://dns.kaipfstr.de/en/glossary/) |

## Why this site exists

There is no shortage of lists of "the best DNS servers". Most have two problems: they are out of date, and they name
only the advantages.

Compiling this one turned up the following points, among others, that recommendation lists still get wrong:

- **dns0.eu no longer exists.** Discontinued in October 2025; the domain now shows a parking page.
- **AhaDNS answers nowhere any more.** Of ten documented locations, eight no longer exist even as a name entry and the
  remaining two accept no connection. The website still lists the addresses unchanged.
- **`dns.digitalcourage.de` has been permanently shut down.** Only `dns3.digitalcourage.de` is active, and it offers
  no DoH.
- **Mullvad shuts down its public encrypted DNS service on 2 November 2026.**
- **DNS4EU is not a resolver operated by the EU.** The EU co-funding ran from 2023 to 2025. Today it is a free product
  of the Czech company Whalebone that retains query data for up to six months.
- **DNS.SB is run by xTom GmbH in Duesseldorf**, not by the widely cited "Xing Tech".
- **Digitale Gesellschaft, Artikel10, Applied Privacy and LibreDNS offer no plaintext DNS on port 53.** Entering their
  IP addresses in a router yields no resolution at all.
- **LibreDNS does not validate DNSSEC.** Evidenced three ways: its own documentation, its published configuration, and
  our own measurement.

## What this site does differently

- **For every service it states what speaks against it.** Including Quad9, which blocks worldwide because of a French
  ruling, and including every case where a no-log commitment is simply unaudited. That applies to all of them.
- **It quotes verbatim.** Logging commitments appear in the original wording, not as a charitable paraphrase.
- **It separates commitment from measurement.** The overview table distinguishes "DNSSEC: yes" from "measured only".
- **It shows what it left out, and why.** CIRA Canadian Shield would be exemplary on the merits, but its terms require
  you to represent that you are a resident of Canada.
- **It makes itself checkable.** The "Verify it yourself" page carries fifteen commands together with the output
  actually observed. Anyone who would rather not take the recommendations on trust can measure instead.
- **It states the limit of the whole exercise.** Encrypted DNS hides which names you look up. It does not hide which
  servers you visit afterwards. RFC 9849 says so itself.

## How it was checked

Every statement was gathered twice: once while compiling it and once in a separate adversarial pass whose explicit
brief was to refute the first version. Both passes worked exclusively from primary sources, meaning the official pages,
privacy policies and repositories of the services, public registers, and the RFCs at the RFC Editor.

The commands on the verification page are not theory. They were executed, and the documented outputs are the observed
ones. Where a measurement contradicted a provider's announcement, the contradiction appears on the page: at
UncensoredDNS the QUIC handshake succeeds, but a real DoQ query went unanswered in our test.

Where a statement could not be evidenced, it does not appear on the site.

## Check it yourself

```console
$ python3 build.py            # generates all six pages and the sitemap
$ python3 check.py            # 270 checks: structure, content, consistency
$ python3 check.py --links    # additionally: each of the 96 source URLs for HTTP 200
$ python3 -m http.server 8000
```

`check.py` verifies, among other things: HTML well-formedness, exactly one `h1` per page, headings without a hierarchy
jump, valid JSON-LD without duplicate `@id`, self-referential `canonical`, reciprocal `hreflang`, snippet lengths for
`title` and `description` and their uniqueness across pages, no em or en dashes, no resources from third-party servers,
no executable script, parity of every IP address and RFC number between the language versions, every CSS class used is
styled and none is dead, the sitemap against the files actually generated, the IndexNow key file, every cited RFC
present in the source list and vice versa, and the overview table against the individual provider cards.

The same checks run on every push through GitHub Actions. The run also fails if the committed HTML does not match
`content.py` and `build.py`, meaning somebody forgot to rebuild. The source URL test additionally runs once a month so
that rotted links get noticed.

## Layout

```
content.py     All content and evidence, bilingual, a single source of truth
build.py       Renderer; generates all six pages and the sitemap
check.py       Validation suite
index.html     generated, German         en/index.html          generated, English
pruefen/       generated, German         en/verify/             generated, English
glossar/       generated, German         en/glossary/           generated, English
sitemap.xml    generated
```

Technical data such as IP addresses and endpoints exist exactly once in `content.py` and are rendered into both
versions. The language versions therefore cannot drift apart, and `check.py` verifies that separately.

## Indexing

Both languages are meant to be indexed separately. That is ensured by:

- **A dedicated URL per language and page**, each with a self-referential `rel="canonical"`.
- **Reciprocal `hreflang` annotations** for `de`, `en` and `x-default`, all with absolute URLs. Each version names
  itself and the other, as Google requires.
- **`sitemap.xml` with `xhtml:link` alternates** for all six URLs.
- **No language-based redirect on `/`.** Netlify could redirect on a `Language` condition, but per Google's own
  documentation Googlebot sends no `Accept-Language` header. Such a rule would be more likely to destroy the separate
  indexing than to help it. Language selection happens through visible links.
- **JSON-LD** per page type: `WebPage` and `BreadcrumbList` everywhere, plus `ItemList` and `FAQPage` on the provider
  page, `HowTo` on the verification page and `DefinedTermSet` in the glossary.

Deliberately absent: `meta name="keywords"`, because Google states explicitly that it has "no effect on indexing and
ranking at all". There are no `twitter:` cards, because the official documentation for them is currently unreachable
and unverified syntax has no place here. `FAQPage` stays in the markup even though Google switched off FAQ rich results
on 7 May 2026: the type remains valid and is read by other consumers.

## Accessibility

The site quotes verbatim throughout, and those quotations are often in the other language. Without annotation a screen
reader pronounces them wrongly. `build.py` therefore marks every quoted span whose language differs from the page
language with a `lang` attribute (WCAG 2.2, success criterion 3.1.2). Ambiguous cases are left untouched rather than
annotated incorrectly.

Alongside that: headings without a hierarchy jump, `scope` and `caption` in the overview table, the horizontally
scrollable table reachable by keyboard, a visible focus ring, and smooth scrolling only under
`prefers-reduced-motion: no-preference`.

## Technical notes

Six static HTML files, no build step on the server, no framework, **no JavaScript**. A page about DNS privacy that
itself pulls scripts from third-party servers would be an irony I would rather avoid. The Content Security Policy in
`netlify.toml` makes that binding: `script-src 'none'`. The only `<script>` block per page is a JSON-LD data block,
which the browser never executes.

## Contributing

Please report errors as an issue, ideally with the primary source that contradicts the page. A correction with
evidence is more welcome than praise without.

## Disclaimer

This site is a technical description, not legal advice. Operators change addresses, policies and filtering rules; in
case of doubt the linked primary source applies, not this page.

## Licence

MIT, see [LICENSE](LICENSE).
