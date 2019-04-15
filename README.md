# Stylometry-DH

## Von der Abschlusspräsentation zur Abgabe

Aufgrund der in der Abschlusspräsentation kritisierten Vorgehensweise des Verwendens von n-grams auf Wortebene haben wir uns entschlossen, die Analysen erneut mit Hilfe von n-grams auf Characterebene durchzuführen. Dadurch konnten bessere Cluster erzielt werden, weshalb wir unsere ersten Ergebnisse auf Wortebene überschrieben und mit denen auf Characterebene ersetzt haben. Die berechneten Visualisierungen befinden der Subkorpora entsprechend untergliedert im Ordner "results_stylometry".

## Installationsanweisungen
Die hier beschriebenen Installationsanweisungen beziehen sich auf das Betriebssystem Windows 10.
In diesem Repository sind bereits alle Ergebnisse zu dem hier analysierten Korpus abgelegt. Es ist jedoch möglich, mit Hilfe des Programms eigene Korpora stilometrisch zu analysieren.

1. Installation von Python 3.7
* Download der Installationsdatei unter https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe und Ausführung durch Doppelklick
* Auswahl von "Customize installation" und Anwählen von "Add Python 3.7 to PATH"
* Im nächsten Fenster auf "Next"
* Im nächsten Fenster Anwählen von "Precompile standard library" und Anpassen des Installationsziels (hier beispielhaft: C:\Python_3.7)
* Nach Installation Starten der Windows-Kommandozeile und Navigation in den Ordner C:\Python_3.7\Scripts für die Installation aller benötigten Packages
* Eingabe folgender Befehle: `pip install nltk`, `pip install germalemma`, `pip install pandas`, `pip install sklearn`, `pip install matplotlib`, `python.exe()`, `import nltk`, `nltk.download('punkt')`, `nltk.download('stopwords')`



2. Ausführen des Projekts
  * Das Projekt befindet sich beispielhaft unter dem Pfad “C:\Users\name\Documents\Project”
  
  * Ausführung des Skripts für die Generierung der Korpora und Anwendung der Methoden des Text-Preprocessings
  * Das Skript create_corpora.py dient zum Pre-Processing der Korpora. Bei bedarf können alle txt-Dateien zu einer einzelnen zusammengefügt werden. Es werden Interpunktionen, Zahlen und zusätzliche Whitespaces entfernt. Eine zusätzliche Entfernung von Stopwords ist möglich. Außerdem kann die durchschnittliche Wortlänge der einzelnen Dokumente berechnet werden.
  * Starten der Windows-Kommandozeile 
 * Navigieren in den Projektordner unter dem oben beschriebenen Pfad “C:\Users\name\Documents\Project”
* Ausführen des Skripts mit dem Befehl: python.exe create_corpora.py

2.2 Ausführung des Skripts für die Generierung von Culling-Dokumenten, Berechnung der Stilometrie und Ausgabe der Visualisierungen
Zunächst müssen alle Dateien generiert werden, die Culling-Dokumente erstellen. Dies ist unabhängig von der Stilometrie-Berechnung, da die Generierung sehr lange dauert (je nach Computerumgebung und Korpuslänge bis zu 2 Stunden pro Dokument)
* Für die Generierung der Culling-Dokumente
** Starten der Windows-Kommandozeile 
** Navigieren in den Projektordner unter dem oben beschriebenen Pfad
** Ausführen des Skripts mit dem Befehl: python.exe stylometry.py culling
    * Das Skript iteriert über alle Korpora, die sich in dem Subordner "corpus" befinden
    * Für jedes Korpus wird automatisch eine Textdatei im Subordner "culling_preprocessing" erstellt, welche alle Wörter enthält, die nach dem Prinzip des Culling aus den finalen Korpora entfernt werden sollen.
    * Sobald alle Dokumente ausgegeben worden sind, wird das Programm in der Kommandozeile automatisch geschlossen.
*  In unserem Projekt wurden auf diese Weise 27 Culling-Dokumente generiert mit einer Processing-Dauer von insgesamt 54 Stunden
  
  
  * Für die Stilometrische Berechnung und Ausgabe der Visualisierungen
    * Starten der Windows-Kommandozeile 
Navigieren in den Projektordner unter dem oben beschriebenen Pfad
Ausführen des Skripts mit dem Befehl: 
python.exe stylometry.py

    * Skript iteriert über alle Korpora, die sich im Subordner "corpus" befinden. Für jedes Korpus werden automatisch stilometrische Berechnungen mit Hilfe der vordefinierten Parameter durchgeführt. Diese Parameter werden iteriert und besitzten eine vordefinierte Unter- und Obergrenze.
    * Pro Parameter-Kombination in einem Korpus werden Dendrogramm-Visualisierungen erstellt und im Subordner "results_stylometry" ausgegeben.
    * Sobald alle Berechnungen und Visualisierungen ausgegeben wurden, schließt sich das Programm in der Kommandozeile.
    * Auf diese Weise werden 1800 Visualisierungen in ca. 45 Minuten ausgegeben.
