from skimage import io
import cv2
import numpy as np
from FileSelector import open_file_dialog as ofd


def simple_dilation(file_path=None):
    if file_path is None:
        print("Opening file dialog.")
        image_to_analyze = cv2.imread(ofd())

    else:
        image_to_analyze = cv2.imread(file_path)

    print("Creating kernel of 10x10.")
    kernel = np.ones((10, 10), np.uint8)
    print("Applying dilation.")
    new_image = cv2.dilate(image_to_analyze, kernel, iterations=1)
    print("Showing result.")
    io.imshow(new_image)
    io.show()
