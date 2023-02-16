# Version 3.0

import os

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

rename_files("/Users/lordalexleon/Code/dataset9_feb/approche-right")