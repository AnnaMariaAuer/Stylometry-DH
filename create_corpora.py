import glob
import re
import os
import string
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
STOPWORDS = stopwords.words('german')
print(STOPWORDS)
# from nltk.tokenize import word_tokenize



# Reading in files from a certain path and create one txt-file out of it: all files of one category

def make_txt_to_category(path, name, save_to_folder):

    filename = name + "_all.txt"
    save_path = save_to_folder

    path_to_files = path + "/*.txt"
    all_files = glob.glob(path_to_files)
    print(all_files)

    complete_name = os.path.join(save_path, filename )
    output_file = open(complete_name, 'a+', encoding='UTF-8')
    for file in all_files:
        f = open(file, 'r')
        output_file.write(f.read())
        f.close()
    output_file.close()


# Finds all txt-files of Subcorpus and appends them to one txt-file
def get_all_txt_of_category (path, name):
    path_to_open = path + "/**/*.txt"
    filename = name + "_all.txt"
    all_files = glob.glob(path_to_open, recursive=True)
    print(all_files)

    complete_name = os.path.join(path, filename)
    output_file = open(complete_name, 'a+')
    for file in all_files:
        f = open(file, 'r')
        #sys.stdout.write(f.read())
        output_file.write(f.read())
        f.close()
    output_file.close()


def remove_punctuation_numbers (path, save_to_folder):
    files_to_process = path + "/*.txt"
    files = glob.glob(files_to_process)
    print(files)

    filenames = []

    #removes digits
    translator = str.maketrans('','', string.digits)
    translator2 = str.maketrans('','',string.punctuation)

    counter = 0

    for file in files:

        #gets the names and saves them to list
        filename = os.path.splitext(file)
        filenames.append(re.findall(r'[ \w]*_all', str(filename[0])))

        #removes punctuation, numbers, strip whitespace, to lower
        current_name = str(filenames[counter]).translate(translator2)
        print(current_name)
        complete_name = os.path.join(save_to_folder, current_name + '.txt')

        current_file = open(complete_name, 'w', encoding='UTF-8')
        f = open(file, 'r', encoding='UTF-8')
        content_of_file = f.read()
        no_punctuation = re.sub(r'[^\w\s]','',content_of_file)
        no_digits = no_punctuation.translate(translator).lower()
        no_digits = " ".join(no_digits.split())
        print(no_digits)
        current_file.write(no_digits)

        f.close()
        current_file.close()

        counter += 1


def make_corpus_without_stopwords(path, save_to_directory):
    # todo: ich finde wir sollten alle "Wörter" entfernen, die kleiner gleich 3 Buchstaben haben, zumindest alle einzelnen Buchstaben!
    files_to_process = path + "/*.txt"
    files = glob.glob(files_to_process)
    print(files)

    filenames = []
    translator2 = str.maketrans('', '', string.punctuation)

    counter = 0

    for file in files:

        #gets the names and saves them to list
        filename = os.path.splitext(file)
        filenames.append(re.findall(r'[ \w]*all', str(filename[0])))


        #removes punctuation, numbers, strip whitespace, to lower
        current_name = str(filenames[counter]).translate(translator2)
        print(current_name)
        complete_name = os.path.join(save_to_directory, current_name + '.txt')

        current_file = open(complete_name, 'a+', encoding='UTF-8')
        f = open(file, 'r', encoding='UTF-8')
        words_of_file = f.read().split()
        no_stopwords = []
        for word in words_of_file:
            print(word)
            if word not in STOPWORDS:
                no_stopwords.append(word)

        text_for_output = ' '.join(no_stopwords)
        current_file.write(text_for_output)

        f.close()
        current_file.close()

        counter += 1
    print(filenames)



if __name__ == "__main__":
    # make_txt_to_category("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter/Social security for migrant workers", "social_security_for_migrant_workers", "/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter")
    # get_all_txt_of_category("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter", "subject_matter")
    # remove_punctuation_numbers(r"C:\Users\ArbeitsPC\PycharmProjects\Stylometry-DH\Arbeitskorpus_advocate_general_structured", r"C:\Users\ArbeitsPC\PycharmProjects\Stylometry-DH\corpus-without-punct-numb\advocats")
    make_corpus_without_stopwords(r"C:\Users\ArbeitsPC\PycharmProjects\Stylometry-DH\corpus-without-punct-numb\subject-matter", r"C:\Users\ArbeitsPC\PycharmProjects\Stylometry-DH\corpus-without-stopword\subject-matter")
