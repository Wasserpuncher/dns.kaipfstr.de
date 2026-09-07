# -*- coding: utf-8 -*-
"""
Inhalt und Belege fuer dns.kaipfstr.de / Content and evidence for dns.kaipfstr.de

Jede Tatsachenbehauptung auf der Seite stammt aus diesem Modul und traegt eine
Primaerquelle. Technische Daten (IP-Adressen, Endpunkte) stehen genau EINMAL hier
und werden in beide Sprachfassungen gerendert. Damit koennen die Fassungen nicht
auseinanderlaufen.

Every factual claim on the site originates here and carries a primary source.
Technical data (IP addresses, endpoints) exist exactly ONCE and are rendered into
both language versions, so the two cannot drift apart.

Stand aller Abrufe / All sources retrieved: 2026-09-06
"""

RETRIEVED = "2026-09-06"
MODIFIED = "2026-09-07"
DOMAIN = "https://dns.kaipfstr.de"

# ---------------------------------------------------------------------------
# Oeffentliche Resolver, am 2026-09-06 als aktiv verifiziert
# ---------------------------------------------------------------------------

PROVIDERS = [
    {
        "id": "quad9",
        "dnssec_ok": "yes",
        "unfiltered": "limited",
        "plain53": True,
        "name": "Quad9",
        "flag": "CH",
        "operator": "Quad9, Stiftung nach schweizerischem Recht, Zürich (UID CHE-435.091.407)",
        "operator_en": "Quad9, a foundation under Swiss law, Zurich (UID CHE-435.091.407)",
        "carrier": "Gemeinnützige Stiftung",
        "carrier_en": "Non-profit foundation",
        "endpoints": [
            ("Gefiltert", "Filtered",
             ["9.9.9.9", "149.112.112.112"],
             ["2620:fe::fe", "2620:fe::9"],
             "https://dns.quad9.net/dns-query", "dns.quad9.net"),
            ("Ungefiltert", "Unfiltered",
             ["9.9.9.10", "149.112.112.10"],
             ["2620:fe::10", "2620:fe::fe:10"],
             "https://dns10.quad9.net/dns-query", "dns10.quad9.net"),
            ("Gefiltert, mit EDNS Client Subnet", "Filtered, with EDNS Client Subnet",
             ["9.9.9.11", "149.112.112.11"],
             ["2620:fe::11", "2620:fe::fe:11"],
             "https://dns11.quad9.net/dns-query", "dns11.quad9.net"),
            ("Ungefiltert, mit EDNS Client Subnet", "Unfiltered, with EDNS Client Subnet",
             ["9.9.9.12", "149.112.112.12"],
             ["2620:fe::12", "2620:fe::fe:12"],
             "https://dns12.quad9.net/dns-query", "dns12.quad9.net"),
        ],
        "doq": "Ja. DNS over QUIC und DNS over HTTP/3 sind seit dem 31. März 2026 aktiv. Quad9 dazu wörtlich: „Quad9 has enabled DNS over HTTP/3 (DoH3) and DNS over QUIC (DoQ) across its global resolver network.“ DoQ läuft über den jeweiligen Diensthostnamen auf UDP-Port 853.",
        "doq_en": "Yes. DNS over QUIC and DNS over HTTP/3 have been live since 31 March 2026. Quad9 states verbatim: “Quad9 has enabled DNS over HTTP/3 (DoH3) and DNS over QUIC (DoQ) across its global resolver network.” DoQ uses the respective service hostname on UDP port 853.",
        "dnssec": "Validierend. Seit dem 15. Juni 2026 validiert Quad9 nach eigener Ankündigung auf allen Endpunkten, also auch auf den zuvor nicht validierenden Adressen.",
        "dnssec_en": "Validating. Since 15 June 2026 Quad9 validates on all endpoints according to its own announcement, including the addresses that previously did not validate.",
        "filtering": "Wählbar über die Adresse. 9.9.9.9 und 9.9.9.11 blockieren Domains, die von Partnern als Malware, Phishing oder Botnetz gemeldet werden. 9.9.9.10 und 9.9.9.12 blockieren diese nicht. Werbung und Tracker filtert Quad9 nicht.",
        "filtering_en": "Selectable by address. 9.9.9.9 and 9.9.9.11 block domains reported by partners as malware, phishing or botnet infrastructure. 9.9.9.10 and 9.9.9.12 do not. Quad9 does not filter advertising or trackers at all.",
        "logging": "Die Datenschutzerklärung (Version 1.1, veröffentlicht am 24. Juni 2026) sagt in Abschnitt 2.1 wörtlich: „Quad9 does not collect or record user IP addresses, nor does it collect or hold any proxy for or representation of user IP addresses, nor does it collect or hold any other unique identifier of individuals in lieu of IP addresses.“",
        "logging_en": "The privacy policy (version 1.1, published 24 June 2026) states verbatim in section 2.1: “Quad9 does not collect or record user IP addresses, nor does it collect or hold any proxy for or representation of user IP addresses, nor does it collect or hold any other unique identifier of individuals in lieu of IP addresses.”",
        "strengths": [
            "Gemeinnützige Stiftung nach schweizerischem Recht, kein Unternehmen mit Werbe- oder Datengeschäft.",
            "Die Datenschutzerklärung ist ausdrücklich an RFC 8932 ausgerichtet, dem IETF-Dokument für Datenschutzrichtlinien von DNS-Betreibern. Das ist eine Selbstauskunft, kein geprüftes Testat, aber es macht die Zusagen vergleichbar.",
            "Sehr großes Anycast-Netz und vollständige Protokollpalette: Do53, DoT, DoH, DoH3 und DoQ.",
            "Sowohl gefilterte als auch ungefilterte Adressen unter demselben Betreiber und derselben Datenschutzerklärung.",
        ],
        "strengths_en": [
            "A non-profit foundation under Swiss law, not a company with an advertising or data business.",
            "The privacy policy is explicitly aligned with RFC 8932, the IETF document on privacy policies for DNS operators. That is a self-declaration rather than an audited certification, but it makes the commitments comparable.",
            "Very large anycast network and a complete protocol range: Do53, DoT, DoH, DoH3 and DoQ.",
            "Filtered and unfiltered addresses from the same operator under the same privacy policy.",
        ],
        "caveats": [
            "Gerichtlich erzwungene Urheberrechtssperren wirken weltweit. Nach dem Pariser Urteil im Verfahren von Canal+ sperrt Quad9 die beanstandeten Domains für alle Nutzerinnen und Nutzer, weil der Dienst nicht nach Regionen unterscheidet. Quad9 selbst schreibt dazu: „we have to block these sites for all users, in all areas. This amounts to French law being applied globally.“",
            "Diese Sperren greifen auch auf den ungefilterten Adressen. „Ungefiltert“ bezieht sich bei Quad9 auf die Malware-Liste, nicht auf gerichtliche Anordnungen.",
            "Die Zusage, keine Client-IP-Adressen zu speichern, ist eine Selbstverpflichtung. Ein unabhängiges technisches Audit, das diese Praxis bestätigt, liegt nicht vor.",
        ],
        "caveats_en": [
            "Court-ordered copyright blocks apply worldwide. Following the Paris ruling in the Canal+ proceedings, Quad9 blocks the contested domains for all users because the service does not differentiate by region. Quad9 itself writes: “we have to block these sites for all users, in all areas. This amounts to French law being applied globally.”",
            "These blocks also apply on the unfiltered addresses. At Quad9, “unfiltered” refers to the malware list, not to court orders.",
            "The commitment not to store client IP addresses is a self-imposed obligation. No independent technical audit confirming this practice is available.",
        ],
        "sources": [
            ("https://quad9.net/service/service-addresses-and-features/", "Quad9: Service Addresses and Features", "Quad9: Service Addresses and Features"),
            ("https://quad9.net/privacy/policy/", "Quad9: Data Privacy Policy, Version 1.1, 24.06.2026", "Quad9: Data Privacy Policy, version 1.1, 24 June 2026"),
            ("https://quad9.net/news/blog/quad9-enables-dns-over-http-3-and-dns-over-quic/", "Quad9 Blog: Quad9 Enables DNS Over HTTP/3 and DNS Over QUIC, 31.03.2026", "Quad9 blog: Quad9 Enables DNS Over HTTP/3 and DNS Over QUIC, 31 March 2026"),
            ("https://quad9.net/news/press/quad9-faces-new-dns-censorship-legal-challenge-in-france-from-canal/", "Quad9: Presseerklärung zum Verfahren von Canal+ in Frankreich, 10.12.2024", "Quad9: press statement on the Canal+ proceedings in France, 10 December 2024"),
        ],
    },
    {
        "id": "dns4eu",
        "dnssec_ok": "yes",
        "unfiltered": "limited",
        "plain53": True,
        "name": "DNS4EU",
        "flag": "CZ",
        "operator": "Whalebone, s.r.o., Jezuitská 14/13, 602 00 Brno, Tschechien (IČO 05120403)",
        "operator_en": "Whalebone, s.r.o., Jezuitská 14/13, 602 00 Brno, Czechia (company ID 05120403)",
        "carrier": "Privatwirtschaftliches Unternehmen, hervorgegangen aus einem EU-kofinanzierten Projekt",
        "carrier_en": "Private company, grown out of an EU co-funded project",
        "endpoints": [
            ("Protective (Schutz vor Malware und Phishing)", "Protective (malware and phishing protection)",
             ["86.54.11.1", "86.54.11.201"],
             ["2a13:1001::86:54:11:1", "2a13:1001::86:54:11:201"],
             "https://protective.joindns4.eu/dns-query", "protective.joindns4.eu"),
            ("Protective und Kinderschutz", "Protective plus child protection",
             ["86.54.11.12", "86.54.11.212"],
             ["2a13:1001::86:54:11:12", "2a13:1001::86:54:11:212"],
             "https://child.joindns4.eu/dns-query", "child.joindns4.eu"),
            ("Protective und Werbefilter", "Protective plus ad blocking",
             ["86.54.11.13", "86.54.11.213"],
             ["2a13:1001::86:54:11:13", "2a13:1001::86:54:11:213"],
             "https://noads.joindns4.eu/dns-query", "noads.joindns4.eu"),
            ("Protective, Kinderschutz und Werbefilter", "Protective plus child protection plus ad blocking",
             ["86.54.11.11", "86.54.11.211"],
             ["2a13:1001::86:54:11:11", "2a13:1001::86:54:11:211"],
             "https://child-noads.joindns4.eu/dns-query", "child-noads.joindns4.eu"),
            ("Unfiltered (ohne Inhaltsfilter)", "Unfiltered (no content filter)",
             ["86.54.11.100", "86.54.11.200"],
             ["2a13:1001::86:54:11:100", "2a13:1001::86:54:11:200"],
             "https://unfiltered.joindns4.eu/dns-query", "unfiltered.joindns4.eu"),
        ],
        "doq": "Nicht dokumentiert. Auf den geprüften Endpunkten wurde am 6. September 2026 weder die QUIC-Kennung „doq“ noch HTTP/3 angeboten.",
        "doq_en": "Not documented. On the endpoints tested on 6 September 2026 neither the QUIC identifier “doq” nor HTTP/3 was offered.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Fünf Profile mit je eigenen Adressen. Das Kinderschutzprofil filtert laut Betreiber die Kategorien Gambling, Sexual content, Weapons, Child abuse, Drugs, Racism, Terrorism und Violence. Zusätzlich setzt DNS4EU gesetzlich angeordnete Sperren um, und diese greifen in allen Profilen.",
        "filtering_en": "Five profiles, each with its own addresses. According to the operator the child protection profile filters the categories gambling, sexual content, weapons, child abuse, drugs, racism, terrorism and violence. DNS4EU additionally implements legally mandated blocks, and those apply across all profiles.",
        "logging": "Anders als bei den übrigen Diensten dieser Liste ist DNS4EU kein No-Log-Resolver. Die DNS4EU Public Resolvers Policy nennt als erhobene Daten unter anderem die gestellte Anfrage, die Antwort, den Anfragetyp und den Zeitpunkt. Die Client-IP-Adresse wird nach Angabe des Betreibers anonymisiert, die Abfragedaten werden bis zu sechs Monate gespeichert.",
        "logging_en": "Unlike the other services in this list, DNS4EU is not a no-log resolver. The DNS4EU Public Resolvers Policy lists the data collected, including the query sent, the response, the query type and the timestamp. According to the operator the client IP address is anonymised; query data are retained for up to six months.",
        "strengths": [
            "Resolver ausschließlich innerhalb der EU. Die Policy nennt 14 rekursive Resolver in 14 EU-Mitgliedstaaten.",
            "Fünf klar getrennte Filterprofile mit eigenen Adressen, darunter ein Profil ganz ohne Inhaltsfilter.",
            "Aufsicht durch eine benannte europäische Datenschutzbehörde, das tschechische Úřad pro ochranu osobních údajů. Ein benannter Datenschutzbeauftragter ist erreichbar.",
            "Der Betreiber hat einen Transparenzbericht nach dem Digital Services Act und eine Liste der Sperranordnungen veröffentlicht.",
        ],
        "strengths_en": [
            "Resolvers located exclusively inside the EU. The policy names 14 recursive resolvers in 14 EU member states.",
            "Five clearly separated filter profiles with their own addresses, including one profile with no content filter at all.",
            "Supervision by a named European data protection authority, the Czech Úřad pro ochranu osobních údajů. A named data protection officer is reachable.",
            "A published Digital Services Act transparency report exists, as does a published list of blocking orders.",
        ],
        "caveats": [
            "Der Name legt einen Betrieb durch die EU nahe, den es so nicht gibt. Die EU-kofinanzierte Projektphase lief von 2023 bis 2025. Die offizielle Seite formuliert sie in der Vergangenheitsform und schreibt für heute: „Now fully commercialized and operated by Whalebone […] without ongoing EU operational funding.“ Wer DNS4EU heute wählt, wählt einen kostenlosen Dienst eines tschechischen Privatunternehmens mit EU-Projektherkunft, keinen von der EU betriebenen Resolver.",
            "Abfragedaten werden bis zu sechs Monate gespeichert. Das ist die längste dokumentierte Speicherfrist aller hier empfohlenen Dienste.",
            "Gesetzlich angeordnete Sperren wirken auch im Profil „Unfiltered“. Am 6. September 2026 wurden dort unter anderem rt.com und Domains von Sputnik nicht aufgelöst. „Unfiltered“ bezieht sich bei DNS4EU auf die Inhaltsfilter, nicht auf Sperranordnungen.",
            "Die Nutzungsbedingungen schließen Unternehmen und Zugangsanbieter aus. Der Dienst ist für Privatpersonen gedacht; es gilt ein Limit von 1.000 Anfragen pro Sekunde je IP-Adresse.",
        ],
        "caveats_en": [
            "The name suggests operation by the EU, which is not the case. The EU co-funded project phase ran from 2023 to 2025. The official page describes it in the past tense and says of the present: “Now fully commercialized and operated by Whalebone ... without ongoing EU operational funding.” Choosing DNS4EU today means choosing a free service run by a Czech private company with an EU project heritage, not a resolver operated by the EU.",
            "Query data are retained for up to six months. That is the longest documented retention period of any service recommended here.",
            "Legally mandated blocks also apply in the “Unfiltered” profile. On 6 September 2026 rt.com and Sputnik domains, among others, did not resolve there. At DNS4EU, “Unfiltered” refers to the content filters, not to blocking orders.",
            "The terms of use exclude enterprises and connectivity providers. The service is intended for private individuals, with a limit of 1,000 queries per second per IP address.",
        ],
        "sources": [
            ("https://www.joindns4.eu/for-public", "DNS4EU: DNS4EU for Public", "DNS4EU: DNS4EU for Public"),
            ("https://www.joindns4.eu/about", "DNS4EU: About the project", "DNS4EU: About the project"),
            ("https://joindns4.eu/legal-information-and-compliance", "DNS4EU: Legal information and compliance", "DNS4EU: Legal information and compliance"),
            ("https://hadea.ec.europa.eu/", "HaDEA, EU-Exekutivagentur zur CEF-Digital-Förderung", "HaDEA, the EU executive agency for CEF Digital funding"),
        ],
    },
    {
        "id": "dnssb",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": True,
        "name": "DNS.SB",
        "flag": "DE",
        "operator": "xTom GmbH, Kreuzstraße 60, 40210 Düsseldorf (HRB 86779, Amtsgericht Düsseldorf)",
        "operator_en": "xTom GmbH, Kreuzstraße 60, 40210 Düsseldorf, Germany (commercial register HRB 86779, Düsseldorf)",
        "carrier": "Privatwirtschaftliches Unternehmen",
        "carrier_en": "Private company",
        "endpoints": [
            ("Ungefiltert", "Unfiltered",
             ["185.222.222.222", "45.11.45.11"],
             ["2a09::", "2a11::"],
             "https://doh.dns.sb/dns-query", "dot.sb"),
        ],
        "doq": "Nicht offiziell dokumentiert.",
        "doq_en": "Not officially documented.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Keine. Der Betreiber schreibt: „No, we do not implement any content filtering or blocking. DNS.SB provides neutral, unfiltered DNS resolution.“",
        "filtering_en": "None. The operator states: “No, we do not implement any content filtering or blocking. DNS.SB provides neutral, unfiltered DNS resolution.”",
        "logging": "Die Datenschutzerklärung, wirksam seit dem 17. Januar 2026, beginnt mit: „TL;DR: We don't collect or store your DNS queries. Period.“ Im Detail nennt sie, dass weder abgefragte Domains noch IP-Adressen noch Zeitstempel in Verbindung mit Anfragen aufgezeichnet werden.",
        "logging_en": "The privacy policy, effective 17 January 2026, opens with: “TL;DR: We don't collect or store your DNS queries. Period.” In detail it states that neither queried domains nor IP addresses nor timestamps are recorded in connection with queries.",
        "strengths": [
            "Sehr kurze, unmissverständliche Datenschutzerklärung mit ausgewiesenem Wirksamkeitsdatum.",
            "Der Betreiber veröffentlicht seit 2019 jährliche Transparenzberichte über Behördenanfragen, einschließlich Anfragen von Behörden außerhalb Deutschlands.",
            "Weltweit verteiltes Netz. Der Betreiber nennt 19 Standorte.",
            "Betreiber mit deutschem Handelsregistereintrag und ladungsfähiger Anschrift, also mit greifbarer Verantwortlichkeit.",
        ],
        "strengths_en": [
            "A very short, unambiguous privacy policy with a stated effective date.",
            "The operator has published annual transparency reports on government requests since 2019, including requests from authorities outside Germany.",
            "A globally distributed network. The operator names 19 locations.",
            "An operator with a German commercial register entry and a serviceable address, so responsibility is traceable.",
        ],
        "caveats": [
            "Die weit verbreitete Angabe, hinter DNS.SB stehe eine Firma namens „Xing Tech“, ließ sich in keiner Primärquelle bestätigen. Betreiber ist die xTom GmbH.",
            "Die xTom GmbH ist ein gewinnorientiertes Hosting-Unternehmen, kein gemeinnütziger Träger. Den Dienst finanziert sie unter anderem über bepreiste Sponsorenstufen.",
            "Die No-Log-Zusage ist Selbstauskunft. Ein unabhängiges Audit gibt es nicht.",
        ],
        "caveats_en": [
            "The widely repeated claim that DNS.SB is run by a company called “Xing Tech” could not be confirmed in any primary source. The operator is xTom GmbH.",
            "This is a for-profit hosting company, not a non-profit body. The service is funded in part through priced sponsorship tiers.",
            "The no-log commitment is a self-declaration. There is no independent audit.",
        ],
        "sources": [
            ("https://dns.sb/", "DNS.SB: Startseite mit Endpunkten", "DNS.SB: home page with endpoints"),
            ("https://dns.sb/privacy/", "DNS.SB: Privacy Policy, wirksam 17.01.2026", "DNS.SB: Privacy Policy, effective 17 January 2026"),
            ("https://dns.sb/report/", "DNS.SB: Transparenzberichte seit 2019", "DNS.SB: transparency reports since 2019"),
            ("https://xtom.com/impressum/", "xTom GmbH: Impressum", "xTom GmbH: legal notice"),
        ],
    },
    {
        "id": "uncensoreddns",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": True,
        "name": "UncensoredDNS",
        "flag": "DK",
        "operator": "Thomas Steen Rasmussen, Dänemark. Privatperson, keine Rechtsform.",
        "operator_en": "Thomas Steen Rasmussen, Denmark. A private individual, no legal entity.",
        "carrier": "Privatperson, unentgeltlich betrieben",
        "carrier_en": "Private individual, operated free of charge",
        "endpoints": [
            ("Anycast-Knoten", "Anycast node",
             ["91.239.100.100"], ["2001:67c:28a4::"],
             "https://anycast.uncensoreddns.org/dns-query", "anycast.uncensoreddns.org"),
            ("Unicast-Knoten", "Unicast node",
             ["89.233.43.71"], ["2a01:3a0:53:53::"],
             "https://unicast.uncensoreddns.org/dns-query", "unicast.uncensoreddns.org"),
        ],
        "doq": "Angekündigt, im Test aber ohne Antwort. Der Betreiber schrieb am 23. Oktober 2025: „Starting today UncensoredDNS fully supports QUIC based DNS lookups.“ Die QUIC-Kennung „doq“ wird tatsächlich ausgehandelt. Eine echte DoQ-Abfrage mit kdig blieb am 7. September 2026 von einem deutschen Anschluss aus jedoch dreimal unbeantwortet, während dieselbe Abfrage gegen Quad9 und AdGuard DNS funktionierte. Das ist ein Momentbefund von einem einzigen Anschluss, kein Beweis, dass der Dienst kein DoQ kann. DoT desselben Servers arbeitete einwandfrei.",
        "doq_en": "Announced, but unanswered in our test. On 23 October 2025 the operator wrote: “Starting today UncensoredDNS fully supports QUIC based DNS lookups.” The QUIC identifier “doq” is indeed negotiated. A real DoQ query with kdig, however, went unanswered three times on 7 September 2026 from a German connection, while the same query against Quad9 and AdGuard DNS succeeded. This is a point-in-time observation from a single connection, not proof that the service cannot do DoQ. DoT on the same server worked flawlessly.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Keine. Der Dienst existiert ausdrücklich als Gegenentwurf zur Filterung. Der Betreiber schreibt: „I am strongly against using DNS as a tool to filter content on the internet.“",
        "filtering_en": "None. The service exists explicitly as a counterpoint to filtering. The operator writes: “I am strongly against using DNS as a tool to filter content on the internet.”",
        "logging": "Die FAQ sagt: „Absolutely nothing is being logged, neither about the users nor the usage of this service. I do keep graphs of the total number of queries, but no personally identifiable information is saved.“",
        "logging_en": "The FAQ states: “Absolutely nothing is being logged, neither about the users nor the usage of this service. I do keep graphs of the total number of queries, but no personally identifiable information is saved.”",
        "strengths": [
            "Der Dienst läuft seit 2009 und ist damit einer der ältesten unabhängigen offenen Resolver Europas.",
            "Vollständige Protokollpalette einschließlich DNS over QUIC und DNS over HTTP/3.",
            "Klare, unzweideutige Haltung gegen Filterung, ohne kommerzielles Interesse dahinter.",
            "Zwei getrennte Zugänge, ein Anycast- und ein Unicast-Knoten, die sich als primärer und sekundärer Server eintragen lassen.",
        ],
        "strengths_en": [
            "The service has run since 2009, making it one of the oldest independent open resolvers in Europe.",
            "A complete protocol range including DNS over QUIC and DNS over HTTP/3.",
            "A clear, unambiguous stance against filtering, with no commercial interest behind it.",
            "Two separate entry points, one anycast and one unicast node, which can be entered as primary and secondary server.",
        ],
        "caveats": [
            "Der Dienst hängt vollständig an einer einzelnen Privatperson. Es gibt keinen Verein, kein Team und keine veröffentlichte Nachfolgeregelung.",
            "Die Logging-Zusage steht in zwei Sätzen einer FAQ. Es gibt keine förmliche Datenschutzerklärung, kein Audit und keinen Transparenzbericht.",
            "Das Anycast-Netz ist klein. Die offizielle Tabelle nennt drei Knoten, zwei davon in Dänemark. Außerhalb Nordeuropas ist der Latenzvorteil entsprechend gering.",
        ],
        "caveats_en": [
            "The service depends entirely on a single private individual. There is no association, no team and no published succession plan.",
            "The logging commitment consists of two sentences in a FAQ. There is no formal privacy policy, no audit and no transparency report.",
            "The anycast network is small. The official table lists three nodes, two of them in Denmark. Outside northern Europe the latency benefit is correspondingly limited.",
        ],
        "sources": [
            ("https://blog.uncensoreddns.org/", "UncensoredDNS: Startseite und Serverliste", "UncensoredDNS: home page and server list"),
            ("https://blog.uncensoreddns.org/faq/", "UncensoredDNS: FAQ mit Logging-Aussage", "UncensoredDNS: FAQ with the logging statement"),
            ("https://blog.uncensoreddns.org/blog/43-full-doq-and-doh3-support/", "UncensoredDNS: Full DoQ and DoH3 support, 23.10.2025", "UncensoredDNS: Full DoQ and DoH3 support, 23 October 2025"),
        ],
    },
    {
        "id": "digitalcourage",
        "dnssec_ok": "measured",
        "unfiltered": "yes",
        "plain53": True,
        "name": "Digitalcourage e. V.",
        "flag": "DE",
        "operator": "Digitalcourage e. V., Marktstraße 18, 33602 Bielefeld",
        "operator_en": "Digitalcourage e. V., Marktstraße 18, 33602 Bielefeld, Germany",
        "carrier": "Gemeinnütziger eingetragener Verein",
        "carrier_en": "Registered non-profit association",
        "endpoints": [
            ("Zensurfreier Resolver", "Censorship-free resolver",
             ["5.9.164.112"], ["2a01:4f8:251:554::2"],
             None, "dns3.digitalcourage.de"),
        ],
        "doq": "Nein.",
        "doq_en": "No.",
        "dnssec": "Eine eigene Messung am 6. September 2026 zeigte DNSSEC-Validierung. Der Verein selbst sagt dazu auf der Dienstseite nichts, es gibt also keine zugesicherte Eigenschaft.",
        "dnssec_en": "A measurement on 6 September 2026 showed DNSSEC validation. The association itself makes no statement about this on the service page, so it is not a guaranteed property.",
        "filtering": "Keine. Der Dienst ist ausdrücklich ein zensurfreier Resolver und kein Werbe- oder Trackerblocker.",
        "filtering_en": "None. The service is explicitly a censorship-free resolver, not an advertising or tracker blocker.",
        "logging": "Auf der offiziellen Seite zu dns3.digitalcourage.de steht: „kein Logging, nur im Fehlerfall (ohne Client-IP)“.",
        "logging_en": "The official page for dns3.digitalcourage.de states, in German: “kein Logging, nur im Fehlerfall (ohne Client-IP)”, meaning no logging except in the event of an error, and then without the client IP.",
        "strengths": [
            "Gemeinnütziger Verein mit langer, öffentlich nachvollziehbarer Arbeit zu Grundrechten und Datenschutz.",
            "Deutscher Serverstandort und deutsche Jurisdiktion. Trägerschaft und Finanzierung sind über einen veröffentlichten Transparenzbericht nachvollziehbar.",
            "Ausdrücklich zensurfrei, ohne kommerzielles Interesse an den Anfragedaten.",
        ],
        "strengths_en": [
            "A non-profit association with a long, publicly traceable record of work on fundamental rights and data protection.",
            "German server location and German jurisdiction; sponsorship and funding are traceable through a published transparency report.",
            "Explicitly censorship-free, with no commercial interest in the query data.",
        ],
        "caveats": [
            "Die vielerorts noch genannte Adresse dns.digitalcourage.de ist dauerhaft abgeschaltet. Der Verein schreibt: „Dieser Server ist abgeschaltet. Bitte die IP aus vorhandenen Konfigurationen entfernen: 85.214.20.141 (dauerhaft abgeschaltet)“. Wer diese IP noch eingetragen hat, hat keinen funktionierenden Resolver. Aktiv ist ausschließlich dns3.digitalcourage.de.",
            "Kein DoH. Der Verein sagt dazu ausdrücklich: „Außerdem kann dieser Server nicht im Browser als DNS-Server eingestellt werden, denn das würde DNS over HTTP (DoH) erfordern, was wir ebenfalls nicht unterstützen.“ In den DoH-Einstellungen von Firefox oder Chrome ist der Dienst damit nicht nutzbar.",
            "Es gibt genau einen Server. Kein Anycast, kein zweiter Knoten, also ein einzelner Ausfallpunkt. Ein zweiter, unabhängiger Resolver als Ersatzeintrag ist sinnvoll.",
        ],
        "caveats_en": [
            "The address dns.digitalcourage.de, still cited in many places, has been permanently shut down. The association writes, in German, that the server is switched off and that the IP 85.214.20.141 should be removed from existing configurations. Anyone still using that IP has no working resolver. Only dns3.digitalcourage.de is active.",
            "No DoH. The association states explicitly that the server cannot be set as a DNS server in the browser because that would require DNS over HTTPS, which the service does not support. The service therefore cannot be used in the DoH settings of Firefox or Chrome.",
            "There is exactly one server. No anycast, no second node, so a single point of failure. Configuring a second, independent resolver as a fallback is advisable.",
        ],
        "sources": [
            ("https://digitalcourage.de/support/zensurfreier-dns-server", "Digitalcourage: Zensurfreier DNS-Server", "Digitalcourage: censorship-free DNS server"),
            ("https://digitalcourage.de/impressum", "Digitalcourage e. V.: Impressum", "Digitalcourage e. V.: legal notice"),
        ],
    },
    {
        "id": "digiges",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": False,
        "name": "Digitale Gesellschaft",
        "flag": "CH",
        "operator": "Digitale Gesellschaft, Verein nach Art. 60 ff. ZGB, Sitz Basel. Server in Zürich.",
        "operator_en": "Digitale Gesellschaft, an association under Articles 60 et seq. of the Swiss Civil Code, with its seat in Basel. Servers in Zurich.",
        "carrier": "Gemeinnütziger Verein",
        "carrier_en": "Non-profit association",
        "endpoints": [
            ("Nur verschlüsselt, kein Klartext-DNS", "Encrypted only, no plaintext DNS",
             ["185.95.218.42", "185.95.218.43"],
             ["2a05:fc84::42", "2a05:fc84::43"],
             "https://dns.digitale-gesellschaft.ch/dns-query", "dns.digitale-gesellschaft.ch"),
        ],
        "doq": "Nicht dokumentiert.",
        "doq_en": "Not documented.",
        "dnssec": "Validierend, ausdrücklich zugesichert: „DNSSEC wird validiert.“",
        "dnssec_en": "Validating, explicitly guaranteed by the operator.",
        "filtering": "Keine. Der Verein sagt: „Es findet kein Logging statt und es werden keine Sperrlisten verwendet.“ Vorbehalten bleibt eine zeitweise Sperre bei Missbrauch.",
        "filtering_en": "None. The association states, in German, that no logging takes place and no block lists are used. It reserves the right to temporary blocks in cases of abuse.",
        "logging": "Offizielle Aussage: „Es findet kein Logging statt und es werden keine Sperrlisten verwendet. DNSSEC wird validiert.“",
        "logging_en": "Official statement, in German: no logging takes place, no block lists are used, and DNSSEC is validated.",
        "strengths": [
            "Gemeinnütziger Verein mit veröffentlichten Statuten und offengelegter Serverkonfiguration in einem öffentlichen Repository.",
            "Schweizer Serverstandort und Schweizer Recht, außerhalb der EU-Jurisdiktion.",
            "Klare, knappe Zusage ohne Marketingaufwand: kein Logging, keine Sperrlisten, DNSSEC-Validierung.",
            "Der Betrieb kostet laut FAQ 1.000 Franken im Jahr. Die Finanzierung ist damit nachvollziehbar unabhängig.",
        ],
        "strengths_en": [
            "A non-profit association with published statutes and a server configuration disclosed in a public repository.",
            "Swiss server location and Swiss law, outside EU jurisdiction.",
            "A clear, concise commitment with no marketing gloss: no logging, no block lists, DNSSEC validation.",
            "Very low running costs, 1,000 Swiss francs a year according to the FAQ, which makes independent funding plausible.",
        ],
        "caveats": [
            "Kein Klartext-DNS auf Port 53. Der Verein betreibt es bewusst nicht. Router, Smart-TVs und viele IoT-Geräte, die nur klassisches DNS können, lassen sich damit nicht versorgen.",
            "Die genannten IP-Adressen sind die Adressen der verschlüsselten Endpunkte. Sie gehören in ein DoT- oder DoH-Feld, nicht in ein gewöhnliches DNS-Server-Feld.",
            "Der Betreiber behält sich vor, bei Missbrauch einzelne Client-IP-Adressen und einzelne Domainnamen zeitweise zu sperren. „Keine Sperrlisten“ heißt also nicht „unter allen Umständen unverändert“.",
        ],
        "caveats_en": [
            "No plaintext DNS on port 53. The association deliberately does not run it. Routers, smart TVs and many IoT devices that only speak classic DNS cannot be served this way.",
            "The IP addresses given are the addresses of the encrypted endpoints. They belong in a DoT or DoH field, not in an ordinary DNS server field.",
            "The operator reserves the right to temporarily block individual client IP addresses and individual domain names in cases of abuse. “No block lists” therefore does not mean “unmodified under all circumstances”.",
        ],
        "sources": [
            ("https://www.digitale-gesellschaft.ch/dns/", "Digitale Gesellschaft: Öffentlicher DNS-Resolver", "Digitale Gesellschaft: public DNS resolver"),
            ("https://github.com/DigitaleGesellschaft/DNS-Resolver", "Digitale Gesellschaft: Konfiguration des Resolvers", "Digitale Gesellschaft: resolver configuration"),
        ],
    },
    {
        "id": "artikel10",
        "dnssec_ok": "measured",
        "unfiltered": "yes",
        "plain53": False,
        "name": "Artikel10 e. V.",
        "flag": "DE",
        "operator": "Artikel10 e. V., Hamburg (VR 24066, Amtsgericht Hamburg). Infrastruktur bei Individual Network Berlin e. V.",
        "operator_en": "Artikel10 e. V., Hamburg, Germany (register VR 24066, Hamburg local court). Infrastructure hosted at Individual Network Berlin e. V.",
        "carrier": "Eingetragener Verein",
        "carrier_en": "Registered association",
        "endpoints": [
            ("Nur verschlüsselt, kein Klartext-DNS", "Encrypted only, no plaintext DNS",
             ["217.197.91.153"], ["2001:67c:1401:2120::1"],
             "https://dns.artikel10.org/dns-query", "dns.artikel10.org"),
        ],
        "doq": "Nicht dokumentiert.",
        "doq_en": "Not documented.",
        "dnssec": "Eine eigene Messung am 6. September 2026 zeigte DNSSEC-Validierung. Eine ausdrückliche Zusage des Betreibers dazu gibt es nicht.",
        "dnssec_en": "A measurement on 6 September 2026 showed DNSSEC validation. There is no explicit commitment from the operator.",
        "filtering": "Der Betreiber äußert sich nicht ausdrücklich dazu. Eine eigene Messung am 6. September 2026 zeigte keine Filterung.",
        "filtering_en": "The operator makes no explicit statement. A measurement on 6 September 2026 showed no filtering.",
        "logging": "Die Dienstseite sagt: „Der Server speichert keine Informationen über einzelne DNS-Anfragen.“",
        "logging_en": "The service page states, in German, that the server stores no information about individual DNS queries.",
        "strengths": [
            "Eingetragener Verein mit Satzung und Registereintrag, der sich seit Jahren dem Schutz des Fernmeldegeheimnisses widmet und daneben Tor-Infrastruktur betreibt.",
            "Deutscher Standort und deutsche Jurisdiktion.",
            "Knappe, klare Logging-Aussage ohne Einschränkungen im Kleingedruckten.",
        ],
        "strengths_en": [
            "A registered association with statutes and a register entry, dedicated for years to protecting the privacy of correspondence and also operating Tor infrastructure.",
            "German location and German jurisdiction.",
            "A concise, clear logging statement without qualifications in the small print.",
        ],
        "caveats": [
            "Kein Klartext-DNS auf Port 53. Die genannten Adressen antworten ausschließlich über DoT auf Port 853 und DoH auf Port 443. Wer sie als gewöhnliche DNS-Server einträgt, bekommt keine Auflösung.",
            "Der Verein kommuniziert öffentlich seit dem 27. November 2023 nicht mehr. Der Dienst läuft nachweislich, aber es gibt keine aktuelle Kommunikation über seinen Zustand.",
            "Der Verein dokumentiert den Dienst knapp: keine förmliche Datenschutzerklärung für den Resolver, kein Audit, kein Transparenzbericht.",
        ],
        "caveats_en": [
            "No plaintext DNS on port 53. The addresses respond only via DoT on port 853 and DoH on port 443. Entering them as ordinary DNS servers yields no resolution at all.",
            "The association has not communicated publicly since 27 November 2023. The service demonstrably runs, but there is no current communication about its state.",
            "The service is documented very briefly. There is no formal privacy policy for the resolver, no audit and no transparency report.",
        ],
        "sources": [
            ("https://dns.artikel10.org/", "Artikel10: DNS-Resolver", "Artikel10: DNS resolver"),
            ("https://artikel10.org/", "Artikel10 e. V.: Website und Impressum", "Artikel10 e. V.: website and legal notice"),
        ],
    },
    {
        "id": "dnsforge",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": True,
        "name": "dnsforge.de",
        "flag": "DE",
        "operator": "adminForge, betrieben von Stefan Giebel, Köln. Server in Deutschland.",
        "operator_en": "adminForge, run by Stefan Giebel, Cologne, Germany. Servers in Germany.",
        "carrier": "Privates Projekt, spendenfinanziert",
        "carrier_en": "Private project, donation funded",
        "endpoints": [
            ("Normal, mit Werbe- und Trackerfilter", "Normal, with ad and tracker filtering",
             ["49.12.67.122", "91.99.154.175", "176.9.93.198", "176.9.1.117"],
             ["2a01:4f8:c013:29d::122", "2a01:4f8:c010:8c35::175", "2a01:4f8:151:34aa::198", "2a01:4f8:141:316d::117"],
             "https://dnsforge.de/dns-query", "dnsforge.de"),
            ("Clean, zusätzlich Erwachsenen- und Glücksspielinhalte", "Clean, additionally filters adult and gambling content",
             ["49.12.223.2", "49.12.43.208"],
             ["2a01:4f8:c17:4fbc::2", "2a01:4f8:c012:ed89::208"],
             "https://clean.dnsforge.de/dns-query", "clean.dnsforge.de"),
            ("Hard, strengster Filter", "Hard, strictest filter",
             ["49.12.222.213", "88.198.122.154"],
             ["2a01:4f8:c17:2c61::213", "2a01:4f8:c013:5ec0::154"],
             "https://hard.dnsforge.de/dns-query", "hard.dnsforge.de"),
            ("Blank, ohne jeden Filter", "Blank, without any filter",
             ["138.199.149.249", "78.47.71.194"],
             ["2a01:4f8:c17:7aa5::249", "2a01:4f8:c013:aae9::194"],
             "https://blank.dnsforge.de/dns-query", "blank.dnsforge.de"),
        ],
        "doq": "Der Betreiber listet für alle vier Varianten DoQ-Endpunkte. Eigene Messungen dazu liegen nicht vor.",
        "doq_en": "The operator lists DoQ endpoints for all four variants. No independent measurement of these is available.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Vier abgestufte Varianten mit je eigenen Adressen, von „Normal“ mit Werbe- und Trackerfilter bis „Blank“ ganz ohne Filter. Geblockte Namen werden mit 0.0.0.0 beziehungsweise :: beantwortet, nicht mit NXDOMAIN.",
        "filtering_en": "Four graded variants, each with its own addresses, from “Normal” with ad and tracker filtering to “Blank” with no filtering at all. Blocked names are answered with 0.0.0.0 or ::, not with NXDOMAIN.",
        "logging": "Die FAQ sagt: „Nein. dnsforge.de protokolliert keine DNS-Anfragen und arbeitet vollständig ohne Logging.“ Der Datenschutzhinweis von adminForge enthält dazu einen eigenen Abschnitt.",
        "logging_en": "The FAQ states, in German, that dnsforge.de logs no DNS queries and operates entirely without logging. The adminForge privacy notice contains a dedicated section on this.",
        "strengths": [
            "Vier klar getrennte Filterstufen, darunter eine völlig ungefilterte. Die Wahl bleibt bei der Nutzerin und nicht beim Betreiber.",
            "Die verwendeten Blocklisten werden offen benannt, nicht bloß behauptet.",
            "Server ausschließlich in Deutschland, Betreiber mit Impressum und ladungsfähiger Anschrift.",
            "Die Blocklisten-Zählerstände werden tagesaktuell auf der Startseite veröffentlicht.",
        ],
        "strengths_en": [
            "Four clearly separated filter levels, including a completely unfiltered one. The choice stays with the user rather than the operator.",
            "The block lists used are named openly rather than merely asserted.",
            "Servers exclusively in Germany, operator with a legal notice and a serviceable address.",
            "Block list counts are published on the home page and updated daily.",
        ],
        "caveats": [
            "Träger ist kein Verein und keine Gesellschaft, sondern ein privates Projekt. Für den Einsatz in Organisationen mit Verfügbarkeitsanforderungen ist das ein ernst zu nehmender Punkt.",
            "Der Dienst finanziert sich über Spenden. Die Spendenseite weist die Monatsziele aus, die Finanzierung ist damit sichtbar, aber nicht institutionell abgesichert.",
            "Die No-Log-Zusage ist Selbstauskunft ohne unabhängiges Audit.",
        ],
        "caveats_en": [
            "The service is run neither by an association nor by a company but as a private project. For use in organisations with availability requirements that is a serious consideration.",
            "The service is funded by donations. The donation page shows the monthly targets, so funding is visible but not institutionally secured.",
            "The no-log commitment is a self-declaration without an independent audit.",
        ],
        "sources": [
            ("https://dnsforge.de/", "dnsforge.de: Endpunkte, Varianten und FAQ", "dnsforge.de: endpoints, variants and FAQ"),
            ("https://adminforge.de/datenschutz/", "adminForge: Datenschutzhinweis", "adminForge: privacy notice"),
            ("https://adminforge.de/impressum/", "adminForge: Impressum", "adminForge: legal notice"),
        ],
    },
    {
        "id": "ffmuc",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": True,
        "name": "Freifunk München",
        "flag": "DE",
        "operator": "Freie Netze München e. V., Parkstraße 28, 82131 Gauting (VR 206402, Amtsgericht München). Server in München und Wien.",
        "operator_en": "Freie Netze München e. V., Parkstraße 28, 82131 Gauting, Germany (register VR 206402, Munich local court). Servers in Munich and Vienna.",
        "carrier": "Eingetragener Verein",
        "carrier_en": "Registered association",
        "endpoints": [
            ("Ungefiltert", "Unfiltered",
             ["5.1.66.255", "185.150.99.255"],
             ["2001:678:e68:f000::", "2001:678:ed0:f000::"],
             "https://doh.ffmuc.net/dns-query", "dot.ffmuc.net"),
        ],
        "doq": "Der Betreiber nennt den Hostnamen doq.ffmuc.net. DoH über HTTP/3 wird angeboten.",
        "doq_en": "The operator names the hostname doq.ffmuc.net. DoH over HTTP/3 is offered.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Keine. Die Datenschutzrichtlinie des Dienstes sagt: „The resolver operates as a general-purpose recursive DNS service and does not perform content filtering or censorship by default.“",
        "filtering_en": "None. The service privacy policy states: “The resolver operates as a general-purpose recursive DNS service and does not perform content filtering or censorship by default.”",
        "logging": "Die Datenschutzrichtlinie sagt: „The service does not retain identifiable per-user DNS query logs.“ Ausdrücklich genannt werden temporäre Zähler je IP-Adresse für die Begrenzung der Anfragerate.",
        "logging_en": "The privacy policy states: “The service does not retain identifiable per-user DNS query logs.” Temporary per-IP counters for rate limiting are explicitly mentioned.",
        "strengths": [
            "Eingetragener Verein aus der Freifunk-Bewegung mit langjähriger Praxis im Betrieb offener Netze.",
            "Server ausschließlich in der EU, konkret in München und Wien.",
            "Der Betreiber benennt die Ausnahme selbst: temporäre Zähler je IP für Ratenbegrenzung.",
            "Klartext-DNS und verschlüsselte Protokolle stehen beide zur Verfügung.",
        ],
        "strengths_en": [
            "A registered association from the Freifunk movement with long-standing practice in running open networks.",
            "Servers exclusively within the EU, specifically in Munich and Vienna.",
            "The operator names the exception itself: temporary per-IP counters for rate limiting.",
            "Both plaintext DNS and encrypted protocols are available.",
        ],
        "caveats": [
            "Der Gemeinnützigkeitsstatus ist unklar. Die Einrichtungsseite bezeichnet den Verein als gemeinnützig, während die eigene Wiki-FAQ sagt, man sei „wegen fehlender rechtlicher Voraussetzungen nicht gemeinnützig“ und könne keine Spendenquittung ausstellen. Ein Freistellungsbescheid ließ sich nicht auffinden. „e. V.“ allein bedeutet keine Gemeinnützigkeit.",
            "Zwei Standorte, beide im deutschsprachigen Raum. Außerhalb Mitteleuropas ist der Dienst entsprechend langsamer.",
        ],
        "caveats_en": [
            "The charitable tax status is unclear. The setup page describes the association as a non-profit, while its own wiki FAQ states that it is not recognised as charitable because the legal requirements are not met, and cannot issue donation receipts. No exemption notice could be found. The suffix “e. V.” alone does not imply charitable status.",
            "Two locations, both in German-speaking Europe. Outside central Europe the service is correspondingly slower.",
        ],
        "sources": [
            ("https://dns-setup.ffmuc.net/", "FFMUC: DNS-Einrichtung", "FFMUC: DNS setup"),
            ("https://ffmuc.net/dns-privacy/", "FFMUC: DNS Privacy Policy", "FFMUC: DNS Privacy Policy"),
            ("https://ffmuc.net/impressum/", "Freie Netze München e. V.: Impressum", "Freie Netze München e. V.: legal notice"),
        ],
    },
    {
        "id": "restena",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": True,
        "name": "RESTENA",
        "flag": "LU",
        "operator": "Fondation Restena, 2 place de l'Université, L-4365 Esch-sur-Alzette, Luxemburg",
        "operator_en": "Fondation Restena, 2 place de l'Université, L-4365 Esch-sur-Alzette, Luxembourg",
        "carrier": "Stiftung, nationales Forschungs- und Bildungsnetz Luxemburgs",
        "carrier_en": "Foundation, the national research and education network of Luxembourg",
        "endpoints": [
            ("Öffentlicher Resolver", "Public resolver",
             ["158.64.1.29"], ["2001:a18:1::29"],
             "https://dnspub.restena.lu/dns-query", "dnspub.restena.lu"),
        ],
        "doq": "Nicht dokumentiert.",
        "doq_en": "Not documented.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Für den öffentlichen Resolver ist keine Filterung dokumentiert. Die Dienstseite nennt als Eigenschaft die „Guaranteed neutrality, as the resolver does not deliberately modify the collected information before transmitting it“. Die separat angebotene DNS-Firewall ist laut Betreiber nur für angeschlossene Einrichtungen verfügbar.",
        "filtering_en": "No filtering is documented for the public resolver. The service page cites “Guaranteed neutrality, as the resolver does not deliberately modify the collected information before transmitting it”. The separately offered DNS firewall is, according to the operator, available only to connected institutions.",
        "logging": "Es gibt keine eigene Logging-Richtlinie für den Resolver. Die Dienstseite sagt, die für die Auflösung erhobenen Informationen seien „limited to the minimum necessary for the technical functioning of the service“. Das ist weniger konkret als bei den übrigen Diensten dieser Liste.",
        "logging_en": "There is no dedicated logging policy for the resolver. The service page says the information collected for resolution is “limited to the minimum necessary for the technical functioning of the service”. That is less specific than for the other services in this list.",
        "strengths": [
            "Träger ist eine Stiftung mit staatlichem Auftrag, das nationale Forschungs- und Bildungsnetz Luxemburgs. Das ist eine institutionelle Stabilität, die private Projekte nicht bieten können.",
            "Standort und Jurisdiktion Luxemburg, innerhalb der EU.",
            "Ausdrücklich zugesagte Neutralität der Antworten.",
        ],
        "strengths_en": [
            "The operator is a foundation with a public mandate, the national research and education network of Luxembourg. That is a degree of institutional stability that private projects cannot offer.",
            "Location and jurisdiction Luxembourg, within the EU.",
            "Explicitly guaranteed neutrality of the answers.",
        ],
        "caveats": [
            "Die Nutzungsbedingungen der Stiftung beschränken die Nutzung ihrer Ressourcen allgemein auf „the community of education, research, culture, health and administration“, während die Seite des öffentlichen Resolvers ausdrücklich die Allgemeinheit anspricht. Dieser Widerspruch ist in den Primärquellen nicht aufgelöst.",
            "Es gibt genau einen öffentlichen Resolver-Host, eine IPv4- und eine IPv6-Adresse. Kein dokumentiertes Anycast, kein Ersatzziel. Die Stiftung empfiehlt selbst, einen zweiten Server einzutragen.",
            "Die Logging-Aussage ist allgemein gehalten. Es gibt keine bezifferte Speicherfrist.",
        ],
        "caveats_en": [
            "The foundation’s general conditions limit use of its resources to “the community of education, research, culture, health and administration”, while the public resolver page explicitly addresses the general public. This contradiction is not resolved in the primary sources.",
            "There is exactly one public resolver host, one IPv4 and one IPv6 address. No documented anycast, no fallback target. The foundation itself recommends adding a second server.",
            "The logging statement is generic. No retention period is quantified.",
        ],
        "sources": [
            ("https://www.restena.lu/en/service/public-dns-resolver", "Fondation Restena: Public DNS resolver", "Fondation Restena: Public DNS resolver"),
            ("https://www.restena.lu/", "Fondation Restena: Website", "Fondation Restena: Website"),
        ],
    },
    {
        "id": "appliedprivacy",
        "dnssec_ok": "yes",
        "unfiltered": "yes",
        "plain53": False,
        "name": "Applied Privacy",
        "flag": "AT",
        "operator": "Foundation for Applied Privacy, Verein zur Förderung der digitalen Privatsphäre, ZVR 1254016365, Floragasse 7, 1040 Wien",
        "operator_en": "Foundation for Applied Privacy, an Austrian association, register number ZVR 1254016365, Floragasse 7, 1040 Vienna",
        "carrier": "Gemeinnütziger Verein",
        "carrier_en": "Non-profit association",
        "endpoints": [
            ("Nur verschlüsselt, kein Klartext-DNS", "Encrypted only, no plaintext DNS",
             ["146.255.56.98"], ["2a02:1b8:10:234::2"],
             "https://doh.applied-privacy.net/query", "dot1.applied-privacy.net"),
        ],
        "doq": "Nicht dokumentiert.",
        "doq_en": "Not documented.",
        "dnssec": "Validierend.",
        "dnssec_en": "Validating.",
        "filtering": "Keine. Der Betreiber sagt: „We do not provide DNS filter services, our resolvers provide the information they get from the authoritative DNS servers.“",
        "filtering_en": "None. The operator states: “We do not provide DNS filter services, our resolvers provide the information they get from the authoritative DNS servers.”",
        "logging": "Die Datenschutzerklärung sagt: „We do NOT log your IP address. We do NOT log your DNS query. We do NOT share query data with third parties.“",
        "logging_en": "The privacy policy states: “We do NOT log your IP address. We do NOT log your DNS query. We do NOT share query data with third parties.”",
        "strengths": [
            "Gemeinnütziger Verein mit österreichischer Vereinsregisternummer und ausdrücklichem Zweck der Förderung digitaler Privatsphäre.",
            "Sehr klare, dreifach negierte Logging-Zusage ohne Einschränkungen.",
            "DoT wird zusätzlich auf Port 443 angeboten. Das hilft in Netzen, die Port 853 sperren.",
            "Der Betreiber setzt nach eigener Angabe kein EDNS Client Subnet.",
        ],
        "strengths_en": [
            "A non-profit association with an Austrian register number and the explicit purpose of promoting digital privacy.",
            "A very clear, three-part negative logging commitment without qualifications.",
            "DoT is additionally offered on port 443. That helps on networks that block port 853.",
            "According to the operator, no EDNS Client Subnet is set.",
        ],
        "caveats": [
            "Der Betreiber stuft den Dienst selbst als experimentell ein: „This is an experimental service which is operated on a best effort basis.“ Für produktive oder geschäftskritische Nutzung ist er damit nicht gedacht.",
            "Ein einziger dokumentierter Standort, Wien, und faktisch ein einziges Serverpaar. DoH- und DoT-Endpunkt lösen auf dieselben Adressen auf. Kein Anycast, keine geografische Redundanz.",
            "Kein Klartext-DNS auf Port 53.",
        ],
        "caveats_en": [
            "The operator itself classifies the service as experimental: “This is an experimental service which is operated on a best effort basis.” It is therefore not intended for production or business-critical use.",
            "A single documented location, Vienna, and in practice a single pair of servers. The DoH and DoT endpoints resolve to the same addresses. No anycast, no geographic redundancy.",
            "No plaintext DNS on port 53.",
        ],
        "sources": [
            ("https://applied-privacy.net/services/dns/", "Foundation for Applied Privacy: DNS Privacy Services", "Foundation for Applied Privacy: DNS Privacy Services"),
            ("https://applied-privacy.net/privacy-policy/", "Foundation for Applied Privacy: Privacy Policy", "Foundation for Applied Privacy: Privacy Policy"),
        ],
    },
    {
        "id": "libredns",
        "dnssec_ok": "no",
        "unfiltered": "yes",
        "plain53": False,
        "name": "LibreDNS",
        "flag": "GR",
        "operator": "LibreOps, ein Kollektiv namentlich benannter Freiwilliger aus Griechenland. Server bei Hetzner in Nürnberg.",
        "operator_en": "LibreOps, a collective of named volunteers from Greece. Servers at Hetzner in Nuremberg, Germany.",
        "carrier": "Freiwilligenkollektiv ohne eigene Rechtsform",
        "carrier_en": "Volunteer collective without a legal entity of its own",
        "endpoints": [
            ("Nur verschlüsselt, ohne Filter", "Encrypted only, unfiltered",
             ["116.202.176.26"], ["2a01:4f8:1c0c:8274::1"],
             "https://doh.libredns.gr/dns-query", "dot.libredns.gr"),
            ("Nur verschlüsselt, mit Werbefilter", "Encrypted only, with ad blocking",
             [], [],
             "https://doh.libredns.gr/noads", "noads.libredns.gr"),
        ],
        "doq": "Nicht dokumentiert.",
        "doq_en": "Not documented.",
        "dnssec": "Nein, und das ist der wichtigste Punkt bei diesem Dienst. LibreDNS validiert nicht. Die eigene Dokumentation vermerkt bei allen DNS-Stamps „DNSSEC: no“, die veröffentlichte Konfiguration setzt „dnssec=process-no-validate“, und eine Messung am 7. September 2026 bestätigte es: Die absichtlich fehlerhaft signierten Testdomains wurden normal beantwortet, während ein validierender Resolver sie ablehnte.",
        "dnssec_en": "No, and that is the most important point about this service. LibreDNS does not validate. Its own documentation records “DNSSEC: no” for every DNS stamp, the published configuration sets “dnssec=process-no-validate”, and a measurement on 7 September 2026 confirmed it: deliberately mis-signed test domains were answered normally, while a validating resolver refused them.",
        "filtering": "Zwei getrennte Rekursoren. Der Standardendpunkt filtert nicht. Der zweite Endpunkt blockt Werbung und Tracker anhand der öffentlichen Liste von StevenBlack.",
        "filtering_en": "Two separate recursors. The default endpoint does not filter. The second one blocks advertising and trackers using the public StevenBlack list.",
        "logging": "Die Website sagt: „We keep no logs. Logs are disabled for our DNS daemon.“ Anders als bei allen anderen Diensten dieser Liste lässt sich das gegenprüfen: Die vollständige Konfiguration liegt öffentlich, und dort ist die Zugriffsprotokollierung des Webservers abgeschaltet und der Resolver auf „quiet“ gesetzt.",
        "logging_en": "The website states: “We keep no logs. Logs are disabled for our DNS daemon.” Unlike every other service in this list, that can be checked: the complete configuration is public, and in it the web server access log is switched off and the resolver is set to “quiet”.",
        "strengths": [
            "Die vollständige Betriebskonfiguration liegt offen. Die No-Log-Zusage lässt sich dadurch technisch nachvollziehen, statt sie nur zu glauben. Das bietet sonst kein Dienst auf dieser Seite.",
            "Die Betreiber sind namentlich benannt, nicht anonym und nicht hinter einer Briefkastenfirma.",
            "Finanzierung ausschließlich über Spenden, mit öffentlich einsehbarem Kassenbuch bei Open Collective. Keine Tarife, keine Werbung, kein Datengeschäft.",
            "Server in Deutschland und damit im EU-Rechtsraum, obwohl das Kollektiv aus Griechenland kommt.",
        ],
        "strengths_en": [
            "The complete operating configuration is public. That makes the no-log commitment technically verifiable rather than merely believable. No other service on this page offers that.",
            "The operators are named individuals, not anonymous and not behind a shell company.",
            "Funded solely by donations, with a publicly readable ledger on Open Collective. No tariffs, no advertising, no data business.",
            "Servers in Germany and therefore within EU jurisdiction, even though the collective is based in Greece.",
        ],
        "caveats": [
            "Keine DNSSEC-Validierung. Wer LibreDNS benutzt, ist gegen gefälschte DNS-Antworten oberhalb des Resolvers nicht geschützt. Für eine Seite über sichere Namensauflösung ist das der schwerste Einwand gegen diesen Dienst, und er wiegt schwerer als die vorbildliche Transparenz.",
            "Ein einziger Server an einem einzigen Standort. Kein Anycast, keine geografische Redundanz, kein Ersatzziel.",
            "Kein Klartext-DNS auf Port 53. Der Dienst ist nur über DoH und DoT erreichbar.",
            "Kein Rechtsträger. Das Kollektiv nutzt Open Collective Europe als Zahlstelle für Spenden; das macht die Stiftung aber nicht zur Betreiberin und begründet keine Haftung für den Dienst.",
            "Nur zwei DoH-Endpunkte und zwei DoT-Namen stehen auf der Website selbst. Weitere Varianten kursieren im Projektwiki und in Apple-Konfigurationsprofilen.",
        ],
        "caveats_en": [
            "No DNSSEC validation. Anyone using LibreDNS is unprotected against forged DNS answers above the resolver. For a page about secure name resolution that is the gravest objection to this service, and it outweighs the exemplary transparency.",
            "A single server in a single location. No anycast, no geographic redundancy, no fallback target.",
            "No plaintext DNS on port 53. The service is reachable only over DoH and DoT.",
            "No legal entity. The collective uses Open Collective Europe as a fiscal host for donations; that does not make the foundation the operator and creates no liability for the service.",
            "Only two DoH endpoints and two DoT names appear on the website itself. Further variants circulate in the project wiki and in Apple configuration profiles.",
        ],
        "sources": [
            ("https://libredns.gr/", "LibreDNS: Endpunkte und Datenschutzaussage", "LibreDNS: endpoints and privacy statement"),
            ("https://libreops.cc/about/", "LibreOps: das Kollektiv dahinter", "LibreOps: the collective behind it"),
            ("https://gitlab.com/libreops/libredns/libredns-cfg", "LibreDNS: vollständige Betriebskonfiguration", "LibreDNS: complete operating configuration"),
            ("https://opencollective.com/libreops", "LibreOps bei Open Collective: offenes Kassenbuch", "LibreOps on Open Collective: open ledger"),
        ],
    },
]

