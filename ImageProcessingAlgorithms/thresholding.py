import cv2
from skimage import io
from FileSelector import open_file_dialog as ofd


def apply_threshold():
    print("Opening file dialog")
    image_to_analyze = cv2.imread(ofd())
    print("Converting to gray scale.")
    gray_image = cv2.cvtColor(image_to_analyze, cv2.COLOR_BGR2GRAY)
    print("Applying thresholding.")
    new_img = cv2.threshold(gray_image,100, 255, cv2.THRESH_BINARY)
    print("Showing result.")
    io.imshow(new_img[1])
    io.show()
