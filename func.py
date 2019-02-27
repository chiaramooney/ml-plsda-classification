import numpy as np

# def get_images(image, width=40, height=40):
#     _nrows, _ncols= image.shape
#     _size = image.size
#     _strides = image.strides

#     nrows, _m = divmod(_nrows, height)
#     ncols, _n = divmod(_ncols, width)
#     if _m != 0 or _n != 0:
#         return None

#     return np.lib.stride_tricks.as_strided(
#         np.ravel(image),
#         shape=(nrows, ncols, height, width),
#         strides=(height * _strides[0], width * _strides[1], *_strides),
#         writeable=False
#     )
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

def flatten_data(tiles):
    # flatten divided each sub-image into a 1D array
    result = []
    for x in tiles:
        x = np.array(x)
        result.append(x.flatten())
    result = np.array(result)
    return result
"""
[[1,2,3,4]
 [11,12,13,14]
 [21,22,23,24]
 [31,32,33,34]]

arr = [[1,2,3,4],[11,12,13,14],[21,22,23,24],[31,32,33,34]]
arr = np.array(arr)

print(get_data(arr,2,2))

"""
#rotate an image
#rotate_face = ndimage.rotate(face, 90)

#get size of image
#lx, ly = face.shape