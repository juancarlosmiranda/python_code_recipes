"""
Author: Juan Carlos Miranda
Description:
    Script with examples about managing paths and directories.
    https://appdividend.com/2021/03/24/how-to-get-filename-from-path-in-python/
Usage:
    python python_directories_main.py
"""
import os
import os
from os.path import expanduser

if __name__ == '__main__':
    print("Example managing directories")

    # --------------------------------
    # environment information
    user_path = expanduser("~")
    current_folder = os.getcwd()  # 'C:\\Users\\Usuari\\development\\python_code_recipes\\python_advanced_topics'

    # --------------------------------
    # script information, getting data from path
    current_script_path_str = __file__  # with slash /
    script_name = os.path.basename(current_script_path_str)  # get the script's name
    normalised_script_path = os.path.normpath(current_script_path_str)  # conversion to operating system format \ Windows for example.
    local_script_path = os.path.dirname(os.path.abspath(__file__))  # from a complete plath get the dirname

    # --------------------------------
    # managing folders
    absolute_path = os.path.abspath('.')
    absolute_father_path = os.path.abspath('..')  # asking moving from current directory
    father_path = os.pardir
    folder_to_check_path = os.path.join(absolute_path, 'multithreading')
    folder_to_check_not_path = os.path.join(absolute_path, 'NOT_EXISTS')
    folder_to_search = os.path.join(absolute_path, 'multithreading')
    current_dirname = os.path.dirname(os.path.normpath(normalised_script_path))

    print(f"user_path               = {user_path}")
    print(f"current_folder          = {current_folder}")
    print(f"\n")
    print("-- Getting data from script path --")
    print(f"current_script_path_str = {current_script_path_str}")
    print(f"script_name             = {script_name}")
    print(f"normalised_path         = {normalised_script_path}")
    print(f"local_script_path       = {local_script_path}")
    print(f"\n")
    print("-- Working with directories --")
    print(f"absolute_path           = {absolute_path}")
    print(f"absolute_father_path    = {absolute_father_path}")
    print(f"father_path             = {father_path}")
    print(f"folder_to_check_path    = {folder_to_check_path}")
    print(f"folder_to_check_not_path= {folder_to_check_not_path}")
    print(f"current_dirname         = {current_dirname}")
    print(f"\n")


    # ---------------------------------------------------
    path_filename_selected = "/home/user/sound_db/test_data_split/VID-20200319-WA0064.mp4.wav_split_07.wav"
    file_name_selected = os.path.basename(path_filename_selected)
    print("-- Getting the filename from path with os.path.basename() --")
    print(f"path_filename_selected = {path_filename_selected}")
    print(f"file_name_selected     = {file_name_selected}")

    # ---------------------------------------------------
    print("-- Checking directories --")
    # checking for the existence of directories
    if os.path.exists(folder_to_check_path):
        print("Directory exist!!!", folder_to_check_path)
    pass

    if os.path.exists(folder_to_check_not_path):
        print("Directory exist!!!", folder_to_check_not_path)
    else:
        print("Directory doesn't exist!!!", folder_to_check_not_path)
    pass

    print("-- Checking if the path is a file --")
    if os.path.isfile(path_filename_selected):
        print(f"{path_filename_selected} IS A FILE!!")
    else:
        print(f"{path_filename_selected} IT SEEMS IS NOT  A FILE!!")

    # ---------------------------------------------------
    print("-- Iterating over files in directories --")
    extension_file_to_search = ".md"  # filter by extension
    for a_filename in os.listdir(folder_to_search):
        print(f"LISTING - {a_filename}")
        if a_filename.endswith(extension_file_to_search):
            print(f"EXECUTING ACTION WITH with file {a_filename}")

    # ---------------------------------------------------

