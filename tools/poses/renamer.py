import os

def rename_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for i, filename in enumerate(sorted(files)):
        new_filename = f"{str(i).zfill(3)}.{filename.split('.')[-1]}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

rename_files("/Users/lordalexleon/Code/dataset9_feb/approche-left")