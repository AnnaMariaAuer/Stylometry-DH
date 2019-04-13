# Stylometry-DH

## Von der Abschlusspräsentation zur Abgabe

Aufgrund der in der Abschlusspräsentation kritisierten Vorgehensweise des Verwendens von n-grams auf Wortebene haben wir uns entschlossen, die Analysen erneut mit Hilfe von n-grams auf Characterebene durchzuführen. Dadurch konnten bessere Cluster erzielt werden, weshalb wir unsere ersten Ergebnisse auf Wortebene überschrieben und mit denen auf Characterebene ersetzt haben. Die berechneten Visualisierungen befinden der Subkorpora entsprechend untergliedert im Ordner "results_stylometry".

## Installationsanweisungen
Die hier beschriebenen Installationsanweisungen beziehen sich auf das Betriebssystem Windows 10.
In diesem Repository sind bereits alle Ergebnisse zu dem hier analysierten Korpus abgelegt. Es ist jedoch möglich, mit Hilfe des Programms eigene Korpora stilometrisch zu analysieren.

1. Installation von Python 3.7
https://www.python.org/downloads/windows/

2. Asführen des Projekts
  * Das Projekt befindet sich beispielhaft unter dem Pfad “C:\Users\name\Documents\Project”
  * Das Skript create_corpora.py dient zum Pre-Processing der Korpora. Bei bedarf können alle txt-Dateien zu einer einzelnen zusammengefügt werden. Es werden Interpunktionen, Zahlen und zusätzliche Whitespaces entfernt. Eine zusätzliche Entfernung von Stopwords ist möglich. Außerdem kann die durchschnittliche Wortlänge der einzelnen Dokumente berechnet werden.
  * Alle verwendeten Packages müssen ggf. mit Hilfe von "pip3 install ..." heruntergeladen werden
  * Um ein Skript auszuführen, müssen Sie in der Konsole zum Pfad des Projekts navigieren und mit "python.exe create_corpora.py das Programm ausführen
  * Der nächste Schritt sit die Generierung von Culling-Dokumenten, Berechnung der Stilometrie und Ausgabe der Visualisierungen
  * Erstellen der Culling-Dokumente (Dauer: mehrere Stunden, abhängig von Korpusgröße)
    * Navigieren in den Projektordner mit Hilfe der Konsole und Ausführen des Befehls "python.exe stylometry.py culling"
    * Das Skript iteriert über alle Korpora, die sich in dem Subordner "corpus" befinden
    * Für jedes Korpus wird automatisch eine Textdatei im Subordner "culling_preprocessing" erstellt, welche alle Wörter enthält, die nach dem Prinzip des Culling aus den finalen Korpora entfernt werden sollen.
    * Sobald alle Dokumente ausgegeben worden sind, wird das Programm in der Kommandozeile automatisch geschlossen.
  * Stilometrische Berechnung und Ausgabe der Visualisierungen
    * Starten der Windows-Kommandozeile und navigieren in den Projektordner
    * Ausführen des Skripts mit dem Befehl "python.exe stylometry.py"
    * Skript iteriert über alle Korpora, die sich im Subordner "corpus" befinden. Für jedes Korpus werden automatisch stilometrische Berechnungen mit Hilfe der vordefinierten Parameter durchgeführt. Diese Parameter werden iteriert und besitzten eine vordefinierte Unter- und Obergrenze.
    * Pro Parameter-Kombination in einem Korpus werden Dendrogramm-Visualisierungen erstellt und im Subordner "results_stylometry" ausgegeben.
    * Sobald alle Berechnungen und Visualisierungen ausgegeben wurden, schließt sich das Programm in der Kommandozeile.
    * Auf diese Weise werden 1800 Visualisierungen in ca. 45 Minuten ausgegeben.