# ---------------------------------------------------------------------------
# Dienste, die eingestellt werden oder eingestellt sind
# ---------------------------------------------------------------------------

DISCONTINUED = [
    {
        "id": "mullvad",
        "severity": "warn",
        "name": "Mullvad Encrypted DNS",
        "state": "Abschaltung am 2. November 2026",
        "state_en": "Shutting down on 2 November 2026",
        "de": """Mullvad hat am 3. September 2026 angekündigt, den öffentlichen verschlüsselten DNS-Dienst
einzustellen und stattdessen Quad9 finanziell zu unterstützen. Der Blogbeitrag trägt den Titel
„Shutting down our public encrypted DNS servers and sponsoring Quad9 instead“ und nennt als Datum
der Abschaltung den 2. November 2026.

Wer die Adressen 194.242.2.2 bis 194.242.2.9 oder die Hostnamen unter dns.mullvad.net eingetragen
hat, sollte jetzt wechseln, nicht erst im November. Der Dienst wird hier nicht mehr empfohlen,
sondern nur noch dokumentiert, damit niemand eine Adresse konfiguriert, die in wenigen Wochen
nicht mehr antwortet.

Zwei Einschränkungen zur Genauigkeit. Erstens spricht der Blogbeitrag ausdrücklich von den
öffentlichen DoH-Servern. Ob die standortfesten Einzelserver und die in das VPN eingebauten
Resolver denselben Zeitplan haben, sagt er nicht. Zweitens hatte Quad9 das angekündigte Sponsoring
am 6. September 2026 auf keiner eigenen Seite bestätigt. Die Ankündigung ist bislang einseitig.""",
        "en": """On 3 September 2026 Mullvad announced that it will discontinue its public encrypted DNS service and
financially support Quad9 instead. The blog post is titled “Shutting down our public encrypted DNS
servers and sponsoring Quad9 instead” and gives 2 November 2026 as the shutdown date.

Anyone who has configured the addresses 194.242.2.2 to 194.242.2.9, or the hostnames under
dns.mullvad.net, should switch now rather than in November. The service is no longer recommended
here, only documented, so that nobody configures an address that will stop answering within weeks.

Two qualifications for accuracy. First, the blog post explicitly refers to the public DoH servers.
It does not say whether the location-specific single servers and the resolvers built into the VPN
follow the same timetable. Second, as of 6 September 2026 Quad9 had not confirmed the announced
sponsorship on any of its own pages. The announcement is so far one-sided.""",
        "sources": [
            ("https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead", "Mullvad: Shutting down our public encrypted DNS servers, 03.09.2026", "Mullvad: Shutting down our public encrypted DNS servers, 3 September 2026"),
        ],
    },
    {
        "id": "dns0eu",
        "severity": "stop",
        "name": "dns0.eu",
        "state": "Eingestellt seit Oktober 2025",
        "state_en": "Discontinued since October 2025",
        "de": """dns0.eu wird in vielen Empfehlungslisten weiterhin geführt. Der Dienst existiert nicht mehr.

Der Betreiber, ein in Paris eingetragener französischer Verein, kündigte die Einstellung zwischen
dem 14. und dem 18. Oktober 2025 an, mit dem Hinweis: „The dns0.eu service has been discontinued.
We would have liked to keep it running, but it was not sustainable for us in terms of time and
resources.“ Die Domain zeigt inzwischen nur noch eine Parkseite.

Am 6. September 2026 antwortete keine der ehemaligen Adressen mehr, weder 193.110.81.0 noch
185.253.5.0 und auch keine der Varianten ZERO, KIDS oder OPEN. Wer diese Adressen noch eingetragen
hat, sollte sie entfernen. Nicht nur, weil sie ausgefallen sind, sondern weil IP-Bereiche später
neu vergeben werden können.""",
        "en": """dns0.eu still appears in many recommendation lists. The service no longer exists.

The operator, a French association registered in Paris, announced the shutdown between 14 and
18 October 2025, stating: “The dns0.eu service has been discontinued. We would have liked to keep it
running, but it was not sustainable for us in terms of time and resources.” The domain now shows
only a parking page.

On 6 September 2026 none of the former addresses answered, neither 193.110.81.0 nor 185.253.5.0,
and none of the ZERO, KIDS or OPEN variants. Anyone still using these addresses should remove them.
Not only because they are down, but because IP ranges can later be reassigned to someone else.""",
        "sources": [
            ("https://web.archive.org/web/20251018114400/https://www.dns0.eu/", "Internet Archive: dns0.eu mit Abschaltungshinweis, 18.10.2025", "Internet Archive: dns0.eu showing the shutdown notice, 18 October 2025"),
        ],
    },
    {
        "id": "ahadns",
        "severity": "stop",
        "name": "AhaDNS",
        "state": "Praktisch eingestellt",
        "state_en": "Effectively discontinued",
        "de": """AhaDNS wird in vielen Listen weiterhin als datenschutzfreundliche Alternative geführt. Am 7. September 2026
antwortete kein einziger der zehn auf der eigenen Website dokumentierten Standorte mehr.

Von den zehn angegebenen Endpunkten existieren acht nicht einmal mehr als Namenseintrag; die autoritative Abfrage
liefert für sie NXDOMAIN. Die verbleibenden zwei, die Standorte Niederlande und Los Angeles, lösen zwar noch auf,
nehmen aber keine Verbindung mehr an: Der eine antwortet auf keinem Port, der andere weist die Ports 53, 443 und 853
aktiv zurück.

Die Website nennt die Adressen unverändert weiter. Eine Abschaltungsmeldung gibt es nicht. Wer die Adressen eingetragen
hat, sollte sie entfernen.""",
        "en": """AhaDNS still appears in many lists as a privacy-friendly alternative. On 7 September 2026 not one of the ten locations
documented on its own website answered any more.

Of the ten endpoints listed, eight no longer exist even as a name entry; the authoritative query returns NXDOMAIN for
them. The remaining two, the Netherlands and Los Angeles locations, still resolve but accept no connection: one answers
on no port at all, the other actively refuses ports 53, 443 and 853.

The website continues to list the addresses unchanged. There is no shutdown notice. Anyone who has configured these
addresses should remove them.""",
        "sources": [
            ("https://ahadns.com/dns-over-tls/", "AhaDNS: die weiterhin genannten DoT-Endpunkte",
             "AhaDNS: the DoT endpoints still listed"),
            ("https://ahadns.com/dns-over-https/", "AhaDNS: die weiterhin genannten DoH-Endpunkte",
             "AhaDNS: the DoH endpoints still listed"),
        ],
    },
]

