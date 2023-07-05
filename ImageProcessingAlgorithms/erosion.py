import cv2
import numpy as np
from skimage import io

from FileSelector import open_file_dialog as ofd

def erosion():
    print("Opening file dialog.")
    image_to_analyze = cv2.imread(ofd())
    print("Creating kernel of 5x5.")
    ker = np.ones((5, 5), np.uint8)
    print("Applying erosion.")
    new_image = cv2.erode(image_to_analyze, ker, iterations=1)
    print("Showing result.")
    io.imshow(new_image)
    io.show()
