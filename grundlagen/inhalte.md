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

---

# Inhalte: 03_bedingungen.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Bedingte Anweisungen** | - Verzweigungen im Programmfluss<br>- Einrückung bestimmt den Rumpf der Anweisung<br>- Nur der erste zutreffende Fall wird bei elif ausgeführt |
| **if-Anweisung** | - Einfache Bedingung: `if bedingung:`<br>- Einrückung für den Rumpf notwendig<br>- Einzeilige Rümpfe können auch in die Kopfzeile geschrieben werden |
| **if-else** | - Alternative bei nicht zutreffender Bedingung<br>- `if bedingung:` ... `else:` |
| **if-elif-else** | - Fallunterscheidung mit mehreren Bedingungen<br>- Nur der erste zutreffende Fall wird durchlaufen<br>- `elif` für weitere Bedingungen, `else` als Default |
| **Boolesche Ausdrücke** | - Werten sich zu `True` oder `False` aus<br>- Werden in if-Anweisungen verwendet<br>- Ergebnis kann in Variablen gespeichert werden |
| **Vergleichsoperatoren** | - Größer: `>`<br>- Größer oder gleich: `>=`<br>- Kleiner: `<`<br>- Kleiner oder gleich: `<=`<br>- Gleichheit: `==`<br>- Ungleichheit: `!=` |
| **Boolesche Operatoren** | - `and`: Logisches UND (beide Bedingungen müssen wahr sein)<br>- `or`: Logisches ODER (mindestens eine Bedingung muss wahr sein)<br>- `not`: Logische Negation<br>- Auswertungsreihenfolge: `not`, `and`, `or` |
| **Bedingte Zuweisungen** | - Kurzform für if-else Zuweisungen<br>- Syntax: `variable = wert1 if bedingung else wert2`<br>- Beispiel: `status = 'gerade' if x % 2 == 0 else 'ungerade'` |

---

# Inhalte: 04_schleifen.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **while-Schleife** | - Rumpf wird solange durchlaufen, bis Bedingung `False` ist<br>- Syntax: `while bedingung:`<br>- Für unbekannte Anzahl von Durchläufen |
| **for-Schleife mit range()** | - Für bekannte Anzahl von Durchläufen<br>- `range(n)`: von 0 bis n-1<br>- `range(start, ende)`: von start bis ende-1<br>- `range(start, ende, schrittweite)`: mit bestimmter Schrittweite<br>- Ende-Wert ist immer ausgeschlossen |
| **Faustregel** | - For-Schleifen bei bekannter Anzahl von Durchläufen<br>- While-Schleifen bei unbekannter Anzahl |
| **break** | - Verlässt die Schleife sofort<br>- Fortsetzung hinter der Schleife<br>- Nur in Schleifen verwendbar<br>- Nützlich für Endlosschleifen mit Abbruchbedingung |
| **continue** | - Beendet den aktuellen Durchlauf<br>- Beginnt mit dem nächsten Durchlauf<br>- Nur in Schleifen verwendbar<br>- Überspringt bestimmte Werte |

---

# Inhalte: 05_strings2.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Leerer String** | - `s = ''`<br>- Länge ist 0 |
| **String vervielfachen** | - Mit `*` Operator<br>- Beispiel: `'Ha' * 3` ergibt `'HaHaHa'` |
| **Indexing** | - Positive Indizes: von vorne, beginnend bei 0<br>- Negative Indizes: von hinten, beginnend bei -1<br>- `s[0]`: erstes Zeichen, `s[-1]`: letztes Zeichen |
| **Slicing** | - Teilstrings extrahieren<br>- `s[:n]`: erste n Zeichen<br>- `s[-n:]`: letzte n Zeichen<br>- `s[start:ende]`: von start bis ende (ausschließlich)<br>- `s[n:]`: alles außer den ersten n Zeichen<br>- `s[:-n]`: alles außer den letzten n Zeichen |
| **String-Methoden** | - `upper()`: in Großbuchstaben<br>- `lower()`: in Kleinbuchstaben<br>- `count(teilstring)`: Anzahl Vorkommen<br>- `replace(alt, neu)`: Ersetzen eines Teilstrings<br>- `in`: Prüfen ob Teilstring vorkommt<br>- `not in`: Prüfen ob Teilstring nicht vorkommt |
| **String durchlaufen** | - Mit Index: `for i in range(len(s)):`<br>- Direkt über Zeichen: `for c in s:` |
| **ord() und chr()** | - `ord(zeichen)`: gibt die Zahl für ein Zeichen zurück<br>- `chr(zahl)`: gibt das Zeichen für eine Zahl zurück<br>- Ermöglicht Vergleich von Zeichen/Strings<br>- Für alphabetische Ordnung: Strings mit `lower()` oder `upper()` umwandeln |

