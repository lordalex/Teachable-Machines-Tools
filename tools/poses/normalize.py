# Version 3.0

import os
import random
import shutil

def rename_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and "." in f]
    files.sort()
    count = 0
    padding = len(str(len(files) - 1))
    results_path = os.path.join(path, "results")
    if not os.path.exists(results_path):
        os.makedirs(results_path)
    for filename in files:
        split_filename = os.path.splitext(filename)
        new_filename = str(count).zfill(padding) + split_filename[1]
        os.rename(os.path.join(path, filename), os.path.join(results_path, new_filename))
        count += 1



def duplicate_files(folder_path, desired_number_of_files):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")]
    current_number_of_files = len(files)
    while current_number_of_files < desired_number_of_files:
        file_to_duplicate = random.choice(files)
        shutil.copy2(os.path.join(folder_path, file_to_duplicate), os.path.join(folder_path, "_copy" + file_to_duplicate))
        current_number_of_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")])


duplicate_files("/Users/lordalexleon/Code/dataset14_feb/hello_right_hand", 700)
rename_files("/Users/lordalexleon/Code/dataset14_feb/hello_right_hand")