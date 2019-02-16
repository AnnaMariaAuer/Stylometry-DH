from pathlib import Path

#Reading in files from a certain path and create one txt-file out of it

def get_txt(base_directory):
    return Path(base_directory).glob("*/*.txt")

get_txt("Arbeitskorpus_advocate_general_sturctured")