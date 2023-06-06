Motion Detection

This is a simple Python script that uses OpenCV to detect motion in a video stream from a camera. It compares consecutive frames and applies motion detection algorithms to identify moving objects in real-time.

Requirements

Python 3.x
OpenCV (cv2)
Installation

Clone the repository or download the script file.
Install the required dependencies using the following command:
Copy code
pip install opencv-python
Usage

Make sure you have a webcam connected to your system.
Run the script using the following command:
Copy code
python motion_detection.py
The script will open a window displaying the camera feed with motion detection.
Moving objects will be highlighted with bounding rectangles.
Press the 'q' key to stop the script and exit.
Customization

You can modify the following parameters in the script to adjust the motion detection behavior:

cap = cv2.VideoCapture(0): Change the index to specify a different camera source (e.g., 1 for a secondary camera).
cv2.absdiff(gray1, gray2): Adjust the threshold value (30) to control the sensitivity of motion detection.
cv2.contourArea(contour) < 500: Modify the area threshold to filter out smaller contours.
Feel free to experiment and customize the code according to your needs.

License

This project is licensed under Apache Sofwtare License.

Acknowledgements

This script is based on the OpenCV library, which provides the necessary computer vision algorithms for motion detection.

Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

Author 

Your Name Rishi Barua

References

OpenCV documentation: https://docs.opencv.org/
OpenCV-Python Tutorials: https://opencv-python-tutroals.readthedocs.io/
Disclaimer

This script is provided as-is without any warranty. Use it at your own risk.

Please update the README file with appropriate information such as your name, GitHub profile, and any additional references or acknowledgments you want to include.
