from skimage import io
from skimage import feature
from skimage import color
from FileSelector import open_file_dialog as ofd


def canny_detection(file_path=None):
    if file_path is None:
        print("Opening file dialog.")
        image_to_analyze = io.imread(ofd())

    else:
        image_to_analyze = io.imread(file_path)

    print("Computing luminance of the image.")
    gray_image = color.rgb2gray(image_to_analyze)
    print("Computing Canny edge detection.")
    edge_detection = feature.canny(gray_image)
    print("Displaying Canny edge detection.")
    io.imshow(edge_detection)
    print("Showing Canny edge detection.")
    io.show()
