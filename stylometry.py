# based on approach from Paul Vierthaler (https://github.com/vierth/humanitiesTutorial ) --> will be replaced by own version later
import re, nltk, os
from pandas import DataFrame
from nltk.probability import FreqDist
from nltk import word_tokenize
import numpy as np
import math
from collections import Counter

# The components for analysis:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances
from scipy.cluster.hierarchy import linkage, dendrogram

# The components for viz
import matplotlib.pyplot as plot



class Stylometry():
    def __init__(self):
        super().__init__()
        self.MFW = 1000
        self.ngram_range_min = 1
        self.ngram_range_max = 3
        self.hcaAlgorithm = 'ward'
        self.culling = 'no'
        self.document_contents = []
        self.document_titles = []
        self.load_corpus()
        self.apply_culling(10)
        self.apply_stylometry()
        self.visualize_results()



    def load_corpus(self):
        # TODO: in the end think of best way how to access different corpora
        for root, dirs, files in os.walk("corpus"):
            for filename in files:
                label = os.path.splitext(filename)
                f = open(os.path.join(root, filename), 'r')
                content_of_file = f.read()
                self.document_contents.append(content_of_file.lower())
                # remove ".txt" ending of files to obtain names
                self.document_titles.append(label[0])
                f.close()


    def apply_culling(self, cull_percentage):
        # = wenn ein Wort nicht min. in x docs auftritt wird es entfernt
        # aus der liste
        # 1. ausrechnen : in wie vielen texten muss es min auftreten?
        # 2. unique words in liste bekommen
        # 3. uniquewords iterieren und schauen, in wie vielen texten es vorkommt
        # 4. wenn anzahl < 1.) dann weg

        min_word_amount = (cull_percentage*len(self.document_contents))/100
        min_word_amount_rounded = round(min_word_amount)
        culledWords = open("culled_words_"+str(cull_percentage)+".txt", "w+")

        all_words = []
        # liste aller docs iterieren und eine liste mit allen wörtern erstellen
        for document in self.document_contents:
            words = nltk.word_tokenize(document)
            for word in words:
                all_words.append(word)





        fdistAll = FreqDist(all_words)
        print(min_word_amount_rounded)



        for word in all_words:
            doc_counter = 0

            for doc in self.document_contents:
                wordsindoc0 = nltk.word_tokenize(doc)
                fdist0Doc = FreqDist(wordsindoc0)

                # kommt nicht in doc 0 vor
                if fdist0Doc[word]==0:
                    #print(len(self.document_contents))
                    #print(doc_counter)
                    # 21-17 muss kleiner sein als 4 --> dann weg
                    doc_counter = doc_counter + 1

                    print("Kommt nicht vor in "+ str(doc_counter)+" Dokumenten "+  " ->Wort:"+word)
                    if len(self.document_contents) - doc_counter < min_word_amount_rounded:
                        #print(doc_counter)
                        print(word +" entfernt, weil nicht in " + str(cull_percentage) + "% der Dokumente")
                        culledWords.write(word+" \n")
                        break






        culledWords.close()

















    def apply_stylometry(self):
        # Frequencies of the x most common n-grams in the corpus
        # n-grams can be indicated as ranges, e.g. (1, 3) includes ngrams from 1 to 3
        # n-grams can also be indicated as single numbers, e.g. (3, 3) includes only 3-grams
        # max_features = MFWs
        # TODO: include culling
        # TODO: consider console parameter for values OR:
        # TODO: consider automation process (e.g. count from 500 to 3000 features, 1-3-gram, etc) and save the images etc
        countVectorizer = TfidfVectorizer(max_features=self.MFW, use_idf=False, ngram_range=(self.ngram_range_min, self.ngram_range_max))
        countMatrix = countVectorizer.fit_transform(self.document_contents)

        # distance measure provided by methods from sklearn:
        # manhattan_distances = burrows delta
        # euclidean_distances = quadratic delta (argamon 2008)
        # beim vergleich der anwälte liefert euclidean metric bessere ergebnisse
        similarity = euclidean_distances(countMatrix)

        # Hierarchical Cluster Analysis, i.e. grouping of nearest documents and
        # display in dendrogram
        # TODO: evaluate which algorithm is best for us
        linkages = linkage(similarity, self.hcaAlgorithm)
        fig = dendrogram(linkages, labels=self.document_titles, orientation="left", leaf_font_size=8, leaf_rotation=0)


    def visualize_results(self):
        plot.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
        plot.title(str(self.MFW) + " MFW " + str(self.ngram_range_min) + "-" + str(self.ngram_range_max) + "-gram " + "no culling " + " Euclidean"  )
        plot.tight_layout()
        plot.show()

def main():
    calculateStylometry = Stylometry()


if __name__ == '__main__':
    main()

