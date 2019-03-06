# based on approach from Paul Vierthaler (https://github.com/vierth/humanitiesTutorial ) --> will be replaced by own version later
import re, nltk, os
from pandas import DataFrame
import numpy as np

# The components for analysis:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances
from scipy.cluster.hierarchy import linkage, dendrogram

# The components for viz
import matplotlib.pyplot as plot

MFW = 1000
ngram = (1, 3)
hcaAlgorithm = 'ward'
culling = 'no'


# TODO: in the end think of best way how to access different corpora
# The vectorizor object wants a list of texts, so we will prepare one for it
sherlockTexts = []
sherlockTitles = []
for root, dirs, files in os.walk("corpus2"):
    for filename in files:
        with open(os.path.join(root,filename)) as rf:
            sherlockTexts.append(rf.read().lower())
            sherlockTitles.append(filename[:-4].lower())
                


# Frequencies of the x most common n-grams in the corpus
# n-grams can be indicated as ranges, e.g. (1, 3) includes ngrams from 1 to 3
# n-grams can also be indicated as single numbers, e.g. (3, 3) includes only 3-grams
# max_features = MFWs
# TODO: include culling
# TODO: consider console parameter for values OR:
# TODO: consider automation process (e.g. count from 500 to 3000 features, 1-3-gram, etc) and save the images etc
countVectorizer = TfidfVectorizer(max_features=MFW, use_idf=False, ngram_range= ngram)
print(countVectorizer)
countMatrix = countVectorizer.fit_transform(sherlockTexts)
print(countMatrix)

# distance measure provided by methods from sklearn:
# manhattan_distances = burrows delta
# euclidean_distances = quadratic delta (argamon 2008)
# beim vergleich der anwälte liefert euclidean metric bessere ergebnisse
similarity = manhattan_distances(countMatrix)
print(similarity)


# Hierarchical Cluster Analysis, i.e. grouping of nearest documents and
# display in dendrogram
# TODO: evaluate which algorithm is best for us
linkages = linkage(similarity, hcaAlgorithm)
fig = dendrogram(linkages, labels=sherlockTitles, orientation="left", leaf_font_size=8,leaf_rotation=0)

plot.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
plot.title(str(MFW) + " MFW " + str(ngram) + " ngram " + "no culling" )
plot.tight_layout()

plot.show()





