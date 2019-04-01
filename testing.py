import string
import re
from nltk.corpus import stopwords
STOPWORDS = stopwords.words('german')
#print(STOPWORDS)
from nltk.stem.wordnet import WordNetLemmatizer
from pywsd.utils import lemmatize, lemmatize_sentence
from collections import Counter
import nltk
from pattern.de import parse, split


translator = str.maketrans('','', string.digits)
s="' x z  uv aber 12 Juni 2018 alle 1  „Vorlage zur Vorabentscheidung – Art 49 AEUV – Körperschaftsteuer – Niederlassungsfreiheit – Gebietsansässige Gesellschaft – Steuerpflichtiger Gewinn – Steuerliche Entlastung – Abzug der Verluste gebietsansässiger Betriebsstätten – Bewilligung – Abzug der Verluste gebietsfremder Betriebsstätten – Ausschluss – Ausnahme – Fakultative Regelung der internationalen gemeinsamen Besteuerung“" \
  "In der Rechtssache C‑65016 " \
  "betreffend ein Vorabentscheidungsersuchen nach Art 267 AEUV eingereicht vom Østre Landsret Landgericht der Region Ost Dänemark mit Entscheidung vom 12 Dezember 2016 beim Gerichtshof eingegangen am 19 Dezember 2016 in dem Verfahren" \
  "AS Bevola" \
  "Jens W Trock ApS' und"

# print(re.sub(r'[^\w\s]','',s))

# print(s.translate(translator).lower())

#no_numbers_lower = s.translate(translator).lower()
#no_whitespace = " ".join(no_numbers_lower.split())
#print(no_whitespace)

#no_stopwords = []
#words = no_whitespace.split()
#lemmatized = []

#lemmatizer = WordNetLemmatizer()
'''

for word in words:

  lemmatized.append(lemmatizer.lemmatize(word))

text_for_output = ' '.join(lemmatized)
#print(lemmatized)
#print(text_for_output)


sentence = "Hallo ich heiße Anna und studiere in Regensburg. Ich spiele gerne Handball und treffe meine Freunde."
print(lemmatize_sentence(sentence))
print(lemmatizer.lemmatize(sentence))'''



testsentence = "hallo du da wie geht es dir ich hoffe dir geht es gut ich mag dich vielleicht sehr gerne"
#counter = Counter()
words  = re.findall(r'\w+', testsentence)
print(words)
#word_counts = Counter(words)
#print(word_counts.most_common(3))
#lemmas = nltk.pos_tag(words, "STTS")
#print(lemmas)
s = parse("hallo du da wie geht es dir ich hoffe dir geht es gut ich mag dich vielleicht sehr gerne", tagset = "STTS")
for sentence in split(s):
  print(sentence)