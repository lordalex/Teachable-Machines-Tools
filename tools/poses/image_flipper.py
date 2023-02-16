import os
from PIL import Image

# Folder path where the images are stored
folder_path = "/Users/lordalexleon/Code/dataset8/Dash_Buttons-samples2"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        img = Image.open(os.path.join(folder_path, filename))

        # Flip the image horizontally
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Save the flipped image
        flipped_img.save(os.path.join(folder_path, "flipped_" + filename))
