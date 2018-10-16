"""
This script has been used for preprocessing remote sensing data, in order to use it with neural networks.
Crops patches of same size in a set of images and in the corresponding ground truth images.
Original images and ground truth are attributed with the same file names.
"""

from PIL import Image
from pylab import array, imshow, show
import sys, os

# Parameters...
# Paths to data.
path_to_img = "D:/Desktop/Vaihingen_original/gt/"

# Define patch size for image cropping.
patch_width = 768
patch_height = 768 

# Read all data files names for loop.
input_filenames = [f for f in os.listdir(path_to_img) if f.endswith('.tif')]

def main():

    # Set an index that will increase after each input image has been processed.
    index = 0
    
    print(input_filenames)
    
    # Loop, for each input image, divide it into patches, and save them on disk.
    for input_filename in input_filenames:

        # Open input image
        img = Image.open(path_to_img+input_filename)

        # Get input image dimensions
        sizeX = img.size[0]
        sizeY = img.size[1]

        # Compute total number of rows and columns that the image will be divided into.
        num_of_columns = sizeX/patch_width
        num_of_rows = sizeY/patch_height
        
        # Loop, goes through the image and crop the patches.
        for row in range(int(num_of_rows)):
            for column in range(int(num_of_columns)):
                coords = (
                    column * patch_width,
                    row * patch_height,
                    (column + 1) * patch_width,
                    (row + 1) * patch_height
                )
                
                patch = img.crop(coords)
                            
                # Save patch to desired path, with unique ID.
                patch.save("D:/Desktop/gt_cropped/"
                + input_filename + "_"
                #+ str(index)
                + str(row)
                + str(column)
                #+ "_L"
                + ".tif" )
                
        # Increases for each input image.   
        index += 1
            
if __name__ == "__main__":
    main()