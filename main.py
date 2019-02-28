import cv2 as cv
import numpy as np
import os
import time
import errno

# Globals
FOLDER_TO_READ = './Sample Data'
START_TIME = time.strftime("%Y%m%d-%H%M%")
OUTPUT_PATH = "./output/output-{}/".format(START_TIME)

def main():
    # Create output environment
    create_output_environment(START_TIME)

    raw_imgs, filenames = get_images_in_dir(FOLDER_TO_READ)

    # Placeholder because I'm bored and want to print the shapes
    for i in range(len(raw_imgs)):
        print("Original shape: {}".format(raw_imgs[i].shape))
        subdivisions_of_img = get_subdivisions(raw_imgs[i], 512, 512)
        print("Size of subdivisions of img array:"
              "{}".format(subdivisions_of_img.size))

        # Save the subdivisions
        for j in range(len(subdivisions_of_img)):
            img_name = "{}_{}".format(j, filenames[i])
            save_image(subdivisions_of_img[j], img_name, OUTPUT_PATH)

        print("Flattening subdivisions...")
        res = np.array(flatten_imgs(subdivisions_of_img))
        print("Shape of result: {}".format(res.shape))
        print('\n')

    print("Finished with whatever we were supposed to be doing.")

def get_subdivisions(arr, nrows=40, ncols=40):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    lx, ly = arr.shape
    return (arr.reshape(lx//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

def flatten_imgs(tiles):
    # flatten divided each sub-image into a 1D array
    result = []
    for x in tiles:
        x = np.array(x)
        result.append(x.flatten())
    result = np.array(result)
    return result

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

    return (imgs, img_files)

def save_image(image_to_save, file_name, output_path):
	print ("Writing {} to {}".format(file_name, output_path))
	cv.imwrite((output_path + file_name), image_to_save)
	print ("Done\n")

def create_output_environment(start_time):
	try:
		os.mkdir('./output/')
	except OSError as e:
		if e.errno == errno.EEXIST:
			print("OutputHandler: output folder already created. Doing "
                  "nothing...")
		else:
			raise	# raise exception if it is not the not exist error
	try:
		os.mkdir('./output/output-{}/'.format(start_time))
	except OSError as e:
		print("Something weird is happening. Find me...")

# must run on img in its 2D state. returns array of all four rotations for a given image. 
def create_img_rots(img):
    res = []
    res.append(img)
    res.append(np.rot90(img))
    res.append(np.rot90(res[1]))
    res.append(np.rot90(res[2]))
    res = np.array(res)
    return res

if __name__ == '__main__':
    main()