# ---------------------------------------------------------------------------
# Die grossen kommerziellen Resolver, zur Einordnung
# ---------------------------------------------------------------------------

COMMERCIAL = [
    {
        "name": "Cloudflare",
        "addresses": "1.1.1.1 und 1.0.0.1, gefilterte Varianten 1.1.1.2 und 1.1.1.3",
        "addresses_en": "1.1.1.1 and 1.0.0.1, filtered variants 1.1.1.2 and 1.1.1.3",
        "de": """Cloudflare, Inc. ist eine US-Gesellschaft. Die Datenschutzzusage ist ungewöhnlich konkret: Quell-IP-Adressen
werden nach eigener Angabe nicht dauerhaft gespeichert, gekürzte Adressen und Protokolldaten innerhalb von
25 Stunden gelöscht. Es gibt eine Ausnahme für höchstens 0,05 Prozent zufällig gesampelter Netzwerkpakete,
für die keine Frist genannt wird. Aggregierte Auswertungen dürfen unbegrenzt gespeichert werden. Cloudflare
gibt Abfragedaten ohne Client-IP an APNIC Labs weiter. Ein externes Audit ist zugesagt.""",
        "en": """Cloudflare, Inc. is a US company. Its privacy commitment is unusually specific: source IP addresses are,
by its own account, not stored persistently, and truncated addresses and log data are deleted within
25 hours. There is an exception for at most 0.05 per cent of randomly sampled network packets, for which
no retention period is stated. Aggregated analyses may be stored indefinitely. Cloudflare shares query
data without client IP with APNIC Labs. An external audit is promised.""",
        "source": ("https://developers.cloudflare.com/1.1.1.1/privacy/public-dns-resolver/", "Cloudflare: Public DNS Resolver Privacy", "Cloudflare: Public DNS Resolver Privacy"),
    },
    {
        "name": "Google Public DNS",
        "addresses": "8.8.8.8 und 8.8.4.4",
        "addresses_en": "8.8.8.8 and 8.8.4.4",
        "de": """Google LLC, US-Gesellschaft. Google Public DNS ist kein Malware-Blocker, behält sich aber
sicherheitsbedingte Sperren sowie die Umsetzung gerichtlicher Anordnungen vor. Google sendet EDNS Client
Subnet an autoritative Server, die es unterstützen, was die Auflösung geografisch näher macht und zugleich
einen gekürzten Teil der Client-Adresse an Dritte weitergibt.""",
        "en": """Google LLC, a US company. Google Public DNS is not a malware blocker, but reserves the right to apply
security-related blocks and to implement court orders. Google sends EDNS Client Subnet to authoritative
servers that support it, which brings resolution geographically closer while also passing a truncated part
of the client address to third parties.""",
        "source": ("https://developers.google.com/speed/public-dns/privacy", "Google Public DNS: Privacy", "Google Public DNS: Privacy"),
    },
    {
        "name": "AdGuard DNS",
        "addresses": "94.140.14.14 gefiltert, 94.140.14.140 ungefiltert",
        "addresses_en": "94.140.14.14 filtered, 94.140.14.140 unfiltered",
        "de": """AdGuard Software Limited mit Sitz in Limassol, Zypern. Der Dienst bietet gefilterte und ungefilterte
Adressen sowie DoH, DoT, DoQ und DNSCrypt. Die verwendete Filterliste liegt als öffentliches Repository mit
offenem Fehlerregister vor, Fehlklassifikationen sind also nachvollziehbar meldbar.""",
        "en": """AdGuard Software Limited, based in Limassol, Cyprus. The service offers filtered and unfiltered addresses
as well as DoH, DoT, DoQ and DNSCrypt. The filter list used is available as a public repository with an open
issue tracker, so anyone can report a misclassification in public and follow what happens to it.""",
        "source": ("https://adguard-dns.io/en/public-dns.html", "AdGuard DNS: Public DNS", "AdGuard DNS: Public DNS"),
    },
    {
        "name": "Cisco OpenDNS",
        "addresses": "208.67.222.222 und 208.67.220.220, FamilyShield 208.67.222.123 und 208.67.220.123",
        "addresses_en": "208.67.222.222 and 208.67.220.220, FamilyShield 208.67.222.123 and 208.67.220.123",
        "de": """Cisco Systems, Inc., börsennotierter US-Konzern. Der freie Dienst ist der Einstieg in das kostenpflichtige
Cisco Umbrella. Bemerkenswert ist, was fehlt: Eine eigene Datenschutzerklärung für den DNS-Dienst gibt es nicht mehr,
die frühere Adresse zeigt nur noch die allgemeine Cisco-Erklärung. Damit fehlen eine No-Log-Zusage und jede
veröffentlichte Aufbewahrungsfrist für Abfragedaten. DNSSEC wird validiert. In Frankreich und Portugal hat Cisco den
Dienst nach Gerichtsentscheidungen nicht gefiltert, sondern landesweit ganz abgeschaltet.""",
        "en": """Cisco Systems, Inc., a listed US corporation. The free service is the entry point to the paid Cisco Umbrella.
What is missing is notable: there is no longer a dedicated privacy policy for the DNS service, and the former address
now shows only the general Cisco statement. That leaves no no-log commitment and no published retention period for
query data. DNSSEC is validated. In France and Portugal, following court decisions, Cisco did not filter the service
but shut it down countrywide.""",
        "source": ("https://www.opendns.com/setupguide/", "OpenDNS: Einrichtung und Adressen",
                   "OpenDNS: setup and addresses"),
    },
    {
        "name": "NextDNS",
        "addresses": "Konto erforderlich; die Adressen hängen an der eigenen Konfigurations-ID",
        "addresses_en": "Account required; the addresses depend on your own configuration ID",
        "de": """NextDNS Inc., Delaware, USA. Der Dienst ist kein fertiger Resolver, sondern ein Baukasten: Filterlisten,
Sperrzeiten und Protokollierung stellt man selbst ein. Die Datenschutzerklärung sagt wörtlich: „If not specifically
requested by the user, no data is logged.“ Wer Auswertungen möchte, schaltet die Protokollierung selbst ein und wählt
Aufbewahrungsdauer und Region. Gegen den Dienst spricht die Trägerschaft: eine gewinnorientierte US-Gesellschaft ohne
Transparenzbericht, ohne unabhängiges Audit und mit einer Datenschutzerklärung ohne Datum und ohne Versionsverlauf.
Auch bei europäischer Log-Region bleibt der Betreiber ein US-Unternehmen.""",
        "en": """NextDNS Inc., Delaware, USA. The service is not a finished resolver but a construction kit: you configure the
filter lists, schedules and logging yourself. The privacy policy states verbatim: “If not specifically requested by the
user, no data is logged.” Anyone wanting analytics switches logging on themselves and picks the retention period and
region. What speaks against it is who runs it: a for-profit US corporation with no transparency report, no independent
audit and a privacy policy carrying no date and no version history. Even with a European log region, the operator
remains a US company.""",
        "source": ("https://nextdns.io/privacy", "NextDNS: Datenschutzerklärung", "NextDNS: privacy policy"),
    },
    {
        "name": "Control D",
        "addresses": "Kostenlose Profile: 76.76.2.0 ungefiltert, 76.76.2.1 Malware, 76.76.2.2 Werbung und Tracker",
        "addresses_en": "Free profiles: 76.76.2.0 unfiltered, 76.76.2.1 malware, 76.76.2.2 ads and trackers",
        "de": """Control D bietet ohne Konto mehrere feste Profile mit eigenen Adressen und DoH-Pfaden, darunter ein
ungefiltertes. Das Unternehmen unterhält ein öffentliches Compliance-Portal mit herunterladbaren Prüfberichten nach
SOC 2 und ISO 27001, was unter den hier genannten Diensten ungewöhnlich ist. Die Kehrseite steht im selben Portal:
„If Analytics is enabled, we log DNS queries and metadata (e.g. source IP, hostname, MAC address).“ Ob die Auswertung
im Auslieferungszustand aus ist, sagt die Dokumentation nicht.""",
        "en": """Control D offers several fixed profiles without an account, each with its own addresses and DoH paths, including
an unfiltered one. The company runs a public compliance portal with downloadable SOC 2 and ISO 27001 attestation
reports, which is unusual among the services named here. The flip side appears in the same portal: “If Analytics is
enabled, we log DNS queries and metadata (e.g. source IP, hostname, MAC address).” Whether analytics is off in the
delivered state is not stated in the documentation.""",
        "source": ("https://controld.com/free-dns", "Control D: kostenlose Profile", "Control D: free profiles"),
    },
]

