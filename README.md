# dns.kaipfstr.de

**Eine zweisprachige Übersicht sicherer öffentlicher DNS-Resolver und der Wege, einen eigenen zu betreiben.
Jede Angabe ist am 6. September 2026 an der Primärquelle geprüft worden.**

Live unter [dns.kaipfstr.de](https://dns.kaipfstr.de/) (Deutsch) und
[dns.kaipfstr.de/en/](https://dns.kaipfstr.de/en/) (Englisch).

## Warum es diese Seite gibt

Listen mit „den besten DNS-Servern“ gibt es viele. Die meisten haben zwei Probleme: Sie sind veraltet, und sie
nennen nur Vorteile.

Beim Zusammentragen dieser Seite kamen unter anderem folgende Punkte heraus, die in gängigen Empfehlungslisten
weiterhin falsch stehen:

- **dns0.eu existiert nicht mehr.** Der Dienst wurde im Oktober 2025 eingestellt, die Domain zeigt eine Parkseite.
  Er wird trotzdem noch empfohlen.
- **`dns.digitalcourage.de` ist dauerhaft abgeschaltet.** Aktiv ist ausschließlich `dns3.digitalcourage.de`, und
  dieser Server bietet kein DoH.
- **Mullvad schaltet seinen öffentlichen verschlüsselten DNS-Dienst am 2. November 2026 ab** und unterstützt
  stattdessen Quad9. Angekündigt am 3. September 2026.
- **DNS4EU ist kein von der EU betriebener Resolver.** Die EU-Kofinanzierung lief 2023 bis 2025. Heute ist es ein
  kostenloses Produkt der tschechischen Firma Whalebone, das Abfragedaten bis zu sechs Monate speichert.
- **Betreiber von DNS.SB ist die xTom GmbH in Düsseldorf.** Die vielzitierte Firmierung „Xing Tech“ ließ sich in
  keiner Primärquelle belegen.
- **Digitale Gesellschaft, Artikel10 und Applied Privacy bieten kein Klartext-DNS auf Port 53.** Wer ihre
  IP-Adressen in den Router einträgt, bekommt gar keine Auflösung.

## Was die Seite anders macht

- **Sie nennt zu jedem Dienst, was dagegen spricht.** Auch bei Quad9, das wegen eines französischen Urteils
  weltweit sperrt, und auch dort, wo eine No-Log-Zusage schlicht unauditiert ist. Das gilt für alle.
- **Sie zitiert wörtlich.** Logging-Zusagen stehen im Originalwortlaut da, nicht als wohlwollende Paraphrase.
- **Sie trennt Zusage von Messung.** Wo eine Eigenschaft nur gemessen und nicht zugesichert ist, steht das dabei.
- **Sie benennt die Grenze der ganzen Übung.** Verschlüsseltes DNS verbirgt, welche Namen man nachschlägt. Es
  verbirgt nicht, welche Server man danach besucht. RFC 9849 sagt das selbst.

## Prüfverfahren

Jede Angabe wurde zweimal erhoben: einmal beim Zusammentragen und einmal in einer getrennten Gegenprüfung, deren
Auftrag ausdrücklich lautete, die erste Fassung zu widerlegen. Beide Durchgänge arbeiteten ausschließlich mit
Primärquellen, also den offiziellen Seiten, Datenschutzerklärungen und Repositories der Dienste, öffentlichen
Registern und den RFCs beim RFC Editor.

Alle 60 externen Quell-URLs wurden zuletzt automatisiert auf HTTP 200 geprüft. Wo eine Angabe nicht belegbar war,
steht sie nicht auf der Seite.

## Aufbau

```
content.py     Sämtliche Inhalte und Belege, zweisprachig, eine einzige Datenquelle
build.py       Renderer, erzeugt beide Sprachfassungen und die Sitemap
index.html     erzeugt, Deutsch
en/index.html  erzeugt, Englisch
sitemap.xml    erzeugt
```

Technische Angaben wie IP-Adressen und Endpunkte stehen genau einmal in `content.py` und werden in beide Fassungen
gerendert. Die Sprachfassungen können dadurch nicht auseinanderlaufen.

```console
$ python3 build.py
$ python3 -m http.server 8000
```

## Indexierung

Beide Sprachen sollen getrennt indexiert werden. Dafür sorgen:

- **Eigene URL je Sprache** und ein selbstreferenzierendes `rel="canonical"` auf jeder.
- **Reziproke `hreflang`-Angaben** für `de`, `en` und `x-default`, jeweils mit absoluten URLs. Jede Fassung nennt
  sich selbst und die andere, wie es Google verlangt.
- **`sitemap.xml` mit `xhtml:link`-Alternates** für beide URLs.
- **Keine sprachabhängige Weiterleitung auf `/`.** Netlify könnte per `Language`-Bedingung umleiten, doch der
  Googlebot sendet nach Googles eigener Doku keinen `Accept-Language`-Header. Eine solche Regel würde die getrennte
  Indexierung eher zerstören als helfen. Die Sprachwahl passiert deshalb über sichtbare Links.
- **`robots.txt` mit `Sitemap`-Direktive**, für beide Sprachen identisch.
- **JSON-LD** mit `WebSite`, `Person`, `WebPage`, `BreadcrumbList`, `ItemList` und `FAQPage`.

## Zugänglichkeit

Die Seite zitiert durchgehend wörtlich, und diese Zitate stehen oft in der jeweils anderen Sprache. Ohne Auszeichnung
liest ein Screenreader sie mit falscher Aussprache vor. `build.py` zeichnet deshalb jede Zitatspanne, deren Sprache von
der Seitensprache abweicht, mit einem `lang`-Attribut aus (WCAG 2.2, Erfolgskriterium 3.1.2). Uneindeutige Fälle bleiben
unberührt, statt falsch ausgezeichnet zu werden.

Dazu kommen: Überschriftenhierarchie ohne Sprung, `scope` und `caption` in der Übersichtstabelle, die horizontal
scrollbare Tabelle per Tastatur erreichbar, sichtbarer Fokusrahmen, und sanftes Scrollen nur unter
`prefers-reduced-motion: no-preference`.

Bewusst nicht enthalten: `meta name="keywords"`, weil Google ausdrücklich sagt, dass es „no effect on indexing and
ranking at all“ hat. `twitter:`-Karten fehlen, weil die offizielle Dokumentation dazu derzeit nicht abrufbar ist
und ungeprüfte Syntax hier nichts zu suchen hat. `FAQPage` bleibt im Markup, obwohl Google die FAQ-Rich-Results zum
7. Mai 2026 abgeschaltet hat: Der Typ ist weiterhin gültig und wird von anderen Auswertern gelesen.

Nach dem ersten Deployment noch zu erledigen: Property in der Google Search Console und in den Bing Webmaster Tools
anlegen, `sitemap.xml` einreichen, beide URLs per URL-Prüfung zur Indexierung anmelden. Für IndexNow liegt die
Schlüsseldatei bereits im Wurzelverzeichnis.

## Technik

Zwei statische HTML-Dateien, kein Build-Schritt auf dem Server, kein Framework, **kein JavaScript**. Eine Seite über
DNS-Privatsphäre, die selbst Skripte von fremden Servern nachlädt, wäre eine Pointe, auf die ich verzichte. Die
Content-Security-Policy in `netlify.toml` schreibt das fest: `script-src 'none'`. Der einzige `<script>`-Block je
Seite ist ein JSON-LD-Datenblock, der vom Browser nie ausgeführt wird.

## Mitarbeit

Fehler bitte als Issue melden, am liebsten mit der Primärquelle, die dagegenspricht. Eine Korrektur mit Beleg ist
willkommener als ein Lob ohne.

## Haftungsausschluss

Diese Seite ist eine technische Darstellung und keine Rechtsberatung. Die Angaben geben den Stand vom
6. September 2026 wieder. Betreiber ändern Adressen, Richtlinien und Filterregeln; im Zweifel gilt die verlinkte
Primärquelle, nicht diese Seite.

## Lizenz

MIT, siehe [LICENSE](LICENSE).
