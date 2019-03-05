import string
import re

translator = str.maketrans('','', string.digits)
s="'12 Juni 2018  1  „Vorlage zur Vorabentscheidung – Art 49 AEUV – Körperschaftsteuer – Niederlassungsfreiheit – Gebietsansässige Gesellschaft – Steuerpflichtiger Gewinn – Steuerliche Entlastung – Abzug der Verluste gebietsansässiger Betriebsstätten – Bewilligung – Abzug der Verluste gebietsfremder Betriebsstätten – Ausschluss – Ausnahme – Fakultative Regelung der internationalen gemeinsamen Besteuerung“" \
  "In der Rechtssache C‑65016 " \
  "betreffend ein Vorabentscheidungsersuchen nach Art 267 AEUV eingereicht vom Østre Landsret Landgericht der Region Ost Dänemark mit Entscheidung vom 12 Dezember 2016 beim Gerichtshof eingegangen am 19 Dezember 2016 in dem Verfahren" \
  "AS Bevola" \
  "Jens W Trock ApS'"

print(re.sub(r'[^\w\s]','',s))

print(s.translate(translator).lower())

no_numbers_lower = s.translate(translator).lower()
no_whitespace = " ".join(no_numbers_lower.split())
print(no_whitespace)