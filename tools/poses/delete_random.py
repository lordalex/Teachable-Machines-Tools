import os
import random

def delete_files(folder_path, number_of_files):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if number_of_files > len(files):
        print(f"Number of files to delete is greater than the number of files in the folder")
        return
    for i in range(number_of_files):
        file_to_delete = random.choice(files)
        os.remove(os.path.join(folder_path, file_to_delete))
        files.remove(file_to_delete)

delete_files("/Users/lordalexleon/Code/dataset8/Vas_T_En_left-samples", 34)
