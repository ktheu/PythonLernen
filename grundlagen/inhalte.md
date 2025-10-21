# Inhalte: 01_grundlagen.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Variablen und Zuweisungen** | - Zuweisung von Werten an Variablen<br>- Datentypen: int (ganze Zahlen) und float (Dezimalzahlen)<br>- Dezimalzahlen mit Punkt statt Komma |
| **print-Funktion** | - Ausgabe von Variablenwerten<br>- Ausgabe mehrerer Werte (durch Komma getrennt)<br>- Werte werden durch Leerzeichen getrennt ausgegeben |
| **Wertänderung** | - Variablen können durch erneute Zuweisung verändert werden<br>- Beispiel: `x = x + 1` |
| **Kommentare** | - Einzeilige Kommentare mit `#`<br>- Mehrzeilige Kommentare mit `'''...'''`<br>- Kommentare dienen zur Dokumentation |
| **Variablennamen** | - Case-sensitiv<br>- Beginnen mit Buchstabe oder Unterstrich<br>- Kurze Namen bei klarem Kontext erlaubt<br>- Sprechende Namen bevorzugt<br>- camelCase oder snake_case für zusammengesetzte Namen |
| **Kurzformen für Zuweisungen** | - `x += 1` statt `x = x + 1`<br>- `x -= 1` statt `x = x - 1`<br>- `x *= 2` statt `x = x * 2` usw. |
| **Arithmetische Operatoren** | - Addition `+`<br>- Subtraktion `-`<br>- Multiplikation `*`<br>- Division `/`<br>- Exponentation `**`<br>- Modulo `%` (Rest bei Division)<br>- Ganzzahlige Division `//` |
| **Auswertungsreihenfolge** | - Exponentation vor Punktrechnung vor Strichrechnung<br>- Verwendung von Klammern im Zweifelsfall |

---

# Inhalte: 02_strings.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Strings (Zeichenketten)** | - Eingeschlossen in einfachen `'...'` oder doppelten `"..."` Hochkommata<br>- Mehrzeilige Strings mit dreifachen Hochkommata `'''...'''`<br>- Zeichenketten zur Darstellung von Text |
| **Länge eines Strings** | - `len(s)` gibt die Anzahl der Zeichen zurück |
| **String-Konkatenation** | - Strings mit `+` aneinanderpappen<br>- Beispiel: `'Hallo' + ' ' + 'Welt'` |
| **Input-Funktion** | - `input()` liest Benutzereingaben von der Konsole<br>- Gibt immer einen String zurück<br>- Umwandlung in Zahlen mit `int()` oder `float()` |
| **f-Strings** | - Variablen direkt in Strings einfügen mit `f'...{variable}...'`<br>- Formatierung mit Mindestlänge: `{variable:5}`<br>- Dezimalzahlen runden: `{variable:.2f}` für 2 Nachkommastellen<br>- Ermöglicht übersichtliche Ausgaben von Text und Variablen |
