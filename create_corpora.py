import glob
import re
import sys
import os
from pathlib import Path

#Reading in files from a certain path and create one txt-file out of it: all files of one category

def make_txt_to_category(path, name, save_to_folder):

    filename = name + "_all.txt"
    save_path = save_to_folder

    path_to_files = path + "/*.txt"
    all_files = glob.glob(path_to_files)
    print(all_files)

    complete_name = os.path.join(save_path, filename )
    output_file = open(complete_name, 'a+')
    for file in all_files:
        f = open(file, 'r')
        #sys.stdout.write(f.read())
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

    to_directory = os.path.join(save_to_folder)
    filenames = []

    for file in files:
        print("Path of current file: " + "" + path + file)
        filename = os.path.splitext(path + file)
        print(filename)
        #todo: regex not working yet
        filenames.append(re.match(r'[ \w-]+?_all', filename[0]))

    print(filenames)




if __name__ == "__main__":
    # make_txt_to_category("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter/Social security for migrant workers", "social_security_for_migrant_workers", "/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter")
    # get_all_txt_of_category("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter", "subject_matter")
    remove_punctuation_numbers("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_advocate_general_structured", "/Users/Anna/PycharmProjects/Stylometry-DH/corpus-without-punct-numb")

'''print(os.getcwd())

data_folder  = Path("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_advocate_general_structured/Bobek")
file_to_open = data_folder / "*.txt"
f = open(file_to_open)
print(f.read())'''