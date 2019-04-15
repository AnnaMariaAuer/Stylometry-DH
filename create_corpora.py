import glob
import re
import os
import string
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
STOPWORDS = stopwords.words('german')
from collections import Counter
from pathlib import Path

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
    path_to_open = path + "*.txt"
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
    print(files_to_process)
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
        print("filename: " + " " + str(filename))
        filenames.append(re.findall(r'[ \w]*_[\w]*', str(filename[0])))
        print(filenames)

        #removes punctuation, numbers, strip whitespace, to lower
        current_name = str(filenames[counter][1]).translate(translator2)
        print(current_name)
        complete_name = os.path.join(save_to_folder, current_name + '.txt')

        current_file = open(complete_name, 'a', encoding='UTF-8')
        f = open(file, 'r', encoding='UTF-8')
        content_of_file = f.read()
        no_punctuation = re.sub(r'[^\w\s]','',content_of_file)
        no_digits = no_punctuation.translate(translator).lower()
        no_digits = " ".join(no_digits.split())
        #print(no_digits)
        current_file.write(no_digits)

        f.close()
        current_file.close()

        counter += 1


def make_corpus_without_stopwords(path, save_to_directory):
    files_to_process = path + "/*.txt"
    files = glob.glob(files_to_process)
    print(files)

    filenames = []
    translator2 = str.maketrans('', '', string.punctuation)

    counter = 0

    for file in files:

        #gets the names and saves them to list
        filename = os.path.splitext(file)
        print("filename: " + str(filename))
        filenames.append(re.findall(r'[\w]*$', str(filename[0])))
        print(filenames)


        #removes stopwords
        current_name = str(filenames[counter][0]).translate(translator2)
        print("current name: " + str(current_name))
        complete_name = os.path.join(save_to_directory, current_name + '.txt')
        current_file = open(complete_name, 'a+', encoding='UTF-8')
        f = open(file, 'r', encoding='UTF-8')
        words_of_file = f.read().split()
        no_stopwords = []
        for word in words_of_file:
            #print(word)
            if (word not in STOPWORDS and len(word)>2):
                no_stopwords.append(word)

        text_for_output = ' '.join(no_stopwords)
        current_file.write(text_for_output)

        f.close()
        current_file.close()

        counter += 1
    print(filenames)


def get_top_n_words(path, save_to_directory, n):

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
        words_of_file = re.findall(r'\w+', f.read())
        print(words_of_file)
        word_counts = Counter(words_of_file)
        current_file.write(str(word_counts.most_common(n)))
        f.close()
        current_file.close()
        counter += 1


def add_POS_tagging (path, save_to_directory):
    files_to_process = path + "/*.txt"
    files = glob.glob(files_to_process)
    print(files)


    s = parse('Die Katze liegt auf der Matte.')
    s = split(s)
    print(s.sentences[0])


    filenames = []
    translator2 = str.maketrans('', '', string.punctuation)

    counter = 0

    for file in files:

        #gets the names and saves them to list
        filename = os.path.splitext(file)
        print("filename: " + str(filename))
        filenames.append(re.findall(r'[\w]*$', str(filename[0])))
        print(filenames)

        #do POS-Tagging
        current_name = str(filenames[counter][0]).translate(translator2)
        print("current name: " + str(current_name))
        complete_name = os.path.join(save_to_directory, current_name + '.txt')
        current_file = open(complete_name, 'a+', encoding='UTF-8')
        f = open(file, 'r', encoding='UTF-8')
        words_of_file = parse(f.read(), tagset="STTS")
        words_of_file = split(words_of_file)
        current_file.write(str(words_of_file))

        f.close()
        current_file.close()

        counter += 1


def get_all_txt_files(path):

    return Path(path).glob("*/*/*.txt")

def count_words():

    all_files = []
    number_of_words_storage = []
    average_words = 0

    for name in get_all_txt_files(r"/Users/Anna/PycharmProjects/Stylometry-DH/corpus-unaltered"):
        all_files.append(name)

    for file in all_files:
        f = open(file, 'r', encoding='UTF-8')
        words_of_file = re.findall(r'\w+', f.read())
        number_of_words_storage.append(len(words_of_file))

    print(number_of_words_storage)

    for number in range(len(number_of_words_storage)):
        print(number_of_words_storage[number])
        average_words += number_of_words_storage[number]
        number += 1

    average_words /= len(number_of_words_storage)
    print(average_words)






if __name__ == "__main__":
    make_txt_to_category()
    get_all_txt_of_category()
    remove_punctuation_numbers()
    make_corpus_without_stopwords()
    get_top_n_words()
    add_POS_tagging()
    get_all_txt_files()
    count_words()




