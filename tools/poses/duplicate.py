import os
import random
import shutil

def duplicate_files(folder_path, number_of_files):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if number_of_files > len(files):
        print(f"Number of files to duplicate is greater than the number of files in the folder")
        return
    for i in range(number_of_files):
        file_to_duplicate = random.choice(files)
        shutil.copy2(os.path.join(folder_path, file_to_duplicate), os.path.join(folder_path, "_copy" + file_to_duplicate))

duplicate_files("/Users/lordalexleon/Code/dataset9_feb/approche-right", 67)

