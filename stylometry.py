import re, nltk, os
from pandas import DataFrame
from nltk.probability import FreqDist
from nltk import word_tokenize
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import sys
import math
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances
import matplotlib.pyplot as plot


class Stylometry():
    def __init__(self):
        super().__init__()
        self.corpus_type = "corpus_type"
        self.corpus_category = "corpus_category"
        self.init_variables()
        self.load_corpus()    

        
    def init_variables(self):
        self.MFW = 0
        self.ngram_range_min = 2
        self.ngram_range_max = 2
        self.hcaAlgorithm = 'ward'
        self.cull_percentage = 0
        self.delta = "Burrow's"
        self.document_contents = []
        self.document_titles = []

    def load_corpus(self):
        folders = []
        files = []
        for corpus_type in os.scandir('corpus'):
            if corpus_type.is_dir():
                self.corpus_type = corpus_type.name
                #print(self.corpus_type)
                for category in os.scandir(corpus_type):
                    self.corpus_category = category.name
                    #print(self.corpus_category)
                    for file in os.scandir(category):
                        # remove ".txt" suffix of files
                        label = file.name.split(".")[0]
                        f = open(os.path.join("", file), 'r', encoding="utf8")
                        self.document_contents.append(f.read().lower())
                        self.document_titles.append(label)
                        f.close()
                    self.start_application()
                    self.init_variables()




    def start_application(self):
        if len(sys.argv) > 1:
            if sys.argv[1] == "culling":
                print("Culling process started. This will take a few minutes.")
                print("Please wait until the program is closed automatically.")
                print("The list with culled words can be found in folder culling_preprocessing.")
                for percentage in range(3):
                    self.preprocess_culling()
                    self.cull_percentage = self.cull_percentage + 10
            else:
                print("The passed parameter could not be recognized.")
        else:
            print("Stylometry will be calculated.")
            print("This will take a few minutes.")
            print("Please wait until the program is closed automatically.")
            print("The output visualizations can be found in the folder results_stylometry.")
            # iterate mfw from 100 to 1000 with stepsize 100
            for mfw_increment in range(10):
                # increase MFW by 100
                self.MFW = self.MFW + 100
                # reset cull percentage
                self.cull_percentage = -10

                # iterate culling from 0 to 20 % with stepsize 10
                for cull_increment in range(3):
                    self.ngram_range_max =2
                    self.cull_percentage = self.cull_percentage + 10

                    # iterate upper range limit for ngram from 3 to 5 with stepsize 1
                    for ngram_range_max_increment in range(3):
                        self.ngram_range_max = self.ngram_range_max + 1
                        self.ngram_range_min=2

                        # iterate lower range limit for ngram from 3 to 5 with stepsize 1
                        for ngram_range_min_increment in range(3):
                            self.ngram_range_min = self.ngram_range_min + 1

                            # lower range limit must be smaller than higher limit
                            if ngram_range_max_increment >= ngram_range_min_increment:
                                culled_docs = self.apply_culling()
                                self.apply_stylometry(culled_docs)
                                self.visualize_results()


                

    def apply_culling(self):
        # removes all culled words from the corpus based on the culling file created
        # in the method preprocess_culling
        culled_document_contents = self.document_contents.copy()
        try:
            # get file with culling words
            culling_list_file = open(os.path.join("culling_preprocessing", "culled_words_" + str(self.cull_percentage) +  "_"  +  self.corpus_type + "_" + self.corpus_category +".txt")
,  'r', encoding="utf8")
            # split file along lines
            culling_list = culling_list_file.read().splitlines()

            # iteratate over each word in the culling list and remove it from all documents
            for word in culling_list:
                # needs to be written this way (self.document_contents[i]), otherwise not applicated
                for i in range(len(culled_document_contents)):
                    culled_document_contents[i] = culled_document_contents[i].replace(word, "")
            culling_list_file.close()

        except FileNotFoundError:
            print("Culling not applied, as no file found. Culling will be skipped for this specific file.")
        return culled_document_contents

    def preprocess_culling(self):
        # applies culling, i.e. identifies words that should not be taken into account
        # for stylometry calculations
        # A word should be removed, if it does not occur in min. X percent of all documents

        # calculate amount of docs based on the selected culling percentage
        min_word_amount = (self.cull_percentage*len(self.document_contents))/100
        min_word_amount_rounded = round(min_word_amount)

        #create file for saving words to be removed
        culledWords = open(os.path.join("culling_preprocessing", "culled_words_" + str(self.cull_percentage) +  "_"  +  self.corpus_type + "_" + self.corpus_category +".txt")
, "w+", encoding="utf8")
        # if percentage is 0, just create empty file, as no culling should be applied
        if self.cull_percentage > 0:
            all_words = []
            # iterate over all documents and create a list with all unique words of all documents
            for document in self.document_contents:
                words = nltk.word_tokenize(document)
                unique_words = set(words)
                unique_words_list = list(unique_words)
                for word in unique_words_list:
                    if word not in all_words:
                        all_words.append(word)

            all_words.sort()

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
                        print("Word does not occur in "+ str(doc_counter)+" documents "+  " -> Word:"+word)

                        # if the current word occurs less than in X percent of all documents
                        if len(self.document_contents) - doc_counter < min_word_amount_rounded:
                            print(word +" removed, because not contained in min. " + str(self.cull_percentage) + "% of all documents.")
                            # add word to to-remove list
                            culledWords.write(word+" \n")
                            # don't iterate this word anymore over other documents
                            break

                
            culledWords.close()


    def apply_stylometry(self, culled_docs):
        # Frequencies of the x most common n-grams in the corpus
        # n-grams can be indicated as ranges, e.g. (1, 3) includes ngrams from 1 to 3
        # n-grams can also be indicated as single numbers, e.g. (3, 3) includes only 3-grams
        # max_features = MFWs
        vectorizer = TfidfVectorizer(max_features=self.MFW, analyzer='char', use_idf=False, ngram_range=(self.ngram_range_min, self.ngram_range_max))
        matrix = vectorizer.fit_transform(culled_docs)
     

        # distance measure provided by methods from sklearn:
        # manhattan_distances = burrows delta
        # euclidean_distances = quadratic delta (argamon 2008)
        # beim vergleich der anwälte liefert euclidean metric zb bessere ergebnisse
        if self.delta == "Quadratic":
            distance = euclidean_distances(matrix)
        else:
            distance = manhattan_distances(matrix)

        # Hierarchical Cluster Analysis, i.e. grouping of nearest documents and
        # display in dendrogram
        hierarchies = linkage(distance, self.hcaAlgorithm)
        figure = dendrogram(hierarchies, labels=self.document_titles, orientation="left", leaf_font_size=8, leaf_rotation=0)

    def visualize_results(self):
        plot.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
        ngram = str(self.ngram_range_min) + "-" + str(self.ngram_range_max) + "-gram "
        plot.title(str(self.MFW) + " MFW " + ngram +  str(self.cull_percentage)+"% culling " + self.delta+" Delta " + "\n"+ self.corpus_category + " " + self.corpus_type + " corpus")
        plot.tight_layout()
        plot.savefig("results_stylometry/"+ str(self.MFW) + "MFW_"+ngram+"_"+str(self.cull_percentage)+"cul_"+ self.delta+ "Delta_"+ self.corpus_category + " " + self.corpus_type+".png")
        # redraws each plot, otherwise all previous plots are placed in one plot
        plot.cla()
        plot.clf()
        plot.close()
def main():
    calculateStylometry = Stylometry()

if __name__ == '__main__':
    main()


