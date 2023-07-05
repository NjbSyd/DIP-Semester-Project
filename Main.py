from ImageProcessingAlgorithms.canny_edge_detection import canny_detection
from ImageProcessingAlgorithms.erosion import erosion
from ImageProcessingAlgorithms.thresholding import apply_threshold
from ImageProcessingAlgorithms.sobel_edge_detection import sobel_detection
from ImageProcessingAlgorithms.simple_dilation import simple_dilation

while True:
    print("Select an option:")
    print("1. Canny edge detection")
    print("2. Sobel edge detection")
    print("3. Simple dilation")
    print("4. Erosion")
    print("5. Thresholding")
    print("*** Press enter or input anything to exit. ***")

    option = input("Option: ")
    if option == "1":
        canny_detection()
    elif option == "2":
        sobel_detection()
    elif option == "3":
        simple_dilation()
    elif option == "4":
        erosion()
    elif option == "5":
        apply_threshold()
    else:
        print("Exiting.")
        exit(0)