# ---------------------------------------------------------------------------
# Selbst betreiben
# ---------------------------------------------------------------------------

SELFHOSTED = [
    {
        "name": "Unbound",
        "by": "NLnet Labs, Niederlande",
        "by_en": "NLnet Labs, Netherlands",
        "license": "BSD 3-Clause",
        "kind": "Vollwertiger validierender rekursiver Resolver",
        "kind_en": "Full validating recursive resolver",
        "de": """Unbound löst selbst ab den Root-Servern auf, statt eine Anfrage an einen fremden Resolver weiterzureichen.
Damit verschwindet der zentrale Mitleser: Kein einzelner Betreiber sieht mehr die vollständige Abfragehistorie.
DNSSEC-Validierung ist eingebaut und in der Standardkonfiguration aktiv, sie braucht allerdings einen gesetzten
Vertrauensanker. Die Handbuchseite sagt dazu ausdrücklich: „You must also set trust-anchors for validation to be
useful.“ Unbound kann auch als Forwarder über DoT laufen, wenn man die Rekursion nicht selbst machen will.

Träger ist NLnet Labs, eine niederländische Non-Profit-Organisation, die von den niederländischen Steuerbehörden
als gemeinnützig anerkannt ist. Sie sagt zur Kontinuität zu, eine Einstellung der Softwarepflege mindestens zwei
Jahre im Voraus anzukündigen.""",
        "en": """Unbound resolves from the root servers itself instead of handing a query to somebody else’s resolver. That
removes the central observer: no single operator sees the full query history any more. DNSSEC validation is built
in and active in the default configuration, but it requires a configured trust anchor. The manual page states
explicitly: “You must also set trust-anchors for validation to be useful.” Unbound can also run as a forwarder over
DoT if you would rather not do the recursion yourself.

The carrier is NLnet Labs, a Dutch non-profit recognised as a public benefit organisation by the Dutch tax
authorities. On continuity it commits to announcing any end of software maintenance at least two years in advance.""",
        "sources": [("https://nlnetlabs.nl/projects/unbound/about/", "NLnet Labs: Unbound", "NLnet Labs: Unbound")],
    },
    {
        "name": "Knot Resolver",
        "by": "CZ.NIC, Tschechien",
        "by_en": "CZ.NIC, Czechia",
        "license": "GPL-3.0-or-later",
        "kind": "Vollwertiger validierender rekursiver Resolver",
        "kind_en": "Full validating recursive resolver",
        "de": """Knot Resolver stammt von CZ.NIC, der Betreiberin der tschechischen Landesdomain .cz. DNSSEC-Validierung ist
seit Version 4.0 standardmäßig aktiv. Bemerkenswert ist die Ehrlichkeit der eigenen Dokumentation. Sie warnt
ausdrücklich davor, verschlüsseltes DNS mit Privatsphäre gleichzusetzen: „Latest research has proven that encrypting
DNS traffic is not sufficient to protect the users' privacy. Therefore, we recommend all users to use a full VPN
instead of encrypting just DNS queries.“ Ein Projekt, das die Grenzen des eigenen Produkts benennt, verdient
mehr Vertrauen als eines, das sie verschweigt.

Wegen der GPL ist Knot Resolver anders als Unbound nicht ohne Weiteres in geschlossene Geräte einbettbar. Für den
Eigenbetrieb spielt das keine Rolle.""",
        "en": """Knot Resolver comes from CZ.NIC, the operator of the Czech country domain .cz. DNSSEC validation has been on
by default since version 4.0. What stands out is the honesty of its own documentation. It explicitly warns against
equating encrypted DNS with privacy: “Latest research has proven that encrypting DNS traffic is not sufficient to
protect the users' privacy. Therefore, we recommend all users to use a full VPN instead of encrypting just DNS
queries.” A project that names the limits of its own product deserves more trust than one that hides them.

Because of the GPL, Knot Resolver, unlike Unbound, cannot readily be embedded in closed devices. For self-hosting
that makes no difference.""",
        "sources": [("https://www.knot-resolver.cz/", "CZ.NIC: Knot Resolver", "CZ.NIC: Knot Resolver")],
    },
    {
        "name": "Pi-hole",
        "by": "Pi-hole, LLC",
        "license": "EUPL v1.2",
        "kind": "DNS-Sinkhole zum Filtern, kein eigener Resolver",
        "kind_en": "DNS sinkhole for filtering, not a resolver of its own",
        "de": """Pi-hole ist ein DNS-Sinkhole, kein rekursiver Resolver. Es prüft Anfragen gegen Blocklisten und reicht alles
Übrige an einen konfigurierten Upstream weiter. Die technische Basis ist ein dnsmasq-Abkömmling namens FTL.

Zwei Punkte, die oft falsch dargestellt werden. Erstens ist Google 8.8.8.8 als Upstream voreingestellt.
Wer Pi-hole installiert und nichts ändert, schickt weiterhin jede nicht geblockte Anfrage an Google, nur gebündelt
über eine einzige IP. Zweitens ist DNSSEC-Validierung zwar eingebaut, aber standardmäßig ausgeschaltet.

Verschlüsselten Transport bringt Pi-hole von Haus aus weder zu den Clients noch zum Upstream mit. Wer echte
Rekursion will, installiert zusätzlich Unbound und trägt es als lokalen Upstream ein. Die Rekursion leistet dann
Unbound, nicht Pi-hole.""",
        "en": """Pi-hole is a DNS sinkhole, not a recursive resolver. It checks queries against block lists and forwards
everything else to a configured upstream. The technical base is a dnsmasq derivative called FTL.

Two points that are often misrepresented. First, the default upstream is Google 8.8.8.8. Anyone who installs
Pi-hole and changes nothing still sends every unblocked query to Google, merely bundled through a single IP.
Second, DNSSEC validation is built in but switched off by default.

Pi-hole ships no encrypted transport, neither towards the clients nor towards the upstream. If you want real
recursion, you additionally install Unbound and enter it as a local upstream. The recursion is then done by
Unbound, not by Pi-hole.""",
        "sources": [("https://docs.pi-hole.net/guides/dns/unbound/", "Pi-hole: Unbound als rekursiver Upstream", "Pi-hole: Unbound as a recursive upstream")],
    },
    {
        "name": "AdGuard Home",
        "by": "AdGuard Software Limited, Zypern",
        "by_en": "AdGuard Software Limited, Cyprus",
        "license": "GPL-3.0",
        "kind": "Eigener DNS-Server mit Filterung, arbeitet als Forwarder",
        "kind_en": "A standalone DNS server with filtering; operates as a forwarder",
        "de": """AdGuard Home ist anders als Pi-hole kein Aufsatz auf dnsmasq, sondern ein eigenständiger, in Go geschriebener
DNS-Server. Es kann DoH, DoT und DoQ ohne Zusatzsoftware für die eigenen Clients anbieten. Das ist der praktische
Vorteil gegenüber Pi-hole: Mobilgeräte können den heimischen Filter auch von unterwegs verschlüsselt erreichen.

Die Option „Enable DNSSEC“ bedeutet nicht, dass AdGuard Home selbst
validiert. Es setzt das DO-Bit und verlässt sich auf den Upstream. Wer echte lokale Validierung will, braucht einen
validierenden Resolver davor oder dahinter.

Rekursiv arbeitet AdGuard Home nicht. Ein gewählter Upstream sieht weiterhin alle nicht geblockten Anfragen.""",
        "en": """Unlike Pi-hole, AdGuard Home is not a layer on top of dnsmasq but a standalone DNS server written in Go. It can
offer DoH, DoT and DoQ to its own clients without extra software. That is its practical advantage over Pi-hole:
mobile devices can reach the home filter over an encrypted connection from anywhere.

One point that is frequently overstated: the “Enable DNSSEC” option does not mean AdGuard Home validates by itself.
It sets the DO bit and relies on the upstream. Anyone who wants genuine local validation needs a validating resolver
in front of or behind it.

AdGuard Home does not work recursively. A chosen upstream still sees every unblocked query.""",
        "sources": [("https://github.com/AdguardTeam/AdGuardHome", "AdGuard Home: Repository und Dokumentation", "AdGuard Home: repository and documentation")],
    },
    {
        "name": "Technitium DNS Server",
        "by": "Technitium",
        "license": "GPL-3.0",
        "kind": "Autoritativer Server und rekursiver Resolver in einem",
        "kind_en": "Authoritative server and recursive resolver in one",
        "de": """Technitium deckt beides ab: eigene Rekursion ab den Root-Servern einschließlich QNAME-Minimierung nach RFC 9156
oder Forwarder-Betrieb über DoT, DoH und DoQ zu einem öffentlichen Resolver. Es bringt eine Weboberfläche, Blocklisten,
einen DHCP-Server und eine HTTP-Schnittstelle mit und kann DoT, DoH und DoQ auch selbst für die eigenen Clients
anbieten, DoH dabei über HTTP/1.1, HTTP/2 und HTTP/3.

Für ein Heimnetz oder ein kleines Büro ist das die vollständigste Einzellösung dieser Liste.""",
        "en": """Technitium covers both: its own recursion from the root servers including QNAME minimisation per RFC 9156, or
forwarder operation over DoT, DoH and DoQ to a public resolver. It ships a web console, block lists, a DHCP server and
an HTTP API, and can itself offer DoT, DoH and DoQ to its own clients, with DoH over HTTP/1.1, HTTP/2 and HTTP/3.

For a home network or a small office this is the most complete single solution in this list.""",
        "sources": [("https://github.com/TechnitiumSoftware/DnsServer", "Technitium DNS Server: Repository", "Technitium DNS Server: Repository")],
    },
    {
        "name": "dnscrypt-proxy",
        "by": "Frank Denis",
        "license": "ISC",
        "kind": "Lokaler verschlüsselnder Proxy, kein Resolver",
        "kind_en": "Local encrypting proxy, not a resolver",
        "de": """dnscrypt-proxy nimmt unverschlüsseltes DNS auf einem lokalen Socket entgegen und schickt es verschlüsselt an einen
öffentlichen Resolver. Es unterstützt DNSCrypt, DoH und, was es von den meisten anderen unterscheidet, Anonymized DNSCrypt und
Oblivious DoH nach RFC 9230. Diese beiden trennen die Frage „wer fragt“ von der Frage „was wird gefragt“, indem ein
Relais dazwischentritt, das den Inhalt nicht sieht, während der Resolver die Client-Adresse nicht sieht.

Der sachliche Unterschied zwischen DNSCrypt und DoH liegt nicht in der Stärke der Verschlüsselung, sondern im
Vertrauensanker. DNSCrypt nutzt einen fest hinterlegten öffentlichen Schlüssel des Anbieters ohne Zertifizierungsstelle.
DoH nutzt die übliche Zertifikatskette und einen Hostnamen, der ohne Encrypted Client Hello im Klartext übertragen wird.
Ein Beobachter sieht bei DoH also üblicherweise, welchen Anbieter man nutzt.

Das Projekt benennt die Grenze selbst: „one still has to trust non-logging DNS servers for actually doing what they pretend
to do.“""",
        "en": """dnscrypt-proxy accepts unencrypted DNS on a local socket and sends it encrypted to a public resolver. It supports
DNSCrypt, DoH and, unlike most alternatives, Anonymized DNSCrypt and Oblivious DoH per RFC 9230. Those two separate the
question of “who is asking” from “what is being asked” by inserting a relay that cannot see the content, while the
resolver cannot see the client address.

The substantive difference between DNSCrypt and DoH is not the strength of the encryption but the trust anchor. DNSCrypt
uses a hard-coded provider public key with no certificate authority. DoH uses the usual certificate chain and a hostname
that, without Encrypted Client Hello, travels in the clear. With DoH an observer therefore usually sees which provider
you use.

The project states the limit itself: “one still has to trust non-logging DNS servers for actually doing what they pretend
to do.”""",
        "sources": [("https://github.com/DNSCrypt/dnscrypt-proxy", "dnscrypt-proxy: Repository und Wiki", "dnscrypt-proxy: repository and wiki")],
    },
]

# ---------------------------------------------------------------------------
# Protokolle. Jede RFC-Nummer wurde am Volltext beim RFC Editor geprueft.
# ---------------------------------------------------------------------------

