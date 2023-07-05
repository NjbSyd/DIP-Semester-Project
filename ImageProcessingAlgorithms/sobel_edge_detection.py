from skimage import io
from skimage import filters
from skimage import color
from FileSelector import open_file_dialog as ofd


def sobel_detection(file_path=None):
    if file_path is None:
        print("Opening file dialog.")
        image_to_analyze = io.imread(ofd())

    else:
        image_to_analyze = io.imread(file_path)

    print("Computing luminance of the image.")
    gray_image = color.rgb2gray(image_to_analyze)
    print("Computing Sobel edge detection.")
    edge_detection = filters.sobel(gray_image)
    print("Displaying Sobel edge detection.")
    io.imshow(edge_detection)
    print("Showing Sobel edge detection.")
    io.show()
