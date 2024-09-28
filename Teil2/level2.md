
```
tags: #teiler, #string, #loop, #range, #zählen, #indexing, #slicing, #contains
#list, #split, #conversion, #modulo, #comprehension

Aufgabe 2:
Lies eine Zahl x ein
Falls x durch 2 teilbar: Gib aus '2 ist Teiler'
Falls x durch 3 teilbar: Gib aus '3 ist Teiler'
Falls x durch 5 teilbar: Gib aus '5 ist Teiler'
Falls x durch 7 teilbar: Gib aus '7 ist Teiler'
Falls x durch 11 teilbar: Gib aus '11 ist Teiler'
#teiler


Aufgabe 3
Das Programm liest eine Zahl ein und gibt 
dann die Teiler zurück.  
#teiler

Aufgabe 4
Lies eine ganze Zahl k > 2 ein.
Gib ein k x k Quadrat mit '#'-Rändern aus.
#string

Aufgabe 5
Lies in einer Zeile zwei ganze Zahlen a, b ein und ermittle die Summe aller
Zahlen k zwischen a und b, also a <= k <= b. 
#range

Aufgabe 6
Lies eine ganze Zahl k > 0 ein und gib die Multiplikationstabelle aus.  
#range

Aufgabe 7:
Lies einen String s ein. Dann lies ein einzelnes Zeichen c ein. 
Gib aus, wieviel mal das Zeichen c im String s vorkommt.
#string, #string #loop

Aufgabe 8:
Lies einen String s ein.
Gib die Anzahl der Zeichen aus, bei denen das nachfolgende Zeichen das Gleiche ist.
#string, #stringloop, #zählen

Aufgabe 9:
Lies eine String s ein. 
Gib nacheinander Zeichen mit ihren Nachfolgern aus (Teilstrings der Länge 2)
#string #indexing

Aufgabe 10:
Lies eine String s ein. 
Gib nacheinander die vorne beginnenden Teilstrings aus.
#string #slicing

Aufgabe 11:
Lies eine String s ein. 
Gib nacheinander die hinten endenden Teilstrings aus.
#string #slicing

Aufgabe 12:
Lies eine String s ein und einen weiteren String s0 ein. 
Wenn s0 in s vorkommt, gib 'YES' aus, ansonsten 'NO'.
#string #contains

Aufgabe 13:
Lies eine Folge von mindestend 2 Zahlen ein.
Erzeuge dann eine Liste mit den Summen zweier aufeinanderfolgender Zahlen.
Wenn die Liste weniger als 2 Elemente enthält, gib aus: 'zu kurz'
#list #indexing

Aufgabe 14:
Lies eine Folge von Zahlen ein
Gib alle Teillisten aus, die mit 3 beginnen und bis zum Ende gehen.
#list #slicing

Aufgabe 15:
Lies einen String s ein
Lies ein Trennzeichen c ein.
Gib die Liste a aus, die die Bestandteile von s enthält, wenn man c als Trennzeichen nutzt
#string #list #split

Aufgabe 16:
Lies einen Satz mit mehreren Worten ein, die durch Leerzeichen getrennt sind
Gib den Satz aus mit einem '+' zwischen den Worten.
#string  #replace

Aufgabe 17:
Lies einen Satz mit mehreren Worten ein, die durch Leerzeichen getrennt sind
Gib den Satz ohne Leerzeichen aus. 
#string  #replace

Aufgabe 18:
Gib in einer Zeile ein ganze Zahl ein.
Gib die Liste mit den Ziffern aus.
#conversion #string #list

Aufgabe 19:
Gib in einer Zeile eine positive ganze Zahl ein.
Gib die Quersumme der Zahl aus.
#conversion #string #loop

Aufgabe 20:
Lies positive ganze Zahl n ein.
Gib die Summe aller ihrer geraden Ziffern aus.
Nutze eine for-Schleife ohne Index.
#conversion #loop #modulo

--- Level 2 -----

Aufgabe 1:
Schreibe eine Funktion func1, der ein String s und ein Index k übergeben wird und die
eine Liste mit den beiden Teilstrings vor und nach der Stelle k zurückgibt.
#string, #slicing, #list

Aufgabe 2:
Schreibe eine Funktion func2, der eine Liste a mit ints und ein int k übergeben wird und die
'YES' zurück, wenn in a mindestens k gerade Zahlen sind.
#list #loop

Aufgabe 3:
Schreibe eine Funktion func3, der ein String s übergeben wird und die den längsten Teilstring von hinten in
s zurückgibt, der kein '.' enthält
#string #loop 

Aufgabe 4:
Schreibe eine Funktion func4, der eine Liste a mit Strings und eine String s übergeben wird 
und die 'YES' returned, wenn s als Teilstring in einer der Strings in Liste a vorkommt, sonst 'NO'.
#list #loop #contains

Aufgabe 5:
Schreibe eine Funktion func5, der eine Liste mit Strings übergeben wird und die eine Liste mit diesen
Strings in umgekehrter Reihenfolge zurückgibt.
#list 

Aufgabe 6:
Schreibe eine Funktion func6, der ein String s und ein int k übergeben wird und 
die einen String zurückgibt, der aus s dadurch entsteht, dass das erste 
Auftreten von 'o' in s k-mal wiederholt wird.
#list #index

Aufgabe 7:
Schreibe eine Funktion func7, der eine String s und zwei Zeichen c1 und c2 übergeben werden
und die das Zeichen c1 oder c2 zurückgibt, das als erstes in s vorkommt. Wenn keines der Zeichen vorkommt,
soll False zurückgegeben werden.
#list #index

Aufgabe 8:
Schreibe eine Funktion func8, der ein String s übergeben wird der nur aus '0' und '1' besteht und 
die 'YES' zurückgibt wenn 1 häufiger in s vorkommt als 0, sonst 'NO'.
#string #count

Aufgabe 9:
Schreibe eine Funktion func9, der ein String s und eine Zahl k übergeben wird und die
eine Liste zurückgibt, in der s 1..k mal wiederholt wird.
#list #string

Aufgabe 10:
Schreibe eine Funktion func10, der eine Liste a mit Zahlen übergeben und die die Differenz
zwischen dem größten und kleinsten Element zurückgibt.
#list #min #max

Aufgabe 11:
Schreibe eine Funktion func11, der eine Liste a mit Zahlen übergeben wird und eine Zahl k
und die 'YES' returned, wenn k größer als alle Zahlen in a ist, sonst 'NO'.
#list #max

Aufgabe 12:
Schreibe eine Funktion func12, der eine Liste a mit Zahlen übergeben wird und die
den Durchschnittswert der Zahlen in a zurückgibt.
#list #sum

Aufgabe 13:
Schreibe eine Funktion func13, der eine Liste a mit Zahlen übergeben wird und
die eine Liste zurückgibt, in der alle geraden Zahlen von a in umgedrehter Reihenfolge
vorkommen.
#list #modulo

Aufgabe 14:
Schreibe eine Funktion func14, der eine Liste a von Zahlen übergeben wird und die eine Liste
zurückgibt mit allen Zahlen von a aufwärts sortiert, dann abwärts sortiert.
#list #sort

Aufgabe 15
Schreibe eine Funktion func15, der eine Liste a mit Zahlen übergeben wird, und die eine Liste zurückgibt, 
in der alle Zahlen aus a verdoppelt sind.
Nutze eine List-Comprehension.
#list #comprehension

Aufgabe 16:
Schreibe eine Funktion func16, der eine positive Zahl k übergeben wird die eine
Liste mit allen Quadraten der Zahlen von 1 bis k zurückgibt.
Nutze eine List-Comprehension.
#list #range #comprehension

Aufgabe 17:
Schreibe eine Funktion func17, der ein String s übergeben wird und die eine Liste mit
den ASCII-Nummern der Zeichen von s zurückgibt.
#string #ord

Aufgabe 18:
Schreibe eine Funktion func18, der eine Liste mit ASCII-Zahlen übergeben wird und
die den dazugehörigen String zurückgibt.
#string #chr

Aufgabe 19:
Schreibe eine Funktion func19, der ein String mit kleinen Buchstaben des englischen Alphabets 
und ein Zeichen c übergeben werden und die die Anzahl Zeichen in s zurückgibt, die alphabetisch vor c
vorkommen.
#string #loop #zählen

Aufgabe 20:
Schreibe eine Funktion func20, der ein kleiner Buchstabe des englischen Alphabets übergeben wird
und die den nächsten Buchstaben zurückgibt. Falls c ein 'z' ist, soll 'a' ausgegeben werden.
#string #ord #chr

Aufgabe 21:
Schreibe eine Funktion func21, der eine positive ganze Zahl k übergeben wird und die
eine dictionary zurückgibt, dass jeder Zahl von 1..k 'YES' zuordnet, falls die Zahl gerade, sonst 'NO'.
#dict #modulo #range

Aufgabe 22:
Schreibe eine Funktion func22, der eine Liste a mit Strings übergeben wird und die ein dictionary 
zurückgibt, das jedem String in a seine Länge zuordnet.
#dict #string #len

Aufgabe 23:
Schreibe eine Funktion func23, der ein String s übergeben wird und die ein dictionary zurückgibt,
das jedem Zeichen c in s die Häufigkeit seines Vorkommens in s zuordnet.
#dict #string 
 