PROTOCOLS = [
    {
        "abbr": "Do53",
        "title": "Klassisches DNS im Klartext",
        "title_en": "Classic DNS in the clear",
        "rfc": "RFC 1035, STD 13",
        "port": "UDP und TCP 53",
        "port_en": "UDP and TCP 53",
        "de": """Der Standardfall seit 1987. RFC 1035 legt fest, dass DNS über UDP und TCP auf Port 53 läuft, und sieht
keinerlei Vertraulichkeit vor. Wer im selben Netz sitzt oder das Netz betreibt, liest jede Anfrage mit.

RFC 9076, das aktuelle IETF-Dokument zu den Datenschutzaspekten des DNS, benennt den lohnendsten Abhörpunkt
ausdrücklich: „The best place to tap, from an eavesdropper's point of view, is clearly between the stub resolvers
and the recursive resolvers, because traffic is not limited by DNS caching.“ Genau diese Strecke verschlüsseln
DoT, DoH und DoQ.""",
        "en": """The default case since 1987. RFC 1035 specifies that DNS runs over UDP and TCP on port 53 and provides for no
confidentiality at all. Anyone on the same network, or running it, reads every query.

RFC 9076, the current IETF document on DNS privacy considerations, names the most rewarding tapping point explicitly:
“The best place to tap, from an eavesdropper's point of view, is clearly between the stub resolvers and the recursive
resolvers, because traffic is not limited by DNS caching.” That is precisely the stretch DoT, DoH and DoQ encrypt.""",
    },
    {
        "abbr": "DoT",
        "title": "DNS over TLS",
        "title_en": "DNS over TLS",
        "rfc": "RFC 7858",
        "port": "TCP 853",
        "de": """DNS in einem TLS-Tunnel auf einem eigenen Port. RFC 7858 legt fest: „By default, a DNS server that supports
DNS over TLS MUST listen for and accept TCP connections on port 853, unless it has mutual agreement with its clients to use a port other than 853 for DNS over TLS.“

Der eigene Port ist Vorteil und Nachteil zugleich. Vorteil: Das Betriebssystem kann DoT systemweit für alle Programme
setzen, was Android seit Jahren unter „Privates DNS“ tut. Nachteil: Port 853 ist sichtbar und in restriktiven Netzen
leicht zu sperren.""",
        "en": """DNS inside a TLS tunnel on a dedicated port. RFC 7858 specifies: “By default, a DNS server that supports DNS over
TLS MUST listen for and accept TCP connections on port 853, unless it has mutual agreement with its clients to use a port
other than 853 for DNS over TLS.”

The dedicated port is both an advantage and a drawback. Advantage: the operating system can set DoT system-wide for all
applications, which is what Android has done for years under “Private DNS”. Drawback: port 853 is visible and easy to
block on restrictive networks.""",
    },
    {
        "abbr": "DoH",
        "title": "DNS over HTTPS",
        "title_en": "DNS over HTTPS",
        "rfc": "RFC 8484",
        "port": "TCP 443",
        "de": """DNS in gewöhnlichen HTTPS-Anfragen. RFC 8484 beschreibt es so: „Each DNS query-response pair is mapped into an
HTTP exchange.“

Weil der Verkehr auf Port 443 läuft, ist er von normalem Web-Verkehr kaum zu unterscheiden und entsprechend schwer zu
sperren. Der Preis: DoH wird meist pro Anwendung eingestellt, nicht systemweit. Ein Browser mit eigenem DoH nutzt einen
anderen Resolver als der Rest des Systems, was in der Praxis regelmäßig zu Verwirrung führt.""",
        "en": """DNS inside ordinary HTTPS requests. RFC 8484 states it in one line: “Each DNS query-response pair is mapped into an HTTP
exchange.”

Because the traffic runs on port 443 it is hard to distinguish from normal web traffic and correspondingly hard to block.
The price: DoH is usually configured per application rather than system-wide. A browser with its own DoH uses a different
resolver from the rest of the system, which regularly causes confusion in practice.""",
    },
    {
        "abbr": "DoQ",
        "title": "DNS over QUIC",
        "title_en": "DNS over QUIC",
        "rfc": "RFC 9250",
        "port": "UDP 853",
        "de": """Der jüngste der drei verschlüsselten Transporte, standardisiert im Mai 2022. RFC 9250 beschreibt den Vorteil so:
„The encryption provided by QUIC has similar properties to those provided by TLS, while QUIC transport eliminates the
head-of-line blocking issues inherent with TCP and provides more efficient packet-loss recovery than UDP.“

In der Praxis heißt das: gleiche Vertraulichkeit wie DoT, aber schnellerer Verbindungsaufbau und weniger Verzögerung bei
Paketverlust. Quad9 beantwortete DoQ-Abfragen im Test zuverlässig. UncensoredDNS, dnsforge.de und Freifunk München kündigen DoQ ebenfalls an; bei UncensoredDNS blieb eine echte Abfrage im Test allerdings unbeantwortet.""",
        "en": """The most recent of the three encrypted transports, standardised in May 2022. RFC 9250 describes the benefit as
follows: “The encryption provided by QUIC has similar properties to those provided by TLS, while QUIC transport eliminates
the head-of-line blocking issues inherent with TCP and provides more efficient packet-loss recovery than UDP.”

In practice that means the same confidentiality as DoT, but faster connection setup and less delay under packet loss. Quad9 answered DoQ queries reliably in our test. UncensoredDNS, dnsforge.de and Freifunk München announce DoQ as well,
though at UncensoredDNS a real query went unanswered in our test.""",
    },
    {
        "abbr": "DNSSEC",
        "title": "Signaturen, keine Verschlüsselung",
        "title_en": "Signatures, not encryption",
        "rfc": "RFC 4033, 4034, 4035",
        "port": "unabhängig vom Transport",
        "port_en": "independent of the transport",
        "de": """Die häufigste Verwechslung auf diesem Themenfeld. DNSSEC verschlüsselt nichts. RFC 4033 sagt in einem Satz, was es
leistet: „The Domain Name System Security Extensions (DNSSEC) add data origin authentication and data integrity to the
Domain Name System.“ Und es sagt ebenso deutlich, was es nicht leistet: „These extensions do not provide confidentiality.“

DNSSEC schützt also davor, dass jemand die Antwort fälscht. Es schützt nicht davor, dass jemand die Frage mitliest. Beides
zusammen bekommt man erst, wenn ein validierender Resolver über einen verschlüsselten Transport erreicht wird.

Eine Nebenwirkung sollte man kennen: RFC 4033 warnt, dass DNSSEC in der NSEC-Variante das Aufzählen aller Namen einer Zone
ermöglicht. Für die Privatsphäre von Zoneninhalten ist DNSSEC also kein Gewinn.""",
        "en": """The most common confusion in this field. DNSSEC encrypts nothing. RFC 4033 says in one sentence what it does: “The
Domain Name System Security Extensions (DNSSEC) add data origin authentication and data integrity to the Domain Name
System.” And it says just as plainly what it does not do: “These extensions do not provide confidentiality.”

So DNSSEC protects against someone forging the answer. It does not protect against someone reading the question. You only
get both once a validating resolver is reached over an encrypted transport.

One side effect is worth knowing: RFC 4033 warns that DNSSEC in its NSEC variant allows enumeration of all names in a zone.
For the privacy of zone contents, DNSSEC is therefore no gain.""",
    },
    {
        "abbr": "QNAME",
        "title": "QNAME-Minimierung",
        "title_en": "QNAME minimisation",
        "rfc": "RFC 9156",
        "port": "Verhalten des Resolvers",
        "port_en": "resolver behaviour",
        "de": """Ohne Minimierung fragt ein rekursiver Resolver den Root-Server nach dem vollen Namen, obwohl der Root-Server nur die
Zuständigkeit für die Endung kennt. Mit Minimierung erfährt jede Ebene nur so viel, wie sie zur Weiterleitung braucht.

Wichtig für die Genauigkeit: Der gültige Standard ist RFC 9156 aus dem November 2021, Standards Track. Der oft zitierte
RFC 7816 war experimentell und ist ausdrücklich als überholt gekennzeichnet.""",
        "en": """Without minimisation a recursive resolver asks the root server for the full name, even though the root server only
knows who is responsible for the suffix. With minimisation each level learns only as much as it needs in order to refer the
query onwards.

Important for accuracy: the valid standard is RFC 9156 from November 2021, Standards Track. The frequently cited RFC 7816
was experimental and is explicitly marked as obsoleted.""",
    },
    {
        "abbr": "ECS",
        "title": "EDNS Client Subnet",
        "title_en": "EDNS Client Subnet",
        "rfc": "RFC 7871",
        "port": "Erweiterung, informational",
        "port_en": "extension, informational",
        "de": """Der Resolver reicht einen gekürzten Teil der Client-Adresse an autoritative Server weiter, damit ein Content-Netz eine
geografisch nahe Antwort geben kann. Der Preis ist Privatsphäre.

Der RFC rät selbst zur Zurückhaltung: „We recommend that the feature be turned off by default in all
nameserver software, and that operators only enable it explicitly in those circumstances where it provides a clear benefit for
their clients.“ RFC 7871 ist informational, kein Standards Track.

Praktische Folge: Wer Privatsphäre über Geschwindigkeit stellt, wählt einen Endpunkt ohne ECS. Bei Quad9 sind das 9.9.9.9 und
9.9.9.10, während 9.9.9.11 und 9.9.9.12 ECS ausdrücklich einsetzen.""",
        "en": """The resolver passes a truncated part of the client address on to authoritative servers so that a content network can give
a geographically close answer. The price is privacy.

It is notable that the RFC itself counsels restraint: “We recommend that the feature be turned off by default in all nameserver
software, and that operators only enable it explicitly in those circumstances where it provides a clear benefit for their
clients.” RFC 7871 is informational, not Standards Track.

Practical consequence: anyone putting privacy above speed picks an endpoint without ECS. At Quad9 those are 9.9.9.9 and
9.9.9.10, while 9.9.9.11 and 9.9.9.12 deliberately use ECS.""",
    },
    {
        "abbr": "Padding",
        "title": "EDNS(0) Padding",
        "title_en": "EDNS(0) Padding",
        "rfc": "RFC 7830",
        "port": "Erweiterung",
        "port_en": "extension",
        "de": """Verschlüsselung verbirgt den Inhalt, nicht die Größe. RFC 9076 weist darauf hin, dass sich aus Größe und zeitlichem Muster
verschlüsselter Nachrichten Rückschlüsse ziehen lassen. Als Gegenmittel definiert RFC 7830 eine Auffüllung auf einheitliche Längen. Wer
einen Resolver selbst betreibt, sollte Padding aktivieren.""",
        "en": """Encryption hides the content, not the size. RFC 9076 points out that the size and timing patterns of encrypted messages allow
inferences. RFC 7830 defines padding to uniform lengths as a countermeasure. Anyone running a resolver themselves should enable
padding.""",
    },
]

# ---------------------------------------------------------------------------
# Die ehrliche Einschraenkung. Der wichtigste Abschnitt der Seite.
# ---------------------------------------------------------------------------

LIMITS_DE = """Verschlüsseltes DNS verbirgt, welche Namen Sie nachschlagen. Es verbirgt nicht, welche Server Sie
danach besuchen.

Das ist keine Relativierung, sondern die Aussage der Spezifikation selbst. RFC 9849, die Spezifikation von Encrypted
Client Hello vom März 2026, formuliert es so: „ECH is not in itself sufficient to protect the identity of the server. The
target domain may also be visible through other channels, such as plaintext client DNS queries or visible server IP
addresses.“ Umgekehrt gilt dasselbe: Verschlüsseltes DNS allein reicht nicht, solange der Servername im TLS-Handshake als
Server Name Indication im Klartext steht und die Ziel-IP-Adresse ohnehin sichtbar bleibt.

Was ein anderer DNS-Anbieter also bewirkt:

Er nimmt Ihrem Zugangsanbieter den bequemsten Beobachtungsposten. Statt einer sauber lesbaren Liste von Domainnamen sieht
er verschlüsselten Verkehr zu einer IP-Adresse. Er nimmt ihm außerdem die Möglichkeit, Antworten stillschweigend zu
verändern. Und er nimmt ihm die Rolle des Adressaten von DNS-Sperren, soweit der neue Anbieter denselben Anordnungen nicht
unterliegt.

Was er nicht bewirkt:

Er macht Sie nicht anonym. Der neue Resolver sieht nun das, was vorher der Zugangsanbieter sah. Sie tauschen einen
Mitwisser gegen einen anderen und sollten deshalb einen wählen, dessen Interessen Ihren eigenen nicht widersprechen. Er
ersetzt kein VPN und kein Tor. Und er ist kein Virenschutz: Ein DNS-Filter greift nur, solange ein Name aufgelöst wird,
und lässt sich durch eine direkte IP-Verbindung umgehen.

Die Bundesnetzagentur schreibt dazu in eigener Sache: „Ein kritischer Punkt bei der DNS-Sperre ist, dass eine solche
Sperre leicht umgangen werden kann.“ Das gilt für Sperren, die man ablehnt, genauso wie für Schutzfilter, die man
möchte."""

LIMITS_EN = """Encrypted DNS hides which names you look up. It does not hide which servers you visit afterwards.

That is not a hedge but the statement of the relevant standard itself. RFC 9849, the Encrypted Client Hello specification
from March 2026, puts it this way: “ECH is not in itself sufficient to protect the identity of the server. The target
domain may also be visible through other channels, such as plaintext client DNS queries or visible server IP addresses.”
The converse holds too: encrypted DNS alone is not enough while the server name travels in the clear in the TLS handshake
as Server Name Indication, and the destination IP address remains visible anyway.

So here is what changing your DNS provider actually achieves:

It takes away your access provider’s most convenient observation post. Instead of a cleanly readable list of domain names
it now sees encrypted traffic to an IP address. It can no longer alter answers silently. And it is no longer the addressee
of DNS blocking orders, to the extent that the new provider is not subject to the same orders.

Here is what it does not achieve:

It does not make you anonymous. The new resolver now sees what your access provider saw before. You are exchanging one
observer for another, which is why you should pick one whose interests do not conflict with yours. It does not replace a
VPN or Tor. And it is not antivirus: a DNS filter only bites while a name is being resolved, and can be bypassed by a
direct IP connection.

Germany’s Federal Network Agency itself states that a critical point about DNS blocking is that such a block can easily be
circumvented. That applies to blocks you reject just as much as to protective filters you want."""

# ---------------------------------------------------------------------------
# Rechtlicher Rahmen in Deutschland. Neutral und belegt.
# ---------------------------------------------------------------------------

LEGAL_DE = """In Deutschland können Rechteinhaber Zugangsanbieter dazu verpflichten lassen, einzelne Domains zu sperren. Der Abschnitt
beschreibt die Rechtslage, er bewertet sie nicht.

Rechtsgrundlage ist § 8 des Digitale-Dienste-Gesetzes mit der amtlichen Überschrift „Anspruch auf Sperrung bei
Rechtsverletzung“. Der Bundesgerichtshof hat mit Urteil vom 13. Oktober 2022, Aktenzeichen I ZR 111/21, unter dem
Titel „DNS-Sperre“ entschieden, unter welchen Voraussetzungen Rechteinhaber einen Zugangsanbieter auf Sperrung in
Anspruch nehmen können. Das Gericht beschreibt die Maßnahme technisch so, dass die Zuordnung zwischen Domainname und
IP-Adresse auf dem DNS-Server des Zugangsanbieters verhindert wird.

Koordiniert werden diese Verfahren von der Clearingstelle Urheberrecht im Internet, kurz CUII. Sie beschreibt sich als
unabhängige Stelle, die von Internetzugangsanbietern und Rechteinhabern gegründet wurde. Zum Juli 2025 hat sie ihr
Verfahren umgestellt. Seither gilt der CUII-Verhaltenskodex 2.0, nach dem sich ein Rechteinhaber zunächst an ein
deutsches Gericht wendet, das den Sperranspruch prüft. Die CUII begründet den Wechsel damit, dass die Bundesnetzagentur
ihr mitgeteilt habe, sich künftig auf ihre Pflichtaufgaben konzentrieren zu wollen.

Die CUII stellt selbst klar, dass die gerichtliche Prüfung auf Freiwilligkeit beruht: „Das ist freiwillige
Selbstverpflichtung der CUII-Mitglieder. Denn eigentlich besteht kein Richtervorbehalt.“

Die Bundesnetzagentur grenzt ihre eigene Rolle deutlich ab: „Die Bundesnetzagentur ordnet keine Sperren im Internet an.“
Und: „Die Bundesnetzagentur kann auch weder DNS-Sperren anordnen noch durchsetzen.“ Sie prüft, ob eingerichtete Sperren
mit der Verordnung (EU) 2015/2120 über den Zugang zum offenen Internet vereinbar sind.

Zwei Punkte zur Genauigkeit, weil sie oft falsch wiedergegeben werden. Erstens betreffen diese Sperren die Resolver der
beteiligten Zugangsanbieter, nicht das Internet als solches. Wer einen anderen Resolver nutzt, ist von ihnen nur dann
erfasst, wenn dieser Anbieter denselben Anordnungen unterliegt. Quad9 zeigt, dass das vorkommt: Nach einem französischen
Urteil sperrt der Dienst weltweit. Zweitens ist der Umfang öffentlich nachvollziehbar: Die CUII veröffentlicht sowohl die
gerichtlichen Anordnungen als auch die älteren Empfehlungen ihres früheren Prüfausschusses.

Die Sperranordnungen richten sich an die Zugangsanbieter, nicht an deren Kundinnen und Kunden. Wer den Resolver wechselt,
ändert, wen er fragt. Ob eine konkrete Nutzung zulässig ist, richtet sich nach dem Inhalt, der aufgerufen wird, nicht nach
dem verwendeten DNS-Server. Diese
Seite ist eine technische Darstellung und keine Rechtsberatung."""

LEGAL_EN = """DNS blocking is a live issue in Germany, so it belongs on this page. This section describes the legal situation; it
does not evaluate it.

The legal basis is section 8 of the German Digital Services Act, headed “Claim to blocking in the event of an
infringement”. In a judgment of 13 October 2022, case number I ZR 111/21, titled “DNS-Sperre”, the Federal Court of
Justice decided under what conditions rights holders may require an access provider to block access to a site. The court describes the
measure technically as preventing the mapping between domain name and IP address on the access provider’s DNS server.

These proceedings are coordinated by the Clearing Body for Copyright on the Internet, known as CUII. It describes itself
as an independent body founded by internet access providers and rights holders. In July 2025 it changed its procedure.
The CUII code of conduct 2.0 has applied since then. Under it, a rights holder first turns to a German court, and the
court examines the blocking claim. CUII explains the change by saying that the Federal Network Agency told it the agency intends to
concentrate on its statutory duties in future.

CUII itself makes clear that judicial review rests on a voluntary basis, stating that it is a voluntary self-commitment of
CUII members and that no prior judicial authorisation is required by law.

The Federal Network Agency draws a sharp line around its own role, stating that it does not order any blocks on the
internet and can neither order nor enforce DNS blocks. It examines whether blocks already in place are compatible with
Regulation (EU) 2015/2120 on open internet access.

Two points for accuracy, because they are often misreported. First, these blocks affect the resolvers of the participating
access providers, not the internet as such. Anyone using a different resolver is affected by them only if that provider is
subject to the same orders. Quad9 shows that this happens: following a French ruling the service blocks worldwide. Second, the
scope is publicly traceable: CUII publishes both the court orders and the older recommendations of its former review
committee.

The blocking orders are addressed to the access providers, not to their customers. Changing your resolver changes whom you
ask. Whether a particular use is lawful depends on the content accessed, not on the DNS server used. This page is a technical description, not legal
advice."""

LEGAL_SOURCES = [
    ("https://cuii.info/", "Clearingstelle Urheberrecht im Internet (CUII)", "Clearingstelle Urheberrecht im Internet (CUII), the German copyright clearing body"),
    ("https://cuii.info/anordnungen/", "CUII: Gerichtliche Sperranordnungen und frühere Empfehlungen", "CUII: court blocking orders and earlier recommendations"),
    ("https://www.bundesnetzagentur.de/DE/Fachthemen/Digitales/Schutz/Netzneutralitaet/DNSsperren/start.html", "Bundesnetzagentur: Offenes Internet und Netzsperren", "Bundesnetzagentur (Federal Network Agency): open internet and network blocking"),
    ("https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2022/2022145.html", "Bundesgerichtshof, Pressemitteilung Nr. 145/2022 zum Urteil vom 13.10.2022, I ZR 111/21", "Federal Court of Justice, press release 145/2022 on the judgment of 13 October 2022, I ZR 111/21"),
    ("https://www.gesetze-im-internet.de/ddg/__8.html", "§ 8 Digitale-Dienste-Gesetz", "Section 8 of the German Digital Services Act (DDG)"),
]

# ---------------------------------------------------------------------------
# Auswahlkriterien
# ---------------------------------------------------------------------------

CRITERIA = [
    ("Wer haftet?", "Who is accountable?",
     "Ein eingetragener Verein, eine Stiftung oder eine Gesellschaft mit ladungsfähiger Anschrift ist überprüfbar. Ein anonymes Projekt ist es nicht. Das sagt nichts über die Redlichkeit, aber alles über die Durchsetzbarkeit von Zusagen.",
     "A registered association, a foundation or a company with a serviceable address can be checked. An anonymous project cannot. That says nothing about honesty, but everything about whether commitments can be enforced."),
    ("Wovon lebt der Dienst?", "How is the service funded?",
     "Kostenloses DNS kostet den Betreiber Geld. Wenn nicht erkennbar ist, wer dafür aufkommt, ist die Frage offen, womit der Dienst bezahlt wird. Spenden, Mitgliedsbeiträge und ein tragendes Hauptgeschäft sind nachvollziehbare Antworten.",
     "Free DNS costs the operator money. If it is not apparent who pays, the question of where the money comes from remains open. Donations, membership fees and a supporting core business are traceable answers."),
    ("Was steht wörtlich in der Datenschutzerklärung?", "What does the privacy policy say verbatim?",
     "„Wir respektieren Ihre Privatsphäre“ ist keine Zusage. „We do not log DNS queries“ mit benannten Ausnahmen und einer Speicherfrist ist eine. Eine Erklärung, die ihre eigenen Ausnahmen benennt, ist glaubwürdiger als eine ohne.",
     "“We respect your privacy” is not a commitment. “We do not log DNS queries”, with named exceptions and a retention period, is one. A policy that names its own exceptions is more credible than one without."),
    ("Wird gefiltert, und ist das abwählbar?", "Is there filtering, and can it be turned off?",
     "Ein Malware-Filter ist für die meisten Menschen ein Gewinn. Entscheidend ist, dass es eine ungefilterte Adresse desselben Betreibers gibt, damit die Entscheidung bei Ihnen bleibt.",
     "A malware filter is a benefit for most people. What matters is that the same operator offers an unfiltered address, so the decision stays with you."),
    ("Welche Jurisdiktion?", "Which jurisdiction?",
     "Der Sitz des Betreibers und der Standort der Server entscheiden darüber, welche Behörden welche Anordnungen treffen können. Beides kann auseinanderfallen und sollte getrennt betrachtet werden.",
     "The operator’s seat and the server location determine which authorities can issue which orders. The two can differ and should be considered separately."),
    ("Gibt es einen zweiten Server?", "Is there a second server?",
     "Ein einzelner Resolver ist ein einzelner Ausfallpunkt. Tragen Sie immer einen zweiten, unabhängigen Server ein, am besten von einem anderen Betreiber.",
     "A single resolver is a single point of failure. Always configure a second, independent server, preferably from a different operator."),
]

# ---------------------------------------------------------------------------
# Methode und FAQ
# ---------------------------------------------------------------------------

METHOD_DE = """Diese Seite behauptet nichts, was nicht belegt ist.

Alle Angaben zu Betreibern, Adressen, Endpunkten, Filterung und Protokollierung stammen aus den offiziellen Seiten,
Datenschutzerklärungen und Repositories der jeweiligen Dienste, aus öffentlichen Registern sowie aus den RFCs beim
RFC Editor. Alle Abrufe erfolgten am 6. September 2026.

Jede Angabe wurde zweimal erhoben: einmal beim Zusammentragen und einmal in einer getrennten Gegenprüfung, deren Auftrag
ausdrücklich lautete, die erste Fassung zu widerlegen. Dabei aufgedeckte Fehler wurden korrigiert oder gestrichen. Zwei
Beispiele, damit das nachvollziehbar bleibt: Die vielerorts genannte Adresse dns.digitalcourage.de ist dauerhaft
abgeschaltet, und dns0.eu existiert seit Oktober 2025 nicht mehr, steht aber weiterhin in gängigen Empfehlungslisten.

Wo eine Angabe nicht aus einer Primärquelle zu belegen war, steht sie nicht auf dieser Seite. Wo eine Aussage eine
Selbstauskunft des Anbieters ist, wird sie als solche gekennzeichnet. Keine der No-Log-Zusagen auf dieser Seite ist
unabhängig auditiert; das gilt für alle und ist deshalb bei jedem Dienst mitzudenken.

Zahlen zu Serverstandorten, Nutzerzahlen oder Geschwindigkeit sind bewusst zurückhaltend gehalten. Sie ändern sich
schneller, als eine statische Seite gepflegt werden kann.

Wer einen Fehler findet, möge ihn melden. Der Quelltext dieser Seite liegt offen, jede Aussage lässt sich bis zu ihrer
Quelle zurückverfolgen."""

METHOD_EN = """This page claims nothing that is not evidenced.

All statements about operators, addresses, endpoints, filtering and logging come from the official pages, privacy
policies and repositories of the respective services, from public registers, and from the RFCs at the RFC Editor. All
sources were retrieved on 6 September 2026.

Every statement was verified twice: once when compiling it and once in a separate adversarial check whose explicit brief
was to refute the first version. Errors uncovered that way were corrected or removed. Two examples, so this stays
verifiable: the widely cited address dns.digitalcourage.de has been permanently shut down, and dns0.eu has not existed
since October 2025 yet is still being recommended elsewhere.

Where a statement could not be evidenced from a primary source, it does not appear on this page. Where a statement is a
provider’s self-declaration, it is marked as such. Not one of the no-log commitments on this page is independently
audited. Keep that in mind for every service listed here.

Figures on server locations, user numbers or speed are deliberately kept sparse. They change faster than a static page
can be maintained.

If you find an error, please report it. The code behind this page is public, and every statement can be traced back to its
source."""

FAQ = [
    ("Macht mich ein anderer DNS-Server anonym?",
     "Does a different DNS server make me anonymous?",
     "Nein. Er verlagert die Sichtbarkeit vom Zugangsanbieter zum neuen Resolver. Die Ziel-IP-Adressen Ihrer Verbindungen und, ohne Encrypted Client Hello, der Servername im TLS-Handshake bleiben sichtbar. Anonymität ist ein anderes Problem und braucht andere Werkzeuge.",
     "No. It shifts visibility from your access provider to the new resolver. The destination IP addresses of your connections and, without Encrypted Client Hello, the server name in the TLS handshake remain visible. Anonymity is a different problem and needs different tools."),
    ("DNSSEC oder verschlüsseltes DNS, was brauche ich?",
     "DNSSEC or encrypted DNS, which do I need?",
     "Beides, denn sie lösen verschiedene Probleme. DNSSEC prüft, ob die Antwort echt ist. DoT, DoH und DoQ verbergen die Frage. RFC 4033 sagt zu DNSSEC ausdrücklich: „These extensions do not provide confidentiality.“",
     "Both, because they solve different problems. DNSSEC checks whether the answer is genuine. DoT, DoH and DoQ hide the question. RFC 4033 says of DNSSEC explicitly: “These extensions do not provide confidentiality.”"),
    ("Warum funktioniert die IP-Adresse von Digitale Gesellschaft, Artikel10 oder Applied Privacy nicht in meinem Router?",
     "Why does the IP address of Digitale Gesellschaft, Artikel10 or Applied Privacy not work in my router?",
     "Weil diese Dienste bewusst kein Klartext-DNS auf Port 53 anbieten. Die genannten Adressen antworten nur über DoT auf Port 853 oder DoH auf Port 443. Sie gehören in ein Feld für verschlüsseltes DNS, nicht in das gewöhnliche DNS-Feld.",
     "Because these services deliberately offer no plaintext DNS on port 53. The addresses given answer only over DoT on port 853 or DoH on port 443. They belong in a field for encrypted DNS, not in the ordinary DNS field."),
    ("Ist ein selbst betriebener Resolver privater?",
     "Is a self-hosted resolver more private?",
     "Teilweise. Bei echter Rekursion entfällt der zentrale Resolver, der alles sieht. Dafür laufen die Anfragen an Root-, TLD- und autoritative Server, und in einem sehr kleinen Netz sind sie leichter einer Person zuzuordnen. Der Gewinn liegt also in der Verteilung, nicht in der Unsichtbarkeit.",
     "Partly. With real recursion the central resolver that sees everything disappears. In exchange, queries go to root, TLD and authoritative servers, and on a very small network they are easier to attribute to one person. The gain lies in distribution, not in invisibility."),
    ("Reicht es, DoH im Browser einzuschalten?",
     "Is enabling DoH in the browser enough?",
     "Für den Browser ja, für das Gerät nein. Alles andere, vom E-Mail-Programm bis zum Betriebssystem-Update, nutzt weiterhin den systemweit eingestellten Resolver. Wer das ganze Gerät schützen will, stellt DNS im Betriebssystem oder im Router ein.",
     "For the browser yes, for the device no. Everything else, from the mail client to operating system updates, still uses the system-wide resolver. To protect the whole device, configure DNS in the operating system or the router."),
    ("Warum steht Mullvad hier als Warnung und nicht als Empfehlung?",
     "Why is Mullvad listed here as a warning rather than a recommendation?",
     "Weil der öffentliche verschlüsselte DNS-Dienst am 2. November 2026 abgeschaltet wird. Das hat Mullvad am 3. September 2026 selbst angekündigt. Eine Adresse zu empfehlen, die in wenigen Wochen nicht mehr antwortet, wäre keine Hilfe.",
     "Because the public encrypted DNS service will be shut down on 2 November 2026. Mullvad announced this itself on 3 September 2026. Recommending an address that will stop answering within weeks would be no help."),
]

# ---------------------------------------------------------------------------
# Glossar. Jede Definition ist an der einschlaegigen Norm geprueft.
# ---------------------------------------------------------------------------

GLOSSARY = [
    {
        "group": "basics",
        "term": "Stub-Resolver",
        "short": "Ein Resolver, der die Namensauflösung nicht selbst vollständig durchführen kann und die eigentliche Auflösung an einen rekursiven Resolver abgibt. Er sitzt typischerweise im Betriebssystem oder in der Anwendung und stellt nur die Anfrage.",
        "short_en": "A resolver that cannot perform all resolution itself and depends on a recursive resolver to undertake the actual resolution function. It typically lives in the operating system or the application and only issues the query.",
        "pitfall": "Häufig wird angenommen, der Stub-Resolver im Betriebssystem laufe selbst die Kette von den Root-Servern abwärts ab. Tatsächlich delegiert er die gesamte Auflösungsarbeit an einen rekursiven Resolver.",
        "pitfall_en": "People often assume the operating system stub resolver walks the delegation chain from the root servers itself. In fact it hands the entire resolution work to a recursive resolver.",
        "rfc": "RFC 9499, 1123",
    },
    {
        "group": "basics",
        "term": "Rekursiver Resolver",
        "short": "Ein Resolver im rekursiven Modus, der eine Anfrage entweder aus dem lokalen Cache beantwortet oder selbst weitere Server befragt, bis die endgültige Antwort vorliegt. In der Regel speichert er die erhaltenen Antworten im Cache zwischen.",
        "short_en": "A resolver that acts in recursive mode, either answering from a local cache or querying other servers until it has the final answer. In general it is expected to cache the answers it receives.",
        "pitfall": "Das Wort rekursiv beschreibt nur den Dienst gegenüber dem Client, nicht das Vorgehen nach außen. Gegenüber den autoritativen Servern arbeitet derselbe Resolver iterativ, er folgt also Verweisen Schritt für Schritt.",
        "pitfall_en": "The word recursive describes only the service offered to the client, not the outward behaviour. Toward the authoritative servers the same resolver works iteratively, following referrals step by step.",
        "rfc": "RFC 9499, 1034",
    },
    {
        "group": "basics",
        "term": "Autoritativer Nameserver",
        "short": "Ein Server, der den Inhalt einer DNS-Zone aus lokalem Wissen kennt und Anfragen zu dieser Zone ohne Rückfrage bei anderen Servern beantworten kann. Er setzt in solchen Antworten das AA-Bit im Header auf 1.",
        "short_en": "A server that knows the content of a DNS zone from local knowledge and can answer queries about that zone without needing to query other servers. It sets the AA flag in the response header to 1 for such answers.",
        "pitfall": "Nicht jede Antwort eines autoritativen Servers ist autoritativ: Verweise auf delegierte Kindzonen kommen mit AA-Bit 0. Außerdem kann ein Server autoritativ antworten, ohne dass die Elternzone ihm die Autorität delegiert hat.",
        "pitfall_en": "Not every answer from an authoritative server is authoritative: referrals to delegated child zones come with the AA bit set to 0. A server can also answer authoritatively without the parent zone having delegated authority to it.",
        "rfc": "RFC 9499, 2182",
    },
    {
        "group": "basics",
        "term": "Root-Server",
        "short": "Ein autoritativer Nameserver, der Anfragen zum Inhalt der Root-Zone beantwortet und damit den Einstiegspunkt in das Root-Server-System bildet. Die dreizehn Buchstabenidentitäten A bis M werden von zwölf unabhängigen Organisationen betrieben.",
        "short_en": "An authoritative name server that answers queries for the contents of the root zone and forms an entry point into the root server system. The thirteen letter identities A through M are operated by twelve independent organisations.",
        "pitfall": "Dreizehn Buchstaben bedeuten nicht dreizehn Maschinen: Am 2026-09-07 bestand das System laut root-servers.org aus 2005 betriebsbereiten Instanzen. Der Begriff Mirror ist in diesem Zusammenhang veraltet, korrekt heißt es Instanz.",
        "pitfall_en": "Thirteen letters do not mean thirteen machines: on 2026-09-07 root-servers.org reported 2005 operational instances. The term mirror is deprecated here, the correct word is instance.",
        "rfc": "RFC 9499, 8109",
    },
    {
        "group": "basics",
        "term": "TLD (Top-Level Domain)",
        "short": "Eine Zone, die genau eine Ebene unterhalb der Root liegt, zum Beispiel com oder jp. Die meisten TLDs sind delegierungszentrierte Zonen, also Zonen, die überwiegend aus Delegierungen an Kindzonen bestehen.",
        "short_en": "A zone that is one layer below the root, such as com or jp. Most TLDs are delegation-centric zones, that is zones consisting mostly of delegations to child zones.",
        "pitfall": "Aus Sicht des DNS-Protokolls ist eine TLD nichts Besonderes, sie ist eine Zone wie jede andere. Die Unterscheidungen in ccTLD, gTLD und weitere sind reine Policy-Kategorien.",
        "pitfall_en": "From the point of view of the DNS protocol a TLD is nothing special, it is a zone like any other. The split into ccTLD, gTLD and others is purely a matter of policy.",
        "rfc": "RFC 9499",
    },
    {
        "group": "basics",
        "term": "Anycast",
        "short": "Die Praxis, eine bestimmte Dienstadresse an mehreren getrennten, autonomen Standorten verfügbar zu machen, sodass gesendete Datagramme zu einem dieser Standorte geroutet werden. Jeder dieser Standorte heißt Instanz.",
        "short_en": "The practice of making a particular service address available in multiple, discrete, autonomous locations, such that datagrams sent are routed to one of several available locations. Each such location is called an instance.",
        "pitfall": "Anycast ist kein Lastverteiler und garantiert nicht die geografisch nächste Instanz, denn das Routing entscheidet nach Topologie, nicht nach Entfernung. Unter Anycast-Instanzen gibt es keine Hierarchie, jede hat dieselbe Autorität.",
        "pitfall_en": "Anycast is not a load balancer and does not guarantee the geographically closest instance, since routing decides by topology rather than distance. There is no hierarchy among anycast instances, each has the same level of authority.",
        "rfc": "RFC 4786, 9499",
    },
    {
        "group": "basics",
        "term": "Unicast",
        "short": "Eine Adresse, die genau eine Schnittstelle bezeichnet; ein an eine Unicast-Adresse gesendetes Paket wird an genau diese Schnittstelle zugestellt. Im DNS-Kontext steht Unicast für den Fall, dass eine Serveradresse an nur einem Standort angekündigt wird.",
        "short_en": "An identifier for a single interface; a packet sent to a unicast address is delivered to the interface identified by that address. In a DNS context unicast means a server address announced from only one location.",
        "pitfall": "Unicast identifiziert eine Schnittstelle, nicht einen Host; ein Host kann mehrere Unicast-Adressen tragen. Die in RFC 4291 zitierte Definition stammt aus der IPv6-Adressarchitektur, das Konzept ist aber nicht auf IPv6 beschränkt.",
        "pitfall_en": "Unicast identifies an interface, not a host; one host can carry several unicast addresses. The definition quoted from RFC 4291 comes from the IPv6 addressing architecture, but the concept is not limited to IPv6.",
        "rfc": "RFC 4291",
    },
    {
        "group": "basics",
        "term": "Cache",
        "short": "Eine Struktur, die die Ergebnisse früherer Antworten speichert, damit gleiche Anfragen nicht erneut entfernt aufgelöst werden müssen. Resolver sind dafür verantwortlich, alte Einträge nach Ablauf der TTL zu verwerfen.",
        "short_en": "A structure which stores the results from previous responses so that identical requests need not be resolved remotely again. Resolvers are responsible for discarding old RRs whose TTL has expired.",
        "pitfall": "Ein Cache hält Einträge nicht zwingend bis zum Ablauf der TTL; laut RFC 9499 kann ein RRset vorher aus dem Cache entfernt werden. Auch negative Antworten werden zwischengespeichert, das ist Negative Caching nach RFC 2308.",
        "pitfall_en": "A cache does not necessarily keep entries until the TTL expires; RFC 9499 notes an RRset can be flushed from the cache before the end of the TTL interval. Negative answers are cached too, which is negative caching per RFC 2308.",
        "rfc": "RFC 1034, 1123",
    },
    {
        "group": "basics",
        "term": "TTL (Time to Live)",
        "short": "Die maximale Lebensdauer eines Resource Record, also das Zeitintervall in Sekunden, das der Record zwischengespeichert werden darf, bevor die Quelle erneut befragt werden sollte. Der Wert ist eine vorzeichenlose Zahl von 0 bis 2147483647.",
        "short_en": "The maximum time to live of a resource record, that is the time interval in seconds the record may be cached before the source of the information should again be consulted. The value is an unsigned number from 0 to 2147483647.",
        "pitfall": "Die TTL ist eine Obergrenze und keine Garantie: Ein Cache-Betreiber kann sie aus betrieblichen Gründen verkürzen, und ein RRset kann vorzeitig verworfen werden. Alle Records eines RRset müssen dieselbe TTL tragen (RFC 2181, Abschnitt 5.2).",
        "pitfall_en": "The TTL is an upper bound, not a guarantee: a cache operator may shorten it for operational reasons and an RRset can be flushed early. All records in an RRset are required to carry the same TTL (RFC 2181, Section 5.2).",
        "rfc": "RFC 9499, 1035, 2181",
    },
    {
        "group": "basics",
        "term": "NXDOMAIN",
        "short": "Der DNS-Antwortcode 3 (Name Error), der besagt, dass der in der Anfrage genannte Domainname nicht existiert. Da Namen einen Baum bilden, bedeutet das Nichtexistieren eines Knotens auch das Nichtexistieren des gesamten darunter liegenden Teilbaums.",
        "short_en": "DNS response code 3 (Name Error), signifying that the domain name referenced in the query does not exist. Since names form a tree, nonexistence of a node implies nonexistence of the entire subtree rooted at that node.",
        "pitfall": "NXDOMAIN heißt, dass der Name selbst nicht existiert, nicht dass nur der abgefragte Record-Typ fehlt; letzteres ist eine NODATA-Antwort mit RCODE 0 und leerer Answer-Section. Ebenfalls falsch ist die Annahme, unterhalb eines NXDOMAIN-Namens könnten noch Namen existieren, denn RFC 8020 schließt das aus.",
        "pitfall_en": "NXDOMAIN means the name itself does not exist, not merely that the queried record type is missing; the latter is a NODATA answer with RCODE 0 and an empty answer section. It is likewise wrong to assume names can still exist beneath an NXDOMAIN name, since RFC 8020 rules that out.",
        "rfc": "RFC 1035, 2308, 8020, 9499",
    },
    {
        "group": "basics",
        "term": "Resource Record (RR)",
        "short": "Der einzelne Dateneintrag des DNS, bestehend aus Owner-Name, Typ, Klasse, TTL und RDATA; die Menge der Informationen zu einem Namen setzt sich aus solchen Records zusammen. Records mit gleichem Owner-Name, gleicher Klasse und gleichem Typ bilden ein RRset.",
        "short_en": "The individual DNS data entry, consisting of owner name, type, class, TTL and RDATA; the information associated with a name is composed of such records. Records with the same owner name, class and type form an RRset.",
        "pitfall": "Die Reihenfolge der Records in einer Menge ist ohne Bedeutung und muss von Servern und Resolvern nicht erhalten bleiben. Ein RRset wird zudem immer als Ganzes behandelt, und alle seine Records müssen dieselbe TTL haben.",
        "pitfall_en": "The order of RRs in a set is not significant and need not be preserved by name servers or resolvers. An RRset is also always handled as a whole, and all of its records must carry the same TTL.",
        "rfc": "RFC 1034, 1035, 2181, 9499",
    },
    {
        "group": "protocols",
        "term": "DNSSEC",
        "short": "DNSSEC ist eine Erweiterung des DNS, die per digitaler Signatur die Herkunft und die Unversehrtheit von DNS-Daten nachweisbar macht, spezifiziert in RFC 4033, RFC 4034 und RFC 4035. RFC 9364 (BCP 237) erklärt den Einsatz von DNSSEC zur Ursprungsauthentifizierung von DNS-Daten zur Best Current Practice.",
        "short_en": "DNSSEC is a set of DNS extensions that add data origin authentication and data integrity to DNS answers through digital signatures, specified in RFC 4033, RFC 4034 and RFC 4035. RFC 9364 (BCP 237) states that using DNSSEC for origin authentication of DNS data is the best current practice.",
        "pitfall": "DNSSEC verschlüsselt nichts. RFC 4033 Abschnitt 3 stellt ausdrücklich fest: „These extensions do not provide confidentiality.“, das heißt Anfragen und Antworten bleiben für jeden auf dem Weg mitlesbar, DNSSEC macht sie nur fälschungssicher.",
        "pitfall_en": "DNSSEC does not encrypt anything. RFC 4033 Section 3 states plainly „These extensions do not provide confidentiality.“, so queries and answers remain readable on the wire; DNSSEC only makes them tamper evident.",
        "rfc": "RFC 4033, 4034, 4035, 9364",
    },
    {
        "group": "protocols",
        "term": "DNSSEC-Validierung",
        "short": "DNSSEC-Validierung ist der Vorgang, bei dem ein Resolver die Signaturen einer Antwort kryptografisch prüft und dazu eine Authentifizierungskette aus DNSKEY- und DS-Datensätzen bis zu einem konfigurierten Trust Anchor aufbaut. Das Protokollverhalten validierender Resolver ist in RFC 4035 festgelegt.",
        "short_en": "DNSSEC validation is the process in which a resolver cryptographically verifies the signatures on an answer by building an authentication chain of DNSKEY and DS RRsets up to a configured trust anchor. The protocol behaviour of validating resolvers is defined in RFC 4035.",
        "pitfall": "Validierung schützt nur Zonen, die auch tatsächlich signiert sind. Für unsignierte Zonen kann ein Resolver nur beweisen, dass keine Signatur existiert, nicht dass die Antwort echt ist.",
        "pitfall_en": "validation only protects zones that are actually signed. For unsigned zones a resolver can only prove that no signature exists, not that the answer is genuine.",
        "rfc": "RFC 4035, 6840",
    },
    {
        "group": "protocols",
        "term": "AD-Flag",
        "short": "Das AD-Bit (Authentic Data) im DNS-Header wird von einem sicherheitsbewussten rekursiven Nameserver gesetzt, wenn er alle RRsets in Answer- und Authority-Abschnitt als authentisch validiert hat. RFC 4035 Abschnitt 3.2.3 verbietet das Setzen des Bits, solange nicht alle betroffenen RRsets als authentisch gelten.",
        "short_en": "The AD (Authentic Data) bit in the DNS header is set by a security-aware recursive name server when it has validated all RRsets in the Answer and Authority sections as authentic. RFC 4035 Section 3.2.3 forbids setting the bit unless all relevant RRsets are considered authentic.",
        "pitfall": "Ein gesetztes AD-Bit ist kein Beweis. RFC 4033 Abschnitt 7 nennt es nur einen Hinweis und verlangt, dass der Stub-Resolver „must trust both the recursive name servers in question and the communication channels between itself and those name servers“, denn auf einem ungesicherten Kanal kann jeder Angreifer das Bit setzen.",
        "pitfall_en": "a set AD bit is not proof. RFC 4033 Section 7 calls it only a hint and requires that the stub resolver „must trust both the recursive name servers in question and the communication channels between itself and those name servers“, because on an unsecured channel any attacker can set the bit.",
        "rfc": "RFC 4035, 6840, 4033",
    },
    {
        "group": "protocols",
        "term": "Trust Anchor",
        "short": "Ein Trust Anchor ist laut RFC 4033 „A configured DNSKEY RR or DS RR hash of a DNSKEY RR“, den ein validierender Resolver als Startpunkt der Authentifizierungskette verwendet. RFC 5011 beschreibt, wie Trust Anchors automatisiert und authentifiziert ausgetauscht werden können.",
        "short_en": "A trust anchor is, per RFC 4033, „A configured DNSKEY RR or DS RR hash of a DNSKEY RR“ that a validating resolver uses as the starting point for building the authentication chain. RFC 5011 describes how trust anchors can be updated automatically and authenticated.",
        "pitfall": "Ein Trust Anchor ist kein X.509-Zertifikat und stammt nicht aus dem Browser- oder Betriebssystem-Zertifikatsspeicher. In der Praxis ist meist genau ein Anker konfiguriert, nämlich der der DNS-Root-Zone.",
        "pitfall_en": "a trust anchor is not an X.509 certificate and does not come from the browser or operating system certificate store. In practice usually exactly one anchor is configured, that of the DNS root zone.",
        "rfc": "RFC 4033, 5011",
    },
    {
        "group": "protocols",
        "term": "Root Zone KSK",
        "short": "Der Root Zone Key Signing Key ist der von der IANA verwaltete DNSSEC-Schlüssel, mit dem der Schlüsselsatz der DNS-Root-Zone signiert wird und der als Vertrauensanker fast aller validierenden Resolver dient. Aktiv signierend ist KSK-2017 mit Key Tag 20326 („Signing since 2018-10-11“); der Nachfolger KSK-2024 mit Key Tag 38696 steht laut IANA in „Pre-Publication“ und soll ab dem 11. Oktober 2026 signieren.",
        "short_en": "The Root Zone Key Signing Key is the IANA managed DNSSEC key that signs the key set of the DNS root zone and serves as the trust anchor for nearly all validating resolvers. The actively signing key is KSK-2017 with key tag 20326 („Signing since 2018-10-11“); its successor KSK-2024 with key tag 38696 is listed by IANA as „Pre-Publication“ and is scheduled to sign the zone from 11 October 2026.",
        "pitfall": "Der KSK signiert nicht die einzelnen Root-Einträge, sondern nur den DNSKEY-Satz der Root-Zone; die eigentlichen Daten signiert der Zone Signing Key. Stand 2026-09-07 hat der Rollover auf KSK-2024 noch nicht stattgefunden.",
        "pitfall_en": "the KSK does not sign individual root records, only the root zone DNSKEY RRset; the actual data is signed by the Zone Signing Key. As of 2026-09-07 the rollover to KSK-2024 has not yet taken place.",
        "rfc": "RFC 5011, 4034",
    },
    {
        "group": "protocols",
        "term": "DoT",
        "short": "DNS over TLS (DoT) transportiert DNS-Nachrichten in einer TLS-Sitzung über den fest zugewiesenen Port 853 und verhindert damit Mitlesen und Manipulation auf dem Weg. RFC 8310 ergänzt zwei Nutzungsprofile, Strict Privacy mit zwingender Serverauthentifizierung und Opportunistic Privacy ohne diese Garantie.",
        "short_en": "DNS over TLS (DoT) carries DNS messages inside a TLS session on the dedicated port 853, preventing eavesdropping and on-path tampering. RFC 8310 adds two usage profiles, Strict Privacy with mandatory server authentication and Opportunistic Privacy without that guarantee.",
        "pitfall": "DoT im opportunistischen Profil authentifiziert den Server nicht und schützt daher nicht gegen einen aktiven Angreifer. Nur das Strict-Privacy-Profil nach RFC 8310 verweigert die Auflösung, wenn Verschlüsselung und Authentifizierung nicht zustande kommen.",
        "pitfall_en": "DoT in the opportunistic profile does not authenticate the server and therefore does not protect against an active attacker. Only the Strict Privacy profile of RFC 8310 refuses to resolve when encryption and authentication cannot be established.",
        "rfc": "RFC 7858, 8310",
    },
    {
        "group": "protocols",
        "term": "DoH",
        "short": "DNS over HTTPS (DoH) bildet jedes DNS-Anfrage-Antwort-Paar auf einen HTTP-Austausch über HTTPS ab, sodass DNS-Verkehr verschlüsselt und von anderem HTTPS-Verkehr kaum unterscheidbar ist. Der Medientyp ist application/dns-message, üblich ist der Pfad-Template-Endpunkt eines konfigurierten DoH-Servers.",
        "short_en": "DNS over HTTPS (DoH) maps each DNS query and response pair into an HTTP exchange over HTTPS, so DNS traffic is encrypted and hard to distinguish from other HTTPS traffic. The media type is application/dns-message, addressed via the URI template of a configured DoH server.",
        "pitfall": "DoH verbirgt die besuchte Seite nicht vollständig. Erstens sieht der DoH-Betreiber weiterhin alle Anfragen im Klartext und kann sie laut RFC 8484 Abschnitt 8.2 zusätzlich über HTTP-Cookies, Header-Fingerprinting und IP-Adresse korrelieren; zweitens verrät die anschließende Verbindung selbst das Ziel, denn nach RFC 8744 wird „The SNI extension ... carried in cleartext in the TLS 'ClientHello' message“ und die Server-IP bleibt sichtbar.",
        "pitfall_en": "DoH does not fully hide which site you visit. First, the DoH operator still sees every query in the clear and can correlate it via HTTP cookies, header fingerprinting and IP address (RFC 8484 Section 8.2); second, the subsequent connection itself reveals the destination, since per RFC 8744 „The SNI extension is carried in cleartext in the TLS 'ClientHello' message“ and the server IP address remains visible.",
        "rfc": "RFC 8484",
    },
    {
        "group": "protocols",
        "term": "DoQ",
        "short": "DNS over QUIC (DoQ) überträgt DNS über dedizierte QUIC-Verbindungen auf UDP-Port 853 mit dem ALPN-Token „doq“ und bietet ähnliche Vertraulichkeit wie DoT ohne das Head-of-Line-Blocking von TCP. RFC 9250 beschreibt DoQ als Allzwecktransport für Stub-zu-Resolver, Resolver-zu-autoritativ und Zonentransfer.",
        "short_en": "DNS over QUIC (DoQ) carries DNS over dedicated QUIC connections on UDP port 853 with the ALPN token „doq“, offering confidentiality similar to DoT without TCP head of line blocking. RFC 9250 describes DoQ as a general purpose transport for stub to recursive, recursive to authoritative and zone transfer.",
        "pitfall": "DoQ auf UDP-Port 853 ist nicht dasselbe wie DoT, das TCP-Port 853 nutzt, und es ist auch nicht DNS over HTTP/3. Beide Seiten müssen DoQ ausdrücklich per ALPN aushandeln.",
        "pitfall_en": "DoQ on UDP port 853 is not the same as DoT, which uses TCP port 853, and it is not DNS over HTTP/3 either. Both endpoints must explicitly negotiate DoQ via ALPN.",
        "rfc": "RFC 9250",
    },
    {
        "group": "protocols",
        "term": "DNSCrypt",
        "short": "DNSCrypt ist ein herstelleroffenes, aber nicht von der IETF standardisiertes Protokoll, das laut dnscrypt.info „encrypts, authenticates and optionally anonymizes communications between your DNS client and resolver“. Version 2 der Spezifikation nutzt die Konstruktion X25519-XChaCha20Poly1305 sowie Ed25519 für die Signatur der Resolver-Zertifikate.",
        "short_en": "DNSCrypt is an open but non IETF protocol that, per dnscrypt.info, „encrypts, authenticates and optionally anonymizes communications between your DNS client and resolver“. Version 2 of the specification uses the X25519-XChaCha20Poly1305 construction and Ed25519 for signing resolver certificates.",
        "pitfall": "DNSCrypt ist kein RFC und kein IETF-Standard, sondern liegt nur als individueller Internet-Draft und als eigene Protokollspezifikation vor. Es ist außerdem nicht mit DNSSEC verwandt, denn es sichert den Transportweg, nicht die Zonendaten.",
        "pitfall_en": "DNSCrypt is not an RFC and not an IETF standard; it exists only as an individual Internet-Draft and its own protocol specification. It is also unrelated to DNSSEC, since it secures the transport path rather than the zone data.",
        "rfc": None,
    },
    {
        "group": "protocols",
        "term": "Oblivious DoH",
        "short": "Oblivious DNS over HTTPS (ODoH) schiebt einen Proxy zwischen Client und DoH-Target, sodass der Proxy die IP-Adresse des Clients kennt, aber nicht den Inhalt, und das Target den Inhalt entschlüsselt, aber nur die Proxy-IP sieht. Das Verfahren ist in RFC 9230 als Experimental veröffentlicht.",
        "short_en": "Oblivious DNS over HTTPS (ODoH) inserts a proxy between client and DoH target, so the proxy knows the client IP address but not the content, while the target decrypts the content but only sees the proxy IP. The mechanism is published as Experimental in RFC 9230.",
        "pitfall": "Der Schutz hängt daran, dass Proxy und Target nicht zusammenarbeiten oder demselben Betreiber gehören. Kolludieren beide, ist die Trennung von Identität und Inhalt aufgehoben.",
        "pitfall_en": "the protection depends on proxy and target not colluding or belonging to the same operator. If they collude, the separation of identity and content collapses.",
        "rfc": "RFC 9230",
    },
    {
        "group": "protocols",
        "term": "EDNS(0)",
        "short": "EDNS(0) erweitert das DNS-Drahtformat rückwärtskompatibel über ein OPT-Pseudo-RR (Typ 41) im Additional-Abschnitt, das größere UDP-Nachrichten als 512 Byte, zusätzliche Flag-Bits und einen erweiterten RCODE-Bereich ermöglicht. Das OPT-Record trägt keine Zonendaten, sondern ausschließlich Steuerinformation.",
        "short_en": "EDNS(0) extends the DNS wire format in a backward compatible way through an OPT pseudo RR (type 41) in the additional section, enabling UDP messages larger than 512 bytes, extra flag bits and an extended RCODE space. The OPT record carries no DNS data, only control information.",
        "pitfall": "Die vom Client angegebene UDP-Payload-Größe ist nur eine Angabe der eigenen Empfangsfähigkeit, keine Garantie, dass Pfad-MTU und Firewalls Pakete dieser Größe durchlassen. EDNS(0) ist außerdem kein Sicherheitsmechanismus, sondern nur der Trägermechanismus für Optionen wie Padding, ECS oder DNS Cookies.",
        "pitfall_en": "the UDP payload size a client advertises only states its own receive capability; it does not guarantee that path MTU and firewalls will pass packets of that size. EDNS(0) is also not a security mechanism, only the carrier for options such as Padding, ECS or DNS Cookies.",
        "rfc": "RFC 6891, 2671, 2673",
    },
    {
        "group": "protocols",
        "term": "EDNS Client Subnet",
        "short": "EDNS Client Subnet (ECS) ist eine EDNS(0)-Option, mit der ein Resolver einen gekürzten Teil des Client-Netzpräfixes an autoritative Server weiterreicht, damit diese geografisch passende Antworten liefern und der Cache-Gültigkeitsbereich bekannt wird. RFC 7871 ist Informational und beschreibt ein bereits im Einsatz befindliches Verfahren.",
        "short_en": "EDNS Client Subnet (ECS) is an EDNS(0) option with which a resolver passes a truncated part of the client network prefix to authoritative servers so they can return geographically appropriate answers and signal the cache scope. RFC 7871 is Informational and documents a mechanism already in active use.",
        "pitfall": "ECS untergräbt einen Teil des Datenschutzgewinns von verschlüsseltem DNS, weil Netzinformationen des Nutzers an jeden beteiligten autoritativen Server weitergereicht werden. RFC 7871 empfiehlt daher ausdrücklich, die Option in Nameserver-Software standardmäßig zu deaktivieren.",
        "pitfall_en": "ECS undermines part of the privacy gain of encrypted DNS, because the user network information is passed to every authoritative server involved. RFC 7871 therefore explicitly recommends that the option be turned off by default in nameserver software.",
        "rfc": "RFC 7871",
    },
    {
        "group": "protocols",
        "term": "QNAME-Minimierung",
        "short": "Bei der QNAME-Minimierung sendet ein Resolver einem autoritativen Server nicht mehr den vollständigen Namen und Typ, sondern nur den um ein Label längeren Teil des Namens, für den dieser Server zuständig ist. RFC 9156 ist Standards Track und ersetzt RFC 7816.",
        "short_en": "With QNAME minimisation a resolver no longer sends the full original QNAME and QTYPE to an upstream authoritative server, but only the name stripped to one label more than the longest name for which that server is known to be authoritative. RFC 9156 is Standards Track and obsoletes RFC 7816.",
        "pitfall": "QNAME-Minimierung schützt nur gegenüber den vorgelagerten autoritativen Servern wie den Root- und TLD-Servern. Der eigene rekursive Resolver sieht weiterhin den vollständigen angefragten Namen.",
        "pitfall_en": "QNAME minimisation only protects against upstream authoritative servers such as the root and TLD servers. Your own recursive resolver still sees the full name being queried.",
        "rfc": "RFC 9156, 7816",
    },
    {
        "group": "protocols",
        "term": "Padding",
        "short": "Die EDNS(0)-Padding-Option (Optionscode 12) erlaubt es Client und Server, DNS-Nachrichten um eine variable Zahl von Oktetten aufzufüllen, um Rückschlüsse aus der Nachrichtenlänge zu erschweren. RFC 8467 empfiehlt experimentell Blocklängen-Padding auf ein Vielfaches von 128 Oktetten für Anfragen und 468 Oktetten für Antworten.",
        "short_en": "The EDNS(0) Padding option (option code 12) lets clients and servers pad DNS messages by a variable number of octets so that message length reveals less. RFC 8467 recommends, experimentally, block length padding to a multiple of 128 octets for queries and 468 octets for responses.",
        "pitfall": "Padding ist nur sinnvoll innerhalb eines verschlüsselten Transports wie DoT, DoH oder DoQ. Auf unverschlüsseltem DNS bringt es keinen Datenschutzgewinn, weil der Inhalt ohnehin lesbar ist.",
        "pitfall_en": "padding is only useful inside an encrypted transport such as DoT, DoH or DoQ. On cleartext DNS it yields no privacy gain, because the content is readable anyway.",
        "rfc": "RFC 7830, 8467",
    },
    {
        "group": "protocols",
        "term": "Encrypted Client Hello",
        "short": "Encrypted Client Hello (ECH) ist eine TLS-Erweiterung, die das ClientHello unter einem öffentlichen Serverschlüssel verschlüsselt und damit sensible Felder wie SNI und die ALPN-Liste verbirgt. Die dafür nötige Konfiguration wird üblicherweise über den DNS-Ressourcendatensatz HTTPS/SVCB bezogen.",
        "short_en": "Encrypted Client Hello (ECH) is a TLS extension that encrypts the ClientHello under a server public key, hiding sensitive fields such as the SNI and the ALPN list. The required configuration is normally obtained through the HTTPS/SVCB DNS resource record.",
        "pitfall": "ECH allein verbirgt das Ziel nicht. RFC 9849 stellt fest: „ECH is not in itself sufficient to protect the identity of the server. The target domain may also be visible through other channels, such as plaintext client DNS queries or visible server IP addresses.“",
        "pitfall_en": "ECH alone does not hide the destination. RFC 9849 states: „ECH is not in itself sufficient to protect the identity of the server. The target domain may also be visible through other channels, such as plaintext client DNS queries or visible server IP addresses.“",
        "rfc": "RFC 9849, 9848",
    },
    {
        "group": "protocols",
        "term": "Server Name Indication",
        "short": "Server Name Indication (SNI) ist die TLS-Erweiterung, mit der ein Client dem Server im Handshake mitteilt, welchen Hostnamen er kontaktieren will, damit ein Server mehrere virtuelle Hosts unter einer IP-Adresse bedienen kann. Sie ist in RFC 6066 Abschnitt 3 definiert.",
        "short_en": "Server Name Indication (SNI) is the TLS extension by which a client tells the server, during the handshake, which host name it wants to reach, so that one server can host multiple virtual servers on a single IP address. It is defined in RFC 6066 Section 3.",
        "pitfall": "Ohne ECH wird der Hostname im SNI im Klartext übertragen, obwohl die Verbindung als HTTPS gilt. RFC 8744 hält fest, dass Überwachung sich zunehmend genau auf „the cleartext SNI“ stützt, um zu erkennen, welche Dienste ein Nutzer aufruft.",
        "pitfall_en": "without ECH the host name in the SNI travels in the clear even though the connection counts as HTTPS. RFC 8744 notes that monitoring increasingly relies on exactly „the cleartext SNI“ to identify which services a user accesses.",
        "rfc": "RFC 6066, 8744",
    },
    {
        "group": "protocols",
        "term": "DNS-Sinkhole",
        "short": "Ein DNS-Sinkhole ist ein Resolver, der Anfragen für unerwünschte Namen bewusst nicht wahrheitsgemäß beantwortet, sondern etwa NXDOMAIN, NODATA oder eine umgeleitete Adresse liefert, um Verbindungen zu Schadinfrastruktur oder Werbe- und Trackingdomains zu unterbinden. In BIND 9 wird dies über Response Policy Zones umgesetzt, die die ISC-Dokumentation als „a form of DNS firewall“ beschreibt.",
        "short_en": "A DNS sinkhole is a resolver that deliberately does not answer queries for unwanted names truthfully, returning for example NXDOMAIN, NODATA or a redirected address in order to block connections to malicious infrastructure or ad and tracking domains. In BIND 9 this is implemented through Response Policy Zones, which the ISC documentation describes as „a form of DNS firewall“.",
        "pitfall": "Ein Sinkhole blockiert nur die Namensauflösung, nicht die Verbindung selbst. Wer die IP-Adresse direkt kennt oder einen eigenen verschlüsselten Resolver im Gerät verwendet, umgeht das Sinkhole vollständig; außerdem kollidiert eine gefälschte Antwort mit DNSSEC-Validierung.",
        "pitfall_en": "a sinkhole only blocks name resolution, not the connection itself. Anyone who knows the IP address directly or uses their own encrypted resolver in the device bypasses the sinkhole entirely; a synthesized answer also conflicts with DNSSEC validation.",
        "rfc": None,
    },
    {
        "group": "protocols",
        "term": "Forwarder",
        "short": "Ein Forwarder ist nach RFC 9499 „A nameserver used to resolve queries instead of directly using the authoritative nameserver chain“; Forwarding ist der Vorgang, bei dem ein Server eine Anfrage mit gesetztem RD-Bit an einen anderen Server zur Auflösung weitergibt. RFC 9499 ist BCP 219 und die aktuelle DNS-Terminologie.",
        "short_en": "Per RFC 9499 a forwarder is „A nameserver used to resolve queries instead of directly using the authoritative nameserver chain“; forwarding is „The process of one server sending a DNS query with the RD bit set to 1 to another server to resolve that query“. RFC 9499 is BCP 219 and the current DNS terminology document.",
        "pitfall": "Forwarding ist nicht dasselbe wie blindes Weiterreichen von Paketen, sondern eine Resolver-Funktion mit eigenem Cache. Wer einen Forwarder einsetzt, verlagert damit auch die Vertrauensfrage und die Sichtbarkeit aller Anfragen auf den Upstream-Betreiber.",
        "pitfall_en": "forwarding is not blind relaying of packets but a resolver function with its own cache. Using a forwarder also shifts the trust question and the visibility of all queries to the upstream operator.",
        "rfc": "RFC 9499, 2308",
    },
    {
        "group": "protocols",
        "term": "DNS-Rebinding-Schutz",
        "short": "DNS-Rebinding-Schutz filtert Antworten aus öffentlichen Zonen heraus, die auf private oder lokale IP-Adressbereiche zeigen, damit ein Angreifer den Browser eines Nutzers nicht als Proxy in dessen internes Netz missbrauchen kann. Unbound setzt dies mit der Option private-address um, die passende A-, AAAA-, SVCB- und HTTPS-Einträge aus Antworten entfernt.",
        "short_en": "DNS rebinding protection filters out answers from public zones that point into private or local IP address ranges, so an attacker cannot turn a user browser into a proxy into the internal network. Unbound implements this with the private-address option, which removes matching A, AAAA, SVCB and HTTPS records from answers.",
        "pitfall": "Der Schutz greift nur für Namen aus öffentlichen Zonen und kann legitime Anwendungsfälle brechen, etwa Split-Horizon-Setups oder Dienste wie ACME-Validierung, die absichtlich private Adressen veröffentlichen. Dafür sieht Unbound ausdrücklich Ausnahmen über private-domain vor.",
        "pitfall_en": "the protection applies only to names in public zones and can break legitimate cases such as split horizon setups or services that deliberately publish private addresses. Unbound therefore provides explicit exemptions via private-domain.",
        "rfc": None,
    },
]

