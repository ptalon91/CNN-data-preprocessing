"""
This script has been used for preprocessing remote sensing data, in order to use it with neural networks.
Crops patches of same size in an image and in the corresponding ground truth images.
Original images and ground truth are attributed with the same file names.
"""

from PIL import Image
from pylab import array, imshow, show
import sys, os

# Parameters...
# Paths to data.
path_to_sat_img = "D:/Desktop/mos25.tif"
path_to_gt_img = "D:/Desktop/swiss_annot.tif"

# Define patch size for image cropping.
patch_width = 768
patch_height = 768 

def main():

    # Set an index that will increase after each input image has been processed.
    index = 0
        
    # Open input image
    sat_img = Image.open(path_to_sat_img)
    gt_img = Image.open(path_to_gt_img)

    # Get input image dimensions
    sizeX = sat_img.size[0]
    sizeY = sat_img.size[1]

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
            
            sat_patch = sat_img.crop(coords)
            gt_patch = gt_img.crop(coords)
            
            pixels = gt_patch.load()
            
            bad_pixel = False
            
            # For every pixel:
            for i in range(gt_patch.size[0]): 
                for j in range(gt_patch.size[1]):
                          
                    # If a white or transparent pixel is identified, patch is not saved          
                    if pixels[i,j] == (255, 255, 255, 255) or pixels[i,j] == (0, 0, 0, 0):
                        bad_pixel = True
            
            if bad_pixel == False:
            
                # Save patch to desired path, with unique ID.
                gt_patch.save("D:/Desktop/gt_cropped/"
                #+ "label_"
                + str(row)
                + str(column)
                + ".tif")
                
                sat_patch.save("D:/Desktop/sat_cropped/"
                #+ "sat_"
                + str(row)
                + str(column)
                + ".tif")
                
if __name__ == "__main__":
    main()