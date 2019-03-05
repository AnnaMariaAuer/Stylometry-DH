import string
import re
from nltk.corpus import stopwords
STOPWORDS = stopwords.words('german')
print(STOPWORDS)

translator = str.maketrans('','', string.digits)
s="' aber 12 Juni 2018 alle 1  „Vorlage zur Vorabentscheidung – Art 49 AEUV – Körperschaftsteuer – Niederlassungsfreiheit – Gebietsansässige Gesellschaft – Steuerpflichtiger Gewinn – Steuerliche Entlastung – Abzug der Verluste gebietsansässiger Betriebsstätten – Bewilligung – Abzug der Verluste gebietsfremder Betriebsstätten – Ausschluss – Ausnahme – Fakultative Regelung der internationalen gemeinsamen Besteuerung“" \
  "In der Rechtssache C‑65016 " \
  "betreffend ein Vorabentscheidungsersuchen nach Art 267 AEUV eingereicht vom Østre Landsret Landgericht der Region Ost Dänemark mit Entscheidung vom 12 Dezember 2016 beim Gerichtshof eingegangen am 19 Dezember 2016 in dem Verfahren" \
  "AS Bevola" \
  "Jens W Trock ApS' und"

# print(re.sub(r'[^\w\s]','',s))

# print(s.translate(translator).lower())

no_numbers_lower = s.translate(translator).lower()
no_whitespace = " ".join(no_numbers_lower.split())
print(no_whitespace)

no_stopwords = []
words = no_whitespace.split()

for word in words:
  print(word)
  if word not in STOPWORDS:
    no_stopwords.append(word)

text_for_output = ' '.join(no_stopwords)
print(no_stopwords)
print(text_for_output)
