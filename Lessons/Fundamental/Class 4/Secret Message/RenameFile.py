from os import listdir, rename, getcwd, chdir
import string

def remane_files():
    dir = "./Class 4/Secret Message/images/prank"
    files = listdir(dir)
    saved_path = getcwd()
    chdir(dir)
    translation_table = str.maketrans("0123456789", "          ")
    for file in files:
        rename(file, file.translate(translation_table))
    chdir(saved_path)
    
remane_files()