# ---------------------------------------------------------------------------
# Selbst pruefen. Jeder Befehl wurde am 2026-09-07 ausgefuehrt, die
# beschriebenen Ausgaben sind beobachtet und nicht angenommen.
# ---------------------------------------------------------------------------

CHECK_GROUPS = [
    ("dnssec", "Validiert mein Resolver DNSSEC?", "Does my resolver validate DNSSEC?",
     """Die Frage lässt sich in drei Befehlen beantworten, und zwar zweifelsfrei. Wichtig ist, den Resolver direkt zu
befragen, also mit <code>@</code> und seiner Adresse. Fragt man ohne <code>@</code>, antwortet der lokale Stub des
Betriebssystems, und der verschluckt das entscheidende Merkmal oft.""",
     """Three commands answer this question, and they answer it beyond doubt. What matters is querying the resolver
directly, using <code>@</code> and its address. Without <code>@</code> you are asking the operating system's local stub,
which often swallows the decisive detail."""),
    ("identity", "Welchen Resolver benutze ich wirklich?", "Which resolver am I actually using?",
     """Eingetragen ist eine Sache, benutzt eine andere. Router, VPN-Software, Browser mit eigenem DoH und der
Systemdienst greifen alle ein. Diese Befehle zeigen, wer am Ende wirklich antwortet und welchen Teil Ihrer Adresse er
dabei weitergibt.""",
     """What is configured and what is used are two different things. Routers, VPN software, browsers with their own DoH
and the system service all interfere. These commands show who really answers in the end, and which part of your address
they pass on."""),
    ("encrypted", "Kommt die Antwort wirklich verschlüsselt?", "Is the answer really encrypted?",
     """Eine verschlüsselte Verbindung allein sagt nichts, solange niemand prüft, wer am anderen Ende sitzt. Genau das
ist der häufigste Fehler in Anleitungen: Sie zeigen einen erfolgreichen Handschlag und nennen ihn Sicherheit.""",
     """An encrypted connection on its own means nothing as long as nobody checks who is at the other end. That is the
most common mistake in guides: they show a successful handshake and call it security."""),
    ("metadata", "Was verrät meine Anfrage noch?", "What else does my query reveal?",
     """Zwei Eigenschaften entscheiden darüber, wie viel ein Resolver über Sie preisgibt und wie viel ein Beobachter aus
der reinen Paketgröße ableiten kann. Beide lassen sich in je einem Befehl messen.""",
     """Two properties decide how much a resolver gives away about you, and how much an observer can infer from packet
size alone. Each can be measured with a single command."""),
]

