import cv2 as cv
import numpy as np
import os

# Globals
FOLDER_TO_READ = './Sample Data'

def main():
    raw_imgs = get_images_in_dir(FOLDER_TO_READ)

    # Placeholder because I'm bored and want to print the shapes
    for i in raw_imgs:
        print(i.shape)
    
    print("Finished with whatever we were supposed to be doing.")

def get_images_in_dir(dir):
    '''
    Traverses files in dir specified, getting the images and returning them
    as a list of opencv objects
    '''
    # Get all image files in the folder specified
    print('Searching directory {} for images...'.format(dir))
    img_files = []
    for subdir, dirs, files in os.walk(dir):
        for file_name in files:
            img_files.append(file_name)
            print("Found file: {}".format(file_name))
    
    if (len(img_files) == 0):
        print("No images found, or directory doesn't exist!")

    # For each file, determine if it's an image. If so, open it as an opencv
    # object
    imgs = []
    for f in img_files:
        path_to_f = '{}/{}'.format(dir, f)
        imgs.append(cv.imread(path_to_f, 0)) # Read with openCV in grayscale

    return imgs

if __name__ == '__main__':
    main()