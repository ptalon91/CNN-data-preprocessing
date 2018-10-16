"""
For a set of images that have associated ground truth images in a separate folder.
! Original image and associated ground truth must have the same name !
This script moves a chosen percentage of images randomly selected to another folder.
Corresponding ground truth images are also moved to a particular folder.
This script was used to separate a dataset into training, validation and testing subsets.
"""

import os, random
import shutil

# Get folders containing images.
path_to_img = "D:/Desktop/sat_cropped/"
path_to_gt_img = "D:/Desktop/gt_cropped/"

def main():
    # Get all files name, for loop.
    input_filenames = [f for f in os.listdir(path_to_img) if f.endswith('.tif')]

    # Set percentage of images to be moved.
    percent_of_img = 0.5

    # Random selection of percentage of images.
    random_img_filenames = random.sample(input_filenames, int(len(input_filenames) * percent_of_img))

    # Move images and corresponding ground truth to determined folders.
    for random_img_filename in random_img_filenames:
        full_img_name = os.path.join(path_to_img, random_img_filename)
        if (os.path.isfile(full_img_name)):
            shutil.move(full_img_name, "D:/Desktop/test/")
        
        full_gt_img_name = os.path.join(path_to_gt_img, random_img_filename)
        if (os.path.isfile(full_gt_img_name)):
            shutil.move(full_gt_img_name, "D:/Desktop/test_labels/")
            
if __name__ == "__main__":
    main()