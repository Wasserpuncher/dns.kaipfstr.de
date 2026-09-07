# dns.kaipfstr.de

*[English version](README.en.md)*

**Zwölf geprüfte öffentliche DNS-Resolver, sechs Wege zum Selbsthosten, fünfzehn Befehle zum Nachmessen und ein
Glossar mit dreißig Begriffen. Zweisprachig, jede Angabe an der Primärquelle belegt.**

Live unter [dns.kaipfstr.de](https://dns.kaipfstr.de/) und [dns.kaipfstr.de/en/](https://dns.kaipfstr.de/en/).

| Seite | Deutsch | Englisch |
| --- | --- | --- |
| Anbieter | [`/`](https://dns.kaipfstr.de/) | [`/en/`](https://dns.kaipfstr.de/en/) |
| Selbst prüfen | [`/pruefen/`](https://dns.kaipfstr.de/pruefen/) | [`/en/verify/`](https://dns.kaipfstr.de/en/verify/) |
| Glossar | [`/glossar/`](https://dns.kaipfstr.de/glossar/) | [`/en/glossary/`](https://dns.kaipfstr.de/en/glossary/) |

## Warum es diese Seite gibt

Listen mit „den besten DNS-Servern“ gibt es viele. Die meisten haben zwei Probleme: Sie sind veraltet, und sie nennen
nur Vorteile.

Beim Zusammentragen kamen unter anderem diese Punkte heraus, die in gängigen Empfehlungslisten weiterhin falsch stehen:

- **dns0.eu existiert nicht mehr.** Eingestellt im Oktober 2025, die Domain zeigt eine Parkseite.
- **AhaDNS antwortet nirgends mehr.** Von zehn dokumentierten Standorten existieren acht nicht einmal mehr als
  Namenseintrag, die übrigen zwei nehmen keine Verbindung an. Die Website nennt die Adressen unverändert weiter.
- **`dns.digitalcourage.de` ist dauerhaft abgeschaltet.** Aktiv ist nur `dns3.digitalcourage.de`, und der bietet kein DoH.
- **Mullvad schaltet den öffentlichen verschlüsselten DNS-Dienst am 2. November 2026 ab.**
- **DNS4EU ist kein von der EU betriebener Resolver.** Die EU-Kofinanzierung lief 2023 bis 2025. Heute ein kostenloses
  Produkt der tschechischen Firma Whalebone, das Abfragedaten bis zu sechs Monate speichert.
- **Betreiber von DNS.SB ist die xTom GmbH in Düsseldorf**, nicht die vielzitierte „Xing Tech“.
- **Digitale Gesellschaft, Artikel10, Applied Privacy und LibreDNS bieten kein Klartext-DNS auf Port 53.** Wer ihre
  IP-Adressen in den Router einträgt, bekommt gar keine Auflösung.
- **LibreDNS validiert kein DNSSEC.** Dreifach belegt: eigene Doku, veröffentlichte Konfiguration, eigene Messung.

## Was die Seite anders macht

- **Sie nennt zu jedem Dienst, was dagegen spricht.** Auch bei Quad9, das wegen eines französischen Urteils weltweit
  sperrt, und auch dort, wo eine No-Log-Zusage schlicht unauditiert ist. Das gilt für alle.
- **Sie zitiert wörtlich.** Logging-Zusagen stehen im Originalwortlaut da, nicht als wohlwollende Paraphrase.
- **Sie trennt Zusage von Messung.** Die Übersichtstabelle unterscheidet „DNSSEC: ja“ von „nur gemessen“.
- **Sie zeigt, was sie nicht aufgenommen hat, und warum.** CIRA Canadian Shield wäre fachlich vorbildlich, verlangt in
  den Nutzungsbedingungen aber die Zusicherung, in Kanada zu wohnen.
- **Sie macht sich überprüfbar.** Die Seite „Selbst prüfen“ enthält fünfzehn Befehle mit der tatsächlich beobachteten
  Ausgabe. Wer die Empfehlungen nicht glauben will, misst nach.
- **Sie benennt die Grenze der ganzen Übung.** Verschlüsseltes DNS verbirgt, welche Namen man nachschlägt. Es verbirgt
  nicht, welche Server man danach besucht. RFC 9849 sagt das selbst.

## Prüfverfahren

Jede Angabe wurde zweimal erhoben: einmal beim Zusammentragen und einmal in einer getrennten Gegenprüfung, deren
Auftrag ausdrücklich lautete, die erste Fassung zu widerlegen. Beide Durchgänge arbeiteten ausschließlich mit
Primärquellen, also den offiziellen Seiten, Datenschutzerklärungen und Repositories der Dienste, öffentlichen Registern
und den RFCs beim RFC Editor.

Die Befehle auf der Prüfseite sind keine Theorie. Sie wurden ausgeführt, und die dokumentierten Ausgaben sind die
beobachteten. Wo eine Messung der Ankündigung eines Anbieters widersprach, steht der Widerspruch auf der Seite: Bei
UncensoredDNS gelingt der QUIC-Handschlag, eine echte DoQ-Abfrage blieb im Test aber unbeantwortet.

Wo eine Angabe nicht belegbar war, steht sie nicht auf der Seite.

## Selbst prüfen

```console
$ python3 build.py            # erzeugt alle sechs Seiten und die Sitemap
$ python3 check.py            # 270 Prüfungen: Struktur, Inhalt, Konsistenz
$ python3 check.py --links    # zusätzlich: jede der 96 Quell-URLs auf HTTP 200
$ python3 -m http.server 8000
```

`check.py` prüft unter anderem: HTML-Wohlgeformtheit, genau eine `h1` je Seite, Überschriften ohne Hierarchiesprung,
gültiges JSON-LD ohne doppelte `@id`, selbstreferenzierendes `canonical`, reziprokes `hreflang`, Snippet-Längen von
`title` und `description`, Eindeutigkeit beider über alle Seiten, keine Gedankenstriche, keine Ressourcen von fremden
Servern, kein ausführbares Skript, Gleichstand aller IP-Adressen und RFC-Nummern zwischen den Sprachfassungen, jede
benutzte CSS-Klasse gestaltet und keine tote, Sitemap gegen die tatsächlich erzeugten Dateien, IndexNow-Schlüsseldatei,
jeder zitierte RFC im Quellenverzeichnis und umgekehrt, und die Übersichtstabelle gegen die einzelnen Anbieterkarten.

Dieselben Prüfungen laufen bei jedem Push über GitHub Actions. Der Lauf schlägt auch fehl, wenn das eingecheckte HTML
nicht zu `content.py` und `build.py` passt, jemand also vergessen hat, neu zu bauen. Der Quell-URL-Test läuft zusätzlich
einmal im Monat, damit verrottete Links auffallen.

## Aufbau

```
content.py     Sämtliche Inhalte und Belege, zweisprachig, eine einzige Datenquelle
build.py       Renderer, erzeugt alle sechs Seiten und die Sitemap
check.py       Prüfsuite
index.html     erzeugt, Deutsch          en/index.html          erzeugt, Englisch
pruefen/       erzeugt, Deutsch          en/verify/             erzeugt, Englisch
glossar/       erzeugt, Deutsch          en/glossary/           erzeugt, Englisch
sitemap.xml    erzeugt
```

Technische Angaben wie IP-Adressen und Endpunkte stehen genau einmal in `content.py` und werden in beide Fassungen
gerendert. Die Sprachfassungen können dadurch nicht auseinanderlaufen, und `check.py` prüft das zusätzlich nach.

## Indexierung

Beide Sprachen sollen getrennt indexiert werden. Dafür sorgen:

- **Eigene URL je Sprache und Seite**, mit selbstreferenzierendem `rel="canonical"` auf jeder.
- **Reziproke `hreflang`-Angaben** für `de`, `en` und `x-default`, jeweils mit absoluten URLs. Jede Fassung nennt sich
  selbst und die andere, wie es Google verlangt.
- **`sitemap.xml` mit `xhtml:link`-Alternates** für alle sechs URLs.
- **Keine sprachabhängige Weiterleitung auf `/`.** Netlify könnte per `Language`-Bedingung umleiten, doch der Googlebot
  sendet nach Googles eigener Doku keinen `Accept-Language`-Header. Eine solche Regel würde die getrennte Indexierung
  eher zerstören als helfen. Die Sprachwahl passiert über sichtbare Links.
- **JSON-LD** je Seitentyp: `WebPage` und `BreadcrumbList` überall, dazu `ItemList` und `FAQPage` auf der Anbieterseite,
  `HowTo` auf der Prüfseite und `DefinedTermSet` im Glossar.

Bewusst nicht enthalten: `meta name="keywords"`, weil Google ausdrücklich sagt, dass es „no effect on indexing and
ranking at all“ hat. `twitter:`-Karten fehlen, weil die offizielle Dokumentation dazu derzeit nicht abrufbar ist und
ungeprüfte Syntax hier nichts zu suchen hat. `FAQPage` bleibt im Markup, obwohl Google die FAQ-Rich-Results zum
7. Mai 2026 abgeschaltet hat: Der Typ ist weiterhin gültig und wird von anderen Auswertern gelesen.

## Zugänglichkeit

Die Seite zitiert durchgehend wörtlich, und diese Zitate stehen oft in der jeweils anderen Sprache. Ohne Auszeichnung
liest ein Screenreader sie mit falscher Aussprache vor. `build.py` zeichnet deshalb jede Zitatspanne, deren Sprache von
der Seitensprache abweicht, mit einem `lang`-Attribut aus (WCAG 2.2, Erfolgskriterium 3.1.2). Uneindeutige Fälle bleiben
unberührt, statt falsch ausgezeichnet zu werden.

Dazu kommen: Überschriftenhierarchie ohne Sprung, `scope` und `caption` in der Übersichtstabelle, die horizontal
scrollbare Tabelle per Tastatur erreichbar, sichtbarer Fokusrahmen, und sanftes Scrollen nur unter
`prefers-reduced-motion: no-preference`.

## Technik

Sechs statische HTML-Dateien, kein Build-Schritt auf dem Server, kein Framework, **kein JavaScript**. Eine Seite über
DNS-Privatsphäre, die selbst Skripte von fremden Servern nachlädt, wäre eine Pointe, auf die ich verzichte. Die
Content-Security-Policy in `netlify.toml` schreibt das fest: `script-src 'none'`. Der einzige `<script>`-Block je Seite
ist ein JSON-LD-Datenblock, der vom Browser nie ausgeführt wird.

## Mitarbeit

Fehler bitte als Issue melden, am liebsten mit der Primärquelle, die dagegenspricht. Eine Korrektur mit Beleg ist
willkommener als ein Lob ohne.

## Haftungsausschluss

Diese Seite ist eine technische Darstellung und keine Rechtsberatung. Betreiber ändern Adressen, Richtlinien und
Filterregeln; im Zweifel gilt die verlinkte Primärquelle, nicht diese Seite.

## Lizenz

MIT, siehe [LICENSE](LICENSE).
