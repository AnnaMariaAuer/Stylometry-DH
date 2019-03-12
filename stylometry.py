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
        self.cull_percentage = 10
        self.document_contents = []
        self.document_titles = []
        self.load_corpus()
        # TODO: solve method calling via command line parameter
        #self.preprocess_culling()
        self.apply_culling()
        self.apply_stylometry()
        self.visualize_results()


    def load_corpus(self):
        # TODO: in the end think of best way how to access different corpora
        for root, dirs, files in os.walk("corpus"):
            for filename in files:
                label = os.path.splitext(filename)
                f = open(os.path.join(root, filename), 'r')
                self.document_contents.append(f.read().lower())
                # remove ".txt" ending of files to obtain names
                self.document_titles.append(label[0])
                f.close()

    def apply_culling(self):
        # removes all culled words from the corpus based on the culling file created
        # in the method preprocess_culling

        # get file with culling words
        culling_list_file = open("culled_words_" + str(self.cull_percentage) + ".txt", 'r')
        # split file along lines
        culling_list = culling_list_file.read().splitlines()

        # testing: word amount needs to be higher than after culling --> successful
        #davor = nltk.word_tokenize(self.document_contents[0])
        #davor1 = nltk.word_tokenize(self.document_contents[1])


        # iteratate over each word in the culling list and remove it from all documents
        for word in culling_list:
            # needs to be written this way (self.document_contents[i]), otherwise not applicated
            for i in range(len(self.document_contents)):
                self.document_contents[i] = self.document_contents[i].replace(word, "")
        culling_list_file.close()

        # testing cf. above
        #danach = nltk.word_tokenize(self.document_contents[0])
        #danach1 = nltk.word_tokenize(self.document_contents[1])
        #print(str(len(davor)) + " - " + str(len(danach)))
        #print(str(len(davor1)) + " - " + str(len(danach1)))


    def preprocess_culling(self):
        # applies culling, i.e. identifies words that should not be taken into account
        # for stylometry calculations
        # A word should be removed, if it does not occur in min. X percent of all documents

        # calculate amount of docs based on the selected culling percentage
        min_word_amount = (self.cull_percentage*len(self.document_contents))/100
        min_word_amount_rounded = round(min_word_amount)

        #create file for saving words to be removed
        culledWords = open("culled_words_"+str(self.cull_percentage)+".txt", "w+")

        all_words = []
        # iterate over all documents and create a list with all unique words of all documents
        for document in self.document_contents:
            words = nltk.word_tokenize(document)
            unique_words = set(words)
            unique_words_list = list(unique_words)
            for word in unique_words_list:
                all_words.append(word)

        # iterate over unique wordlist and check how often words occur in the documents
        for word in all_words:
            # counts the amount of documents where the word is not contained
            doc_counter = 0

            # iterate over all documents
            for doc in self.document_contents:
                words_current_doc = nltk.word_tokenize(doc)
                freq_words_curr_doc = FreqDist(words_current_doc)

                # if the current word does not occur in the current document
                if freq_words_curr_doc[word]==0:
                    doc_counter = doc_counter + 1
                    print("Kommt nicht vor in "+ str(doc_counter)+" Dokumenten "+  " ->Wort:"+word)

                    # if the current word occurs less than in X percent of all documents
                    if len(self.document_contents) - doc_counter < min_word_amount_rounded:
                        print(word +" entfernt, weil nicht in " + str(self.cull_percentage) + "% der Dokumente")
                        # add word to to-remove list
                        culledWords.write(word+" \n")
                        # don't iterate this word anymore over other documents
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
        plot.title(str(self.MFW) + " MFW " + str(self.ngram_range_min) + "-" + str(self.ngram_range_max) + "-gram " + str(self.cull_percentage)+"% culling " + " Euclidean"  )
        plot.tight_layout()
        plot.show()

def main():
    calculateStylometry = Stylometry()


if __name__ == '__main__':
    main()

