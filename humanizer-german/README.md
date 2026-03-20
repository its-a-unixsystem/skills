# Humanizer German

KI-Schreibmuster in deutschen Texten erkennen und entfernen.

Basierend auf dem [WikiProjekt KI und Wikipedia / Erkennung KI-Einsatz](https://de.wikipedia.org/wiki/Wikipedia:WikiProjekt_KI_und_Wikipedia/Erkennung_KI-Einsatz) der deutschsprachigen Wikipedia, angepasst für allgemeine deutsche Texte jenseits von Wikipedia.

**ACHTUNG:** Dieser Skill dient nicht dazu, KI-Detektoren (beispielsweise im akademischen Kontext) zu täuschen. Ziel ist es stattdessen, den Lesefluss zu verbessern und KI-generierte Texte natürlicher und angenehmer lesbar zu machen.

## Installation via skills.sh

```bash
npx skills add https://github.com/its-a-unixsystem/skills --skill humanizer-german
```
Mehr Details siehe [skills.sh](https://skills.sh).

## Installation über Claude Desktop

In Claude Desktop:
1. Menü „Skills" öffnen
2. „Add Skill" klicken
3. URL eingeben: `https://github.com/its-a-unixsystem/skills`
4. Skill `humanizer-german` auswählen

## Manuelle Installation

Skill-Verzeichnis nach `~/.claude/skills/` kopieren:

## Verwendung

Der Skill wird automatisch aktiviert, wenn Claude deutschen Text vermenschlichen, bereinigen oder auf KI-Muster prüfen soll. Beispiele:

- „Mach diesen Text menschlicher"
- „Entferne KI-Slop aus diesem Absatz"
- „Prüf diesen Text auf KI-Muster"
- „Humanize this German text"

## Erkannte Muster (28)

### Inhaltliche Muster

#### 1. Bedeutungs-Überhöhungen

KI bläht die Bedeutung von Dingen auf, indem sie abstrakte Wichtigkeitsformeln anhängt, ohne neue Information zu liefern.

> **Vorher:** Das Statistische Institut wurde 1989 gegründet und markiert einen entscheidenden Wendepunkt in der Entwicklung der regionalen Statistik. Diese Initiative spielte eine zentrale Rolle bei der Dezentralisierung und trug wesentlich zur Modernisierung der Verwaltung bei.
>
> **Nachher:** Das Statistische Institut wurde 1989 gegründet. Es erhebt und veröffentlicht regionale Statistiken unabhängig vom nationalen Statistikamt.

#### 2. Autoritäten-Verweise ohne konkrete Quellen

KI verweist auf vage Autoritäten statt auf konkrete Quellen.

> **Vorher:** Experten betonen, dass der Fluss eine entscheidende Rolle im regionalen Ökosystem spielt. Studien zeigen, dass die Artenvielfalt in diesem Gebiet von großer Bedeutung ist.
>
> **Nachher:** In dem Fluss leben mehrere endemische Fischarten, wie eine Studie der Universität Freiburg von 2019 belegt.

#### 3. Werbliche Sprache

KI-Texte über Personen, Orte oder Unternehmen klingen oft wie Pressemitteilungen oder Reiseführer.

> **Vorher:** Idyllisch gelegen im Herzen Bayerns, besticht die Stadt durch ihre einzigartige Kombination aus kulturellem Reichtum und atemberaubender Natur. Sie zeichnet sich durch ein herausragendes gastronomisches Angebot aus.
>
> **Nachher:** Die Stadt liegt in Oberbayern. Sie hat ein Heimatmuseum, mehrere Brauereien und einen Wochenmarkt.

#### 4. Geschwätzigkeit

KI-Text enthält mehr Formulierungen als nötig: Wiederholungen, überflüssige Einleitungen, allgemein gehaltene Aussagen.

> **Vorher:** Die Photosynthese ist ein sehr wichtiger biologischer Prozess, der eine entscheidende Rolle für das Leben auf der Erde spielt. Dabei handelt es sich um einen Prozess, bei dem Pflanzen, Algen und einige Bakterien Lichtenergie nutzen, um chemische Energie zu erzeugen. Dieser Prozess ist deshalb von großer Bedeutung, weil er die Grundlage vieler Nahrungsketten bildet und außerdem zur Produktion von Sauerstoff beiträgt.
>
> **Nachher:** Die Photosynthese ist der Prozess, bei dem Pflanzen, Algen und einige Bakterien Lichtenergie in chemische Energie umwandeln und dabei Sauerstoff freisetzen.

#### 5. Pseudo-Ausgewogenheit

KI versucht krampfhaft, alle Seiten zu beleuchten, auch wenn eine klar überwiegt.

> **Vorher:** Während einige die Maßnahme begrüßen, warnen andere vor möglichen Risiken. Befürworter argumentieren, dass die Vorteile überwiegen, während Kritiker auf potenzielle Nachteile hinweisen. Letztlich muss jeder für sich selbst entscheiden.
>
> **Nachher:** Die Maßnahme ist in der Fachwelt weitgehend unumstritten. Vereinzelt gibt es Bedenken wegen der Kosten.

### Sprach- und Grammatikmuster

#### 6. KI-Floskeln

Standardisierte Formulierungen, die Struktur oder Bedeutung suggerieren, aber wenig Information liefern. KI-typisch ist die Häufung.

> **Vorher:** Darüber hinaus ist zu beachten, dass das Gebäude denkmalgeschützt ist.
>
> **Nachher:** Das Gebäude ist denkmalgeschützt.

Typische Floskeln: „Es ist wichtig zu beachten, dass …", „Grundsätzlich lässt sich sagen, dass …", „In der heutigen Zeit …", „Zusammenfassend lässt sich sagen, dass …", „Ein weiterer wichtiger Aspekt ist …"

#### 7. Füllphrasen

Unnötig aufgeblähte Formulierungen.

> - „Um dieses Ziel zu erreichen" → „Dafür"
> - „Aufgrund der Tatsache, dass" → „Weil"
> - „Zum gegenwärtigen Zeitpunkt" → „Derzeit"
> - „Das System verfügt über die Fähigkeit" → „Das System kann"
> - „Es sei darauf hingewiesen, dass" → einfach weglassen

#### 8. Übermäßiges Hedging

Zu viele Absicherungen in einem Satz.

> **Vorher:** Es könnte möglicherweise argumentiert werden, dass die Maßnahme unter Umständen gewisse Auswirkungen haben könnte.
>
> **Nachher:** Die Maßnahme hat wahrscheinlich Auswirkungen.

#### 9. Synonymkreisel (Elegant Variation)

KI wechselt krampfhaft zwischen Synonymen. Im Deutschen besonders auffällig bei Personenbezeichnungen.

> **Vorher:** Der Forscher untersuchte die Proben. Der Wissenschaftler kam zu überraschenden Ergebnissen. Der Experte veröffentlichte seine Studie. Der Akademiker wurde daraufhin eingeladen.
>
> **Nachher:** Der Forscher untersuchte die Proben und kam zu überraschenden Ergebnissen. Nach der Veröffentlichung seiner Studie wurde er eingeladen.

#### 10. Negative Parallelismen

Konstruktionen wie „Nicht nur … sondern auch …" oder „Es geht nicht nur um … es geht um …" sind bei KI massiv überrepräsentiert.

> **Vorher:** Es geht nicht nur um den Beat unter den Vocals, es geht um die Aggression und Atmosphäre. Es ist nicht nur ein Song, es ist ein Statement.
>
> **Nachher:** Der schwere Beat verstärkt den aggressiven Ton.

#### 11. Dreierregel-Übernutzung

KI erzwingt Ideen in Dreiergruppen, um umfassend zu wirken.

> **Vorher:** Die Veranstaltung bietet Vorträge, Podiumsdiskussionen und Networking-Möglichkeiten. Die Teilnehmer können Innovation, Inspiration und Brancheneinblicke erwarten.
>
> **Nachher:** Die Veranstaltung besteht aus Vorträgen und Podien. Zwischen den Programmpunkten ist Zeit zum Netzwerken.

#### 12. Falsche Spannbögen

KI nutzt „von X bis Y"-Konstruktionen, bei denen X und Y auf keiner sinnvollen Skala liegen.

> **Vorher:** Von der Gründung über die Industrialisierung bis hin zur Digitalisierung hat die Stadt eine beeindruckende Entwicklung durchlaufen, die von Tradition und Innovation gleichermaßen geprägt ist.
>
> **Nachher:** Die Stadt wurde 1250 gegründet und war im 19. Jahrhundert ein Textilstandort. Heute gibt es dort mehrere IT-Unternehmen.

#### 13. KI-Anglizismen und falsche Idiome

KI-Modelle übersetzen englische Redewendungen oft wörtlich ins Deutsche.

> - „Lassen Sie uns eintauchen in …" (von "Let's dive into...")
> - „Ein Testament für seine harte Arbeit …" (von "A testament to...")
> - „Am Ende des Tages …" (von "At the end of the day...")

Lösung: Durch natürliche deutsche Idiome ersetzen oder die Aussage direkt formulieren.

#### 14. Passiv- und Nominalstil (Behördensprech)

KI flüchtet sich in Passivkonstruktionen und substantivierte Verben, um distanziert und objektiv zu klingen.

> **Vorher:** Die Optimierung der Prozesse wird durch die neue Software vorgenommen, wodurch eine Steigerung der Effizienz erreicht werden kann.
>
> **Nachher:** Die neue Software optimiert die Prozesse und steigert die Effizienz.

#### 15. Überstrapaziertes „Safe-Vokabular"

KI nutzt ständig dieselben sterilen Adjektive und Nomen, um Kompetenz vorzutäuschen.

Typische Wörter: *facettenreich, vielschichtig, essenziell, nahtlos, robust, innovativ, tiefgreifend, Synergie, Paradigmenwechsel, eine breite Palette an…, eine Vielzahl von…*

> **Vorher:** Eine breite Palette an Funktionen
>
> **Nachher:** Zahlreiche Funktionen

### Stilmuster

#### 16. Geviertstrich-Übernutzung

KI verwendet Geviertstriche (—) häufiger als Menschen. Im Deutschen ist der Halbgeviertstrich (–) ohnehin üblicher.

> **Vorher:** Der Begriff wird hauptsächlich von niederländischen Institutionen verwendet — nicht von den Betroffenen selbst. Man sagt nicht „Niederlande, Europa" als Adresse — und trotzdem setzt sich diese Fehlbezeichnung durch — selbst in offiziellen Dokumenten.
>
> **Nachher:** Der Begriff wird hauptsächlich von niederländischen Institutionen verwendet, nicht von den Betroffenen selbst. Man sagt nicht „Niederlande, Europa" als Adresse, trotzdem taucht diese Fehlbezeichnung in offiziellen Dokumenten auf.

#### 17. Fettdruck-Übernutzung

KI hebt Schlüsselwörter mechanisch durch Fettdruck hervor.

> **Vorher:** **Künstliche Intelligenz** verändert derzeit **grundlegend** die Art und Weise, wie **Organisationen**, **Unternehmen** und **Gesellschaften** mit **Daten** und **Entscheidungsprozessen** umgehen.
>
> **Nachher:** Künstliche Intelligenz verändert, wie Organisationen mit Daten und Entscheidungen umgehen.

#### 18. Listen mit Fettdruck-Überschriften

KI erzeugt Listen, bei denen jeder Punkt mit einer fett gedruckten Kopfzeile und Doppelpunkt beginnt.

> **Vorher:**
> - **Benutzererlebnis:** Das Benutzererlebnis wurde durch ein neues Interface deutlich verbessert.
> - **Leistung:** Die Leistung wurde durch optimierte Algorithmen gesteigert.
> - **Sicherheit:** Die Sicherheit wurde durch Ende-zu-Ende-Verschlüsselung gestärkt.
>
> **Nachher:** Das Update verbessert die Oberfläche, beschleunigt die Ladezeiten durch optimierte Algorithmen und führt Ende-zu-Ende-Verschlüsselung ein.

#### 19. Überstrukturiertheit

KI strukturiert Text stärker als nötig: viele Überschriften auch bei kurzen Texten, nummerierte Listen wo Fließtext reichen würde, symmetrische Gliederungen, regelmäßige Absatzlängen, Einleitung–Hauptteil–Fazit auch bei kurzen Sachtexten.

Lösung: Kurze Abschnitte zusammenführen, unnötige Listen in Fließtext umwandeln, „Fazit"-Abschnitte entfernen die nur wiederholen.

#### 20. Schematische Listen

KI erzeugt auffällig oft Listen mit magischen Standardanzahlen (3, 5, 7, 10). Alle Punkte sind grammatisch identisch aufgebaut. Mehrere Punkte sagen praktisch das Gleiche.

> **Vorher:**
> 1. Verbesserung der Effizienz
> 2. Optimierung der Prozesse
> 3. Steigerung der Produktivität
> 4. Förderung der Innovation
>
> **Nachher:** Die Software beschleunigt die Datenverarbeitung. Ein neues Modulsystem erlaubt es, eigene Erweiterungen zu schreiben.

#### 21. Mechanischer Rhythmus

KI-Sätze sind oft alle exakt gleich lang und folgen stur dem Subjekt-Prädikat-Objekt-Muster (geringe „Burstiness").

> **Vorher:** Der Algorithmus verarbeitet die Daten in Echtzeit. Die Nutzer sehen die Ergebnisse sofort auf dem Bildschirm. Das Unternehmen profitiert von der hohen Geschwindigkeit.
>
> **Nachher:** Datenverarbeitung in Echtzeit. Das bedeutet für Nutzer: Ergebnisse sofort auf dem Schirm – und für das Unternehmen einen massiven Geschwindigkeitsvorteil.

#### 22. Punkt-Wahn in Aufzählungen

KI setzt pedantisch hinter jeden noch so kurzen Bullet-Point einen Punkt, selbst wenn es nur Stichworte sind.

> **Vorher:**
> - Schnelle Lieferung.
> - Günstiger Preis.
>
> **Nachher:**
> - Schnelle Lieferung
> - Günstiger Preis

#### 23. Emojis

KI dekoriert Überschriften oder Aufzählungspunkte mit Emojis.

> **Vorher:**
> 🚀 **Launch-Phase:** Das Produkt startet in Q3
> 💡 **Wichtige Erkenntnis:** Nutzer bevorzugen Einfachheit
>
> **Nachher:** Das Produkt startet in Q3. Nutzerforschung zeigt eine Präferenz für Einfachheit.

#### 24. Typografische Anführungszeichen

KI-Modelle verwenden oft englische typografische Anführungszeichen (“...”) statt der im Deutschen üblichen („...").

> **Vorher:** Er sagte “Das Projekt liegt im Zeitplan”, aber andere waren anderer Meinung.
>
> **Nachher:** Er sagte „Das Projekt liegt im Zeitplan", aber andere waren anderer Meinung.

### Kommunikationsmuster

#### 25. KI-Regieanweisungen

Reste eines Chatbot-Dialogs werden in den Text kopiert.

> **Vorher:** Hier ist eine Übersicht über die Französische Revolution. Ich hoffe, das hilft! Lass mich wissen, wenn du möchtest, dass ich einen Abschnitt ausbaue.
>
> **Nachher:** Die Französische Revolution begann 1789, als eine Finanzkrise und Lebensmittelknappheit zu breiten Unruhen führten.

#### 26. Unterwürfiger Ton

Übertrieben positive, gefällige Sprache.

> **Vorher:** Tolle Frage! Du hast absolut recht, dass das ein komplexes Thema ist. Das ist ein ausgezeichneter Punkt zu den wirtschaftlichen Faktoren.
>
> **Nachher:** Die wirtschaftlichen Faktoren, die du ansprichst, sind hier relevant.

#### 27. Generisch positive Schlussformeln

Vage, optimistische Enden ohne konkrete Information. Die „besinnliche Schlussbetrachtung".

> **Vorher:** Die Zukunft sieht vielversprechend aus für das Unternehmen. Es stehen spannende Zeiten bevor, während es seinen Weg zu Exzellenz fortsetzt. Dies stellt einen wichtigen Schritt in die richtige Richtung dar.
>
> **Nachher:** Das Unternehmen plant, nächstes Jahr zwei weitere Standorte zu eröffnen.

#### 28. Inkonsequente Anrede (Sie/Du-Mischmasch)

Die KI wechselt innerhalb eines Textes unbemerkt zwischen der förmlichen Anrede („Sie/Ihnen") und der vertraulichen Form („Du/Ihr/Euch").

Lösung: Eine Anredeform wählen und im gesamten Text beibehalten. Wo möglich die direkte Anrede ganz weglassen.

## Quelle

Basierend auf [Wikipedia:WikiProjekt KI und Wikipedia / Erkennung KI-Einsatz](https://de.wikipedia.org/wiki/Wikipedia:WikiProjekt_KI_und_Wikipedia/Erkennung_KI-Einsatz), gepflegt vom deutschen WikiProjekt KI und Wikipedia, angepasst für allgemeine deutsche Texte, sowie dem [Humanizer](https://github.com/blader/humanizer) von blader.