---

# Inhalte: 06_listen.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Listen** | - Speichern mehrerer Werte<br>- Syntax: `a = [1, 2, 3]`<br>- Leere Liste: `a = []`<br>- Länge mit `len(a)` |
| **Vervielfachen** | - Mit `*` Operator<br>- Beispiel: `[0, 1] * 5` |
| **Indexing** | - Positive Indizes: von vorne, beginnend bei 0<br>- Negative Indizes: von hinten, beginnend bei -1<br>- Elemente können über Index verändert werden |
| **Slicing** | - Teillisten extrahieren<br>- `a[:n]`: erste n Elemente<br>- `a[-n:]`: letzte n Elemente<br>- `a[start:ende]`: von start bis ende (ausschließlich)<br>- `a[n:]`: alles außer den ersten n Elementen<br>- `a[:-n]`: alles außer den letzten n Elementen |
| **Hinzufügen/Entfernen** | - `append(element)`: Element am Ende hinzufügen<br>- `pop()`: letztes Element herausnehmen und zurückgeben<br>- Leere Liste hat booleschen Wert `False` |
| **Element suchen** | - `element in liste`: prüft ob Element vorhanden ist |
| **Sortieren** | - `sorted(liste)`: gibt sortierte Kopie zurück<br>- `sorted(liste, reverse=True)`: absteigende Sortierung |
| **Liste durchlaufen** | - Mit Index: `for i in range(len(a)):`<br>- Direkt über Elemente: `for x in a:` |
| **Funktionen für Zahlenlisten** | - `max(liste)`: Maximum<br>- `min(liste)`: Minimum<br>- `sum(liste)`: Summe |
| **split()** | - String in Liste umwandeln<br>- Trennung an Leerzeichen<br>- Beispiel: `'Dies ist ein Satz'.split()` |
| **Unpacking** | - Listenelemente in Variablen speichern<br>- Syntax: `x, y = [5, 2]`<br>- Anzahl Variablen muss mit Länge übereinstimmen |
| **List Comprehensions** | - Kompakte Erzeugung von Listen<br>- Syntax: `[ausdruck for variable in iterable]`<br>- Mit Bedingung: `[ausdruck for variable in iterable if bedingung]`<br>- Beispiel: `[x*x for x in range(1,10)]`<br>- Häufig: String mit Zahlen in Zahlenliste umwandeln |

---

# Inhalte: 07_dicts.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Dictionaries** | - Zugriff über **key** auf **value**<br>- Keys: ints, strings oder tuples<br>- Syntax: `m = {'key1': value1, 'key2': value2}`<br>- Leeres Dict: `m = {}` oder `m = dict()` |
| **Key-Value-Beziehung** | - Key kann nur einmal vorkommen<br>- Value kann mehrfach vorkommen<br>- Länge mit `len(m)` |
| **Zugriff auf Values** | - Mit Key: `m['key']`<br>- Fehler wenn Key nicht vorhanden |
| **Update von Values** | - `m['key'] = neuer_wert` |
| **Hinzufügen** | - `m['neuer_key'] = wert`<br>- Wenn Key noch nicht vorhanden, wird er hinzugefügt |
| **Entfernen** | - `m.pop('key')`: gibt Value zurück und löscht Eintrag |
| **Key vorhanden?** | - `'key' in m`: prüft ob Key im Dictionary ist |
| **Keys und Values** | - `m.keys()`: alle Keys<br>- `m.values()`: alle Values<br>- Mit `list()` in Liste umwandeln |
| **Dict durchlaufen** | - `for k in m:` durchläuft alle Keys<br>- Zugriff auf Value über `m[k]` |