CHECKS = [
    {
        "group": "dnssec",
        "title": "Die Positivkontrolle",
        "title_en": "The positive control",
        "question": "Markiert der Resolver eine korrekt signierte Antwort als geprüft?",
        "question_en": "Does the resolver mark a correctly signed answer as verified?",
        "command": "dig +dnssec @9.9.9.9 sigok.ippacket.stream A",
        "expected": """In der Zeile <code>;; flags:</code> muss neben <code>qr rd ra</code> auch <code>ad</code> stehen, der Status
muss <code>NOERROR</code> sein. Gemessen am 7. September 2026: <code>status: NOERROR</code> und
<code>flags: qr rd ra ad</code>. Das <code>ad</code> steht für „authentic data“. RFC 4035 erlaubt einem Server, dieses
Bit nur zu setzen, wenn er alle Datensätze der Antwort selbst geprüft hat.""",
        "expected_en": """The line <code>;; flags:</code> must contain <code>ad</code> alongside <code>qr rd ra</code>, and the
status must be <code>NOERROR</code>. Measured on 7 September 2026: <code>status: NOERROR</code> and
<code>flags: qr rd ra ad</code>. The <code>ad</code> stands for “authentic data”. RFC 4035 permits a server to set this
bit only if it has verified every record in the answer itself.""",
        "note": "Ersetzen Sie <code>9.9.9.9</code> durch die Adresse, die Sie prüfen wollen.",
        "note_en": "Replace <code>9.9.9.9</code> with the address you want to test.",
    },
    {
        "group": "dnssec",
        "title": "Die Negativkontrolle",
        "title_en": "The negative control",
        "question": "Weist der Resolver eine absichtlich falsch signierte Antwort zurück?",
        "question_en": "Does the resolver reject a deliberately mis-signed answer?",
        "command": "dig @9.9.9.9 sigfail.ippacket.stream A\ndig @9.9.9.9 dnssec-failed.org A",
        "expected": """Beide müssen <code>status: SERVFAIL</code> und eine leere Antwortsektion liefern. Gemessen am
7. September 2026: beide <code>SERVFAIL</code>. Kommt stattdessen <code>NOERROR</code> mit einer IP-Adresse zurück,
validiert dieser Resolver nicht. Zwei unabhängige Testdomains deshalb, weil eine davon jederzeit ausfallen kann.""",
        "expected_en": """Both must return <code>status: SERVFAIL</code> and an empty answer section. Measured on
7 September 2026: both <code>SERVFAIL</code>. If <code>NOERROR</code> comes back with an IP address instead, this
resolver does not validate. Two independent test domains, because either one can go away at any time.""",
        "note": None, "note_en": None,
    },
    {
        "group": "dnssec",
        "title": "Der Beweis, dass es wirklich an DNSSEC lag",
        "title_en": "Proof that DNSSEC was really the reason",
        "question": "Ein SERVFAIL kann viele Ursachen haben. Wie schließe ich die anderen aus?",
        "question_en": "A SERVFAIL can have many causes. How do I rule the others out?",
        "command": "dig +cd @9.9.9.9 sigfail.ippacket.stream A",
        "expected": """Mit gesetztem CD-Bit, also „checking disabled“, muss dieselbe Abfrage jetzt <code>NOERROR</code> und eine
Adresse liefern. Gemessen am 7. September 2026: ohne <code>+cd</code> SERVFAIL, mit <code>+cd</code> NOERROR. Genau
dieser Umschlag ist der Beweis: Der Resolver hat vorher geprüft und deshalb abgelehnt, und nicht etwa, weil die Domain
kaputt oder der Server überlastet wäre.""",
        "expected_en": """With the CD bit set, meaning “checking disabled”, the same query must now return <code>NOERROR</code>
and an address. Measured on 7 September 2026: without <code>+cd</code> SERVFAIL, with <code>+cd</code> NOERROR. That
switch is the proof: the resolver checked first and refused for that reason, not because the domain was broken or the
server overloaded.""",
        "note": None, "note_en": None,
    },
    {
        "group": "dnssec",
        "title": "Den Grund im Klartext lesen",
        "title_en": "Reading the reason in plain text",
        "question": "Sagt der Resolver auch, warum er abgelehnt hat?",
        "question_en": "Does the resolver also say why it refused?",
        "command": "dig @9.9.9.9 sigfail.ippacket.stream A | grep EDE",
        "expected": """Eine Zeile der Form <code>; EDE: 6 (DNSSEC Bogus)</code>. Genau das wurde am 7. September 2026 gemessen.
Extended DNS Errors nach RFC 8914 liefern einen maschinenlesbaren Grund statt eines nackten SERVFAIL. Erscheint keine
EDE-Zeile, unterstützt der Resolver diese Erweiterung nicht; das ist für sich genommen kein Mangel an der Validierung.""",
        "expected_en": """A line of the form <code>; EDE: 6 (DNSSEC Bogus)</code>. That is exactly what was measured on
7 September 2026. Extended DNS Errors per RFC 8914 give a machine-readable reason instead of a bare SERVFAIL. If no EDE
line appears, the resolver does not support the extension; on its own that says nothing about its validation.""",
        "note": None, "note_en": None,
    },
    {
        "group": "dnssec",
        "title": "Der Fallstrick, an dem die meisten Tests scheitern",
        "title_en": "The pitfall that ruins most tests",
        "question": "Warum fehlt das ad-Flag, obwohl der Resolver validiert?",
        "question_en": "Why is the ad flag missing even though the resolver validates?",
        "command": "dig +dnssec sigok.ippacket.stream A\ndig +dnssec @9.9.9.9 sigok.ippacket.stream A",
        "expected": """Der Unterschied ist das <code>@</code>. Ohne Adresse fragen Sie den lokalen Dienst des Betriebssystems.
Auf dem Testrechner lieferte der erste Befehl am 7. September 2026 <code>flags: qr rd ra</code> ohne
<code>ad</code>, der zweite <code>flags: qr rd ra ad</code>. Der Upstream validiert also, der lokale Stub reicht die
Markierung nur nicht durch. Wer das nicht weiß, hält einen validierenden Resolver für kaputt.""",
        "expected_en": """The difference is the <code>@</code>. Without an address you are asking the operating system's local
service. On the test machine the first command returned <code>flags: qr rd ra</code> without <code>ad</code> on
7 September 2026, the second <code>flags: qr rd ra ad</code>. So the upstream does validate, the local stub simply does
not pass the marking through. Anyone unaware of this will mistake a validating resolver for a broken one.""",
        "note": "Unter Linux zeigt <code>resolvectl status</code>, was der Systemdienst tut.",
        "note_en": "On Linux, <code>resolvectl status</code> shows what the system service is doing.",
    },
    {
        "group": "identity",
        "title": "Wer antwortet, und was gibt er von mir weiter?",
        "title_en": "Who answers, and what do they pass on about me?",
        "question": "Sieht der autoritative Server meine Adresse, oder nur die des Resolvers?",
        "question_en": "Does the authoritative server see my address, or only the resolver's?",
        "command": "dig +short TXT whoami.ds.akahelp.net",
        "expected": """Der Dienst von Akamai antwortet mit bis zu drei Paaren. <code>ns</code> ist die Adresse des Resolvers, der
tatsächlich angefragt hat. Erscheint zusätzlich <code>ecs</code>, wurde ein Teil Ihrer eigenen Adresse mitgeschickt.
Gemessen am 7. September 2026 über den Systemresolver: nur <code>"ns"</code>, kein <code>ecs</code>. Es wurde also
nichts von der Client-Adresse weitergereicht.""",
        "expected_en": """This Akamai service answers with up to three pairs. <code>ns</code> is the address of the resolver that
actually asked. If <code>ecs</code> appears as well, part of your own address was sent along. Measured on
7 September 2026 through the system resolver: only <code>"ns"</code>, no <code>ecs</code>. So nothing of the client
address was passed on.""",
        "note": None, "note_en": None,
    },
    {
        "group": "identity",
        "title": "Derselbe Anbieter, zwei Adressen, zwei Ergebnisse",
        "title_en": "One provider, two addresses, two outcomes",
        "question": "Wie sieht der Unterschied zwischen mit und ohne EDNS Client Subnet konkret aus?",
        "question_en": "What does the difference between with and without EDNS Client Subnet actually look like?",
        "command": "dig +short TXT whoami.ds.akahelp.net @9.9.9.9\ndig +short TXT whoami.ds.akahelp.net @9.9.9.11",
        "expected": """Gemessen am 7. September 2026. Über <code>9.9.9.9</code> kam ausschließlich <code>"ns"</code> mit der
Resolveradresse zurück. Über <code>9.9.9.11</code> kamen zusätzlich <code>"ip"</code> und
<code>"ecs" "203.0.113.0/24/24"</code>, also das eigene Netz mit gekürzter Adresse. Derselbe Betreiber, dieselbe
Datenschutzerklärung, ein Zeichen Unterschied in der Adresse. Das ist der sauberste Nachweis für ECS, weil alle
anderen Bedingungen gleich bleiben.""",
        "expected_en": """Measured on 7 September 2026. Via <code>9.9.9.9</code> only <code>"ns"</code> came back with the resolver
address. Via <code>9.9.9.11</code> there were additionally <code>"ip"</code> and
<code>"ecs" "203.0.113.0/24/24"</code>, meaning your own network with a truncated address. Same operator, same privacy
policy, one character of difference in the address. This is the cleanest demonstration of ECS, because every other
condition stays the same.""",
        "note": "Die gezeigte Netzangabe ist ein Beispiel. In Ihrer Ausgabe steht Ihr eigenes Netz.",
        "note_en": "The network shown is an example. Your own output will contain your own network.",
    },
    {
        "group": "identity",
        "title": "Welcher Knoten eines Anycast-Netzes antwortet",
        "title_en": "Which node of an anycast network answers",
        "question": "Anycast heißt: viele Server, eine Adresse. Welcher ist es gerade?",
        "question_en": "Anycast means many servers, one address. Which one is it right now?",
        "command": "dig +nsid @9.9.9.9 example.com A",
        "expected": """Im Abschnitt <code>OPT PSEUDOSECTION</code> erscheint eine Zeile
<code>; NSID: ... ("res701.qfra3")</code>. Genau das wurde am 7. September 2026 gemessen; die Kennung deutet auf einen
Standort in Frankfurt. Fehlt die Zeile, sendet der Server keine Kennung. Der Vorteil gegenüber der älteren Abfrage
<code>dig @server CH TXT id.server</code>: Die Kennung reist in der normalen Antwort mit.""",
        "expected_en": """In the <code>OPT PSEUDOSECTION</code> a line appears reading
<code>; NSID: ... ("res701.qfra3")</code>. That is what was measured on 7 September 2026; the identifier points to a
location in Frankfurt. If the line is missing, the server sends no identifier. The advantage over the older query
<code>dig @server CH TXT id.server</code> is that the identifier travels along with the normal answer.""",
        "note": None, "note_en": None,
    },
    {
        "group": "encrypted",
        "title": "DNS over TLS in einem Befehl",
        "title_en": "DNS over TLS in one command",
        "question": "Kommt die Antwort tatsächlich durch den TLS-Kanal?",
        "question_en": "Does the answer really arrive through the TLS channel?",
        "command": "dig +tls @dns.quad9.net example.com A",
        "expected": """Entscheidend ist die vorletzte Zeile. Gemessen am 7. September 2026:
<code>;; SERVER: 149.112.112.112#853(dns.quad9.net) (TLS)</code>. Das <code>(TLS)</code> und der Port
<code>853</code> sind der Beleg. Steht dort kein <code>(TLS)</code>, lief die Abfrage im Klartext.""",
        "expected_en": """The decisive line is the penultimate one. Measured on 7 September 2026:
<code>;; SERVER: 149.112.112.112#853(dns.quad9.net) (TLS)</code>. The <code>(TLS)</code> and port <code>853</code> are
the evidence. If <code>(TLS)</code> is absent, the query ran in the clear.""",
        "note": None, "note_en": None,
    },
    {
        "group": "encrypted",
        "title": "Der häufigste Fehler: verschlüsselt, aber ungeprüft",
        "title_en": "The most common mistake: encrypted but unverified",
        "question": "Verschlüsselung ohne Zertifikatsprüfung schützt gegen wen genau?",
        "question_en": "Encryption without certificate checking protects against whom exactly?",
        "command": "echo QUIT | openssl s_client -connect dns.quad9.net:853 \\\n  -servername dns.quad9.net -alpn dot 2>&1 \\\n  | grep -E 'subject=|Verification|ALPN protocol'",
        "expected": """Drei Zeilen müssen zusammenkommen. Gemessen am 7. September 2026:
<code>subject=C=CH, ST=Zurich, L=Zürich, O=Quad9, CN=dns.quad9.net</code>, dann <code>Verification: OK</code>, dann
<code>ALPN protocol: dot</code>. Erst alle drei zusammen belegen: verschlüsselt, richtiger Gegenüber, richtiges
Protokoll. Ein Handschlag allein belegt nur, dass irgendjemand geantwortet hat.""",
        "expected_en": """Three lines must come together. Measured on 7 September 2026:
<code>subject=C=CH, ST=Zurich, L=Zürich, O=Quad9, CN=dns.quad9.net</code>, then <code>Verification: OK</code>, then
<code>ALPN protocol: dot</code>. Only all three together establish encrypted, correct counterpart, correct protocol. A
handshake alone establishes only that somebody answered.""",
        "note": """Mit <code>kdig</code> aus dem Paket <code>knot-dnsutils</code> (Debian, Ubuntu) beziehungsweise
<code>knot-utils</code> (Fedora, RHEL) geht dasselbe kürzer:
<code>kdig -d @dns.quad9.net +tls-ca +tls-host=dns.quad9.net example.com A</code>. Achtung: <code>+tls</code> allein
prüft das Zertifikat nicht, dafür braucht es <code>+tls-ca</code>.""",
        "note_en": """With <code>kdig</code> from the package <code>knot-dnsutils</code> (Debian, Ubuntu) or
<code>knot-utils</code> (Fedora, RHEL) the same thing is shorter:
<code>kdig -d @dns.quad9.net +tls-ca +tls-host=dns.quad9.net example.com A</code>. Note that <code>+tls</code> on its
own does not verify the certificate; that requires <code>+tls-ca</code>.""",
    },
    {
        "group": "encrypted",
        "title": "Die Gegenprobe, die scheitern muss",
        "title_en": "The counter-test that has to fail",
        "question": "Prüft mein Werkzeug wirklich, oder nickt es alles ab?",
        "question_en": "Does my tool really check, or does it wave everything through?",
        "command": "echo QUIT | openssl s_client -connect 9.9.9.9:853 \\\n  -servername dns.quad9.net -alpn dot -verify_return_error \\\n  -verify_hostname wrong.example.com 2>&1 | grep -iE 'verif|error' | head -3",
        "expected": """Dieser Befehl muss fehlschlagen. Erwartet wird eine Zeile mit einem Prüffehler zum Hostnamen. Kommt hier
eine erfolgreiche Prüfung zurück, ist Ihre gesamte übrige Prüfung wertlos. Eine Negativkontrolle, die nicht scheitert,
misst nichts.""",
        "expected_en": """This command has to fail. Expected is a line reporting a verification error about the hostname. If a
successful verification comes back here, all your other checks are worthless. A negative control that does not fail
measures nothing.""",
        "note": None, "note_en": None,
    },
    {
        "group": "encrypted",
        "title": "DNS over QUIC prüfen",
        "title_en": "Checking DNS over QUIC",
        "question": "Spricht der Endpunkt wirklich DoQ, oder nur beinahe?",
        "question_en": "Does the endpoint really speak DoQ, or only almost?",
        "command": "openssl s_client -quic -alpn doq -connect dns.quad9.net:853 \\\n  -servername dns.quad9.net < /dev/null 2>&1 \\\n  | grep -E 'ALPN protocol|Verification'",
        "expected": """Gemessen am 7. September 2026: <code>Verification: OK</code> und <code>ALPN protocol: doq</code>. Achtung
bei der Auslegung: Ein ausgehandeltes <code>doq</code> beweist nur, dass der Server das Protokoll annimmt. Ob danach
auch eine Antwort kommt, ist eine zweite Frage. Genau dieser Unterschied trat bei UncensoredDNS auf, wo der Handschlag
gelang, eine echte Abfrage aber unbeantwortet blieb.""",
        "expected_en": """Measured on 7 September 2026: <code>Verification: OK</code> and <code>ALPN protocol: doq</code>. A word
on interpretation: a negotiated <code>doq</code> proves only that the server accepts the protocol. Whether an answer
follows is a separate question. That very difference showed up at UncensoredDNS, where the handshake succeeded but a
real query went unanswered.""",
        "note": "Braucht OpenSSL 3.5 oder neuer. Version prüfen mit <code>openssl version</code>.",
        "note_en": "Requires OpenSSL 3.5 or newer. Check with <code>openssl version</code>.",
    },
    {
        "group": "encrypted",
        "title": "DNS over HTTPS, der bequeme und der genaue Weg",
        "title_en": "DNS over HTTPS, the convenient way and the exact way",
        "question": "Antwortet der DoH-Endpunkt so, wie RFC 8484 es vorschreibt?",
        "question_en": "Does the DoH endpoint answer the way RFC 8484 requires?",
        "command": "dig +https @dns.quad9.net example.com A\n\ncurl -sS -o antwort.bin -w '%{http_code} %{content_type} %{size_download}\\n' \\\n  -H 'accept: application/dns-message' \\\n  'https://dns.quad9.net/dns-query?dns=AAABAAABAAAAAAAAA3d3dwdleGFtcGxlA2NvbQAAAQAB'",
        "expected": """Der erste Befehl ist der bequeme: <code>dig</code> spricht DoH selbst und zeigt eine lesbare Antwort.
Der zweite zeigt, was wirklich über die Leitung geht. Gemessen am 7. September 2026:
<code>200 application/dns-message 65</code>. Die Datei enthält eine binäre DNS-Nachricht, kein JSON. Die ersten Bytes
lauten <code>00 00 81 80 00 01 00 02</code>: Kennung null, wie RFC 8484 es verlangt, Antwortbit gesetzt, eine Frage,
zwei Antworten.""",
        "expected_en": """The first command is the convenient one: <code>dig</code> speaks DoH itself and shows a readable answer.
The second shows what actually goes over the wire. Measured on 7 September 2026:
<code>200 application/dns-message 65</code>. The file contains a binary DNS message, not JSON. The first bytes read
<code>00 00 81 80 00 01 00 02</code>: identifier zero as RFC 8484 requires, response bit set, one question, two
answers.""",
        "note": """Die Base64-Zeichenkette im Beispiel steht so im RFC 8484 selbst und fragt nach
<code>www.example.com</code>. Manche Anbieter bieten zusätzlich eine JSON-Schnittstelle an; die ist bequem, aber kein
Standard und funktioniert nicht überall gleich.""",
        "note_en": """The base64 string in the example appears verbatim in RFC 8484 itself and asks for
<code>www.example.com</code>. Some providers additionally offer a JSON interface; it is convenient, but it is not a
standard and does not behave the same everywhere.""",
    },
    {
        "group": "metadata",
        "title": "QNAME-Minimierung",
        "title_en": "QNAME minimisation",
        "question": "Erfährt jeder Server auf dem Weg den vollen Namen, oder nur so viel wie nötig?",
        "question_en": "Does every server along the way learn the full name, or only as much as it needs?",
        "command": "dig +short TXT qnamemintest.internet.nl @9.9.9.9",
        "expected": """Die Antwort enthält genau einen von zwei Sätzen. Gemessen am 7. September 2026:
<code>"HOORAY - QNAME minimisation is enabled on your resolver :)!"</code>. Die Gegenaussage lautet
<code>"NO - QNAME minimisation is NOT enabled on your resolver :("</code>. Daneben erscheinen immer die Zeile
<code>a.b.qnamemin-test.internet.nl.</code> und ein SPF-Eintrag; die Reihenfolge wechselt.""",
        "expected_en": """The answer contains exactly one of two sentences. Measured on 7 September 2026:
<code>"HOORAY - QNAME minimisation is enabled on your resolver :)!"</code>. The opposite reads
<code>"NO - QNAME minimisation is NOT enabled on your resolver :("</code>. Alongside it you always get the line
<code>a.b.qnamemin-test.internet.nl.</code> and an SPF record; the order varies.""",
        "note": "Der Testdienst wird von SIDN Labs und NLnet Labs betrieben.",
        "note_en": "The test service is operated by SIDN Labs and NLnet Labs.",
    },
    {
        "group": "metadata",
        "title": "Polstert der Resolver seine Antworten?",
        "title_en": "Does the resolver pad its answers?",
        "question": "Verschlüsselung verbirgt den Inhalt. Verbirgt sie auch die Länge?",
        "question_en": "Encryption hides the content. Does it hide the length as well?",
        "command": "dig +tls +padding=468 A example.com @9.9.9.9\ndig +tls +padding=468 A example.com @1.1.1.1",
        "expected": """Ein sehenswerter Unterschied. Gemessen am 7. September 2026: Bei <code>9.9.9.9</code> fehlte die
PAD-Zeile, und <code>;; MSG SIZE  rcvd: 72</code> zeigte die ungepolsterte Größe. Bei <code>1.1.1.1</code> erschien
<code>; PAD: (392 bytes)</code> und <code>;; MSG SIZE  rcvd: 468</code>. Cloudflare polsterte die Antwort auf eine
einheitliche Länge, Quad9 an diesem Tag nicht.""",
        "expected_en": """A difference worth seeing. Measured on 7 September 2026: at <code>9.9.9.9</code> the PAD line was
absent and <code>;; MSG SIZE  rcvd: 72</code> showed the unpadded size. At <code>1.1.1.1</code> there appeared
<code>; PAD: (392 bytes)</code> and <code>;; MSG SIZE  rcvd: 468</code>. Cloudflare padded the answer to a uniform
length, Quad9 did not on that day.""",
        "note": """Warum das zählt: RFC 9076 weist darauf hin, dass sich aus Größe und Zeitmuster verschlüsselter
Nachrichten Rückschlüsse ziehen lassen. Polsterung nach RFC 7830 nimmt dieser Auswertung die Grundlage. Ein einzelner
Messwert an einem Tag ist allerdings keine Aussage über den Dauerbetrieb.""",
        "note_en": """Why this matters: RFC 9076 points out that inferences can be drawn from the size and timing patterns of
encrypted messages. Padding per RFC 7830 removes the basis for that analysis. A single measurement on one day is not,
however, a statement about continuous operation.""",
    },
]


# ---------------------------------------------------------------------------
# Geprueft und bewusst nicht aufgenommen. Wer nur nennt, was er empfiehlt,
# verschweigt die Haelfte der Arbeit.
# ---------------------------------------------------------------------------

GLOSSARY_GROUPS = [
    ("basics", "Grundbegriffe", "Fundamentals"),
    ("protocols", "Protokolle und Erweiterungen", "Protocols and extensions"),
]

NOT_LISTED = [
    {
        "name": "CIRA Canadian Shield",
        "reason": "Vertraglich auf Kanada beschränkt",
        "reason_en": "Contractually limited to Canada",
        "de": """Fachlich wäre dieser Dienst ein Vorbild. Betreiberin ist die Canadian Internet Registration Authority, eine
gemeinnützige Körperschaft nach kanadischem Bundesrecht, die zugleich die Landesdomain .ca führt. Der Dienst finanziert
sich quer aus den Registrierungsgebühren, nennt eine ausdrückliche Aufbewahrungsgrenze von 24 Stunden, validiert DNSSEC
nachweislich und bietet eine wirklich ungefilterte Variante.

Er steht trotzdem nicht in der Liste. Die Nutzungsbedingungen verlangen eine Zusicherung: „You represent and warrant
that a) you are an individual resident of Canada“. Wer den Dienst von Deutschland aus einträgt, gibt damit eine Erklärung
ab, die nicht stimmt. Technisch erreichbar ist er, das ändert an der Rechtslage nichts. Dazu kommt: Es gibt keinen
europäischen Standort, die Antwortzeit lag im Test bei rund 100 Millisekunden.

Für Leserinnen und Leser mit Wohnsitz in Kanada ist er eine sehr gute Wahl. Für alle anderen wäre eine Empfehlung eine
Aufforderung zum Vertragsbruch.""",
        "en": """On the merits this service would be a model. It is run by the Canadian Internet Registration Authority, a
not-for-profit corporation under Canadian federal law that also operates the country domain .ca. The service is
cross-funded from registration fees, states an explicit 24-hour retention limit, demonstrably validates DNSSEC and
offers a genuinely unfiltered variant.

It is still not in the list. The terms of use require a representation: “You represent and warrant that a) you are an
individual resident of Canada”. Anyone configuring the service from Germany makes a declaration that is untrue. It is
technically reachable, which changes nothing about the legal position. On top of that there is no European location;
response time in our test was around 100 milliseconds.

For readers resident in Canada it is a very good choice. For everyone else, recommending it would be an invitation to
break a contract.""",
        "sources": [
            ("https://www.cira.ca/en/canadian-shield/tandc/",
             "CIRA Canadian Shield: Nutzungsbedingungen", "CIRA Canadian Shield: terms and conditions"),
        ],
    },
]
