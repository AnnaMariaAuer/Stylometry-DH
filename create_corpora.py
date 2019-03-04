import glob
import re
import os
import string


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

    filenames = []

    #removes digits
    translator = str.maketrans('','', string.digits)
    translator2 = str.maketrans('','',string.punctuation)

    counter = 0

    for file in files:

        #gets the names and saves them to list
        filename = os.path.splitext(file)
        filenames.append(re.findall(r'[ \w]*_all', str(filename[0])))

        #removes punctuation and numbers
        current_name = str(filenames[counter]).translate(translator2)
        print(current_name)
        complete_name = os.path.join(save_to_folder, current_name + '.txt')

        current_file = open(complete_name, 'w')
        f = open(file, 'r')
        content_of_file = f.read()
        no_punctuation = re.sub(r'[^\w\s]','',content_of_file)
        no_digits = no_punctuation.translate(translator)
        print(no_digits)
        current_file.write(no_digits)

        f.close()
        current_file.close()

        counter += 1



if __name__ == "__main__":
    # make_txt_to_category("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter/Social security for migrant workers", "social_security_for_migrant_workers", "/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter")
    # get_all_txt_of_category("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter", "subject_matter")
    remove_punctuation_numbers("/Users/Anna/PycharmProjects/Stylometry-DH/Arbeitskorpus_subject_matter", "/Users/Anna/PycharmProjects/Stylometry-DH/corpus-without-punct-numb/subject-matter")