---

# Inhalte: 08_tupel.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Tuples** | - Wie Listen, aber unveränderbar<br>- Syntax: `t = (3, 6, 1)`<br>- Leeres Tuple: `t = ()`<br>- Tuple mit einem Element: `t = (1,)` (Komma wichtig!) |
| **Was wie bei Listen funktioniert** | - Indexing (nur lesend)<br>- Slicing<br>- Durchlaufen mit Schleife<br>- Unpacking<br>- `element in tuple` |
| **Keine Veränderung** | - Kein `append()` oder `pop()`<br>- Keine Zuweisung über Index<br>- Für Änderungen: Umweg über Liste mit `list()` und `tuple()` |
| **Vorteil von Tuples** | - Können Keys von Dictionaries sein (Listen nicht)<br>- Unveränderbarkeit schützt Daten<br>- Oft schönere Darstellung, z.B. für Koordinaten |

---

# Inhalte: 09_functionen.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Funktionen** | - Fassen Codeabschnitte zu einer Einheit zusammen<br>- Syntax: `def funktionsname(parameter):`<br>- Rückgabe mit `return` |
| **Parameter und Rückgabewert** | - Funktionen können mehrere Parameter haben<br>- `return` gibt Wert zurück an Aufrufer<br>- Beispiel: `def calc(x, y): return x + y` |
| **Docstrings** | - Dokumentation der Funktion in dreifachen Hochkommata<br>- Beschreibt Parameter, Rückgabewert und Beispiele<br>- Wird direkt nach Funktionskopf geschrieben<br>- Format: Parameter-Beschreibung, returns, und >>> Beispiele |
| **Anwendungsbeispiele** | - Berechnungen durchführen<br>- Mit Listen arbeiten (z.B. Mittelwert berechnen)<br>- Bedingungen in Funktionen verwenden<br>- Funktionen können beliebige Datentypen zurückgeben |

---

# Inhalte: 10_dateizugriff.ipynb

| **Thema** | **Inhalt** |
|-----------|------------|
| **Datei öffnen und schließen** | - `open(dateiname)`: Datei zum Lesen öffnen<br>- `f.close()`: Datei nach Verarbeitung schließen<br>- Wichtig: Datei immer schließen nach Nutzung |
| **readline()** | - Liest eine Zeile aus der Datei<br>- Zeilenvorschub wird mit übernommen<br>- `strip()`: entfernt Zeilenvorschub und Leerzeichen |
| **read()** | - Liest gesamte Datei als String ein<br>- Zeilenvorschub bleibt erhalten |
| **encoding** | - Parameter `encoding='utf-8'` bei Umlauten/Sonderzeichen<br>- Beispiel: `open('datei.txt', encoding='utf-8')`<br>- Verhindert falsche Darstellung von ä, ö, ü, ß |
| **Einlesen von Daten** | - Zeilen mit `int()` oder `float()` in Zahlen umwandeln<br>- `split()`: Zeile in Liste aufteilen<br>- List Comprehensions für kompakte Umwandlung<br>- Unpacking für strukturierte Daten |
| **Schreiben in Datei** | - Parameter `mode='w'` beim Öffnen<br>- `print(..., file=f)`: schreibt in Datei statt Konsole<br>- Beispiel: `f = open('output.txt', encoding='utf-8', mode='w')`<br>- f-Strings für formatierte Ausgabe |
| **Typische Muster** | - Erste Zeile gibt Anzahl folgender Zeilen an<br>- Alle Zahlen in einer Zeile mit Leerzeichen getrennt<br>- Strukturierte Daten mit mehreren Werten pro Zeile |
