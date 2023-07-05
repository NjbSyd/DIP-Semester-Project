# Digital Image Processing Project
This project is developed for the Digital Image Processing subject as part of the BSE (Bachelor of Software Engineering) program. The project implements various image processing algorithms using Python and several libraries, including OpenCV, scikit-image, and Tkinter.

## Project Structure
The project consists of several Python files that implement different image processing algorithms and a file selector module. Here's an overview of the project structure:

- **main.py**: This is the main entry point of the program. It provides a command-line interface for selecting and applying different image processing algorithms.
- **ImageProcessingAlgorithms** (folder):
  - **canny_edge_detection.py**: Implements the Canny edge detection algorithm using the skimage library.
  - **erosion.py**: Implements the erosion algorithm using OpenCV.
  - **thresholding.py**: Implements the thresholding algorithm using OpenCV and scikit-image.
  - **sobel_edge_detection.py**: Implements the Sobel edge detection algorithm using the skimage library.
  - **simple_dilation.py**: Implements the simple dilation algorithm using OpenCV.
  - **FileSelector.py**: Provides a file dialog module using the Tkinter library for selecting image files.
## Usage
To use the program, follow these steps:

- Run the `main.py` script.
- Select an option from the menu by entering the corresponding number.
- Depending on the selected option, the associated image processing algorithm will be applied to the selected image file.
- The processed image will be displayed.

The available options are:

- Canny edge detection: Applies the Canny edge detection algorithm to the selected image.
- Sobel edge detection: Applies the Sobel edge detection algorithm to the selected image.
- Simple dilation: Applies the simple dilation algorithm to the selected image.
- Erosion: Applies the erosion algorithm to the selected image.
- Thresholding: Applies the thresholding algorithm to the selected image.

## Dependencies
The project relies on the following libraries:
- [OpenCV](https://docs.opencv.org/4.8.0/d6/d00/tutorial_py_root.html): Library for computer vision and image processing.
- [scikit-image](https://scikit-image.org/docs/stable/): Library for image processing and analysis.
- [Tkinter](https://docs.python.org/3/library/tk.html): Library for creating GUI applications.
## Installation
To run this project, you need to install the required libraries. Here are the commands to install the necessary dependencies:

**OpenCV**
```
pip install opencv-python
```
**scikit-image**
```
pip install scikit-image
```
**Tkinter** (usually comes pre-installed with Python):
For Debian-based Linux distributions:
```
sudo apt-get install python3-tk
```
For Red Hat-based Linux distributions:
```
sudo dnf install python3-tkinter
```
For macOS:
```
brew install python-tk
```
For Windows:
> Tkinter is typically included with the Python installation

_Make sure you have an active internet connection while executing these commands._ 
After installing the dependencies, you can run the main.py script to use the image processing algorithms.

> Please note that the project assumes Python 3.x is installed on your system. If you're using a different Python version, adjust the commands accordingly.
If you encounter any issues during the installation process, refer to the documentation of the respective libraries or consult the official documentation of your operating system.
Once all the dependencies are installed successfully, you can proceed to use the project as described in the previous section.

Happy image processing!✌
