import os
import random
from shutil import move

def random_swap_files(src_folder, dst_folder):
    src_files = os.listdir(src_folder)
    dst_files = os.listdir(dst_folder)
    
    # Check if both folders have files to swap
    if src_files and dst_files:
        # Select a random file from the source folder
        src_file = random.choice(src_files)
        src_file_path = os.path.join(src_folder, src_file)
        
        # Select a random file from the destination folder
        dst_file = random.choice(dst_files)
        dst_file_path = os.path.join(dst_folder, dst_file)
        
        # Swap the files
        move(src_file_path, dst_file_path)
        move(dst_file_path, src_file_path)
        
        print("Files swapped successfully!")
    else:
        print("Both folders should have at least one file to perform the swap.")

# Example usage
src_folder = "./src"
dst_folder = "./dst"
random_swap_files(src_folder, dst_folder)
