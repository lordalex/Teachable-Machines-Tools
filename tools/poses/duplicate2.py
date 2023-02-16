import os
import random
import shutil

def duplicate_files(folder_path, desired_number_of_files):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")]
    current_number_of_files = len(files)
    while current_number_of_files < desired_number_of_files:
        file_to_duplicate = random.choice(files)
        shutil.copy2(os.path.join(folder_path, file_to_duplicate), os.path.join(folder_path, "_copy" + file_to_duplicate))
        current_number_of_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")])

duplicate_files("/Users/lordalexleon/Code/dataset9_feb/approche-right", 700)

