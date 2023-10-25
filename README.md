## Car Parking Space Detection and Management

This Python project uses the OpenCV library to detect and manage parking spaces in a video stream. It consists of two main scripts:

### 1. main.py

- **Function**: This script processes a video feed of a parking area, identifies occupied and vacant parking spaces, and displays real-time statistics.
- **Usage**: Run this script to monitor parking spaces in a video stream. Press 'q' to exit.
- **Dependencies**: OpenCV.
- **Configuration**: Make sure to have a video file named 'carPark.mp4' and parking space positions stored in 'CarParkPos' (you can add them using the second script).
- **How It Works**: The script calculates the number of white pixels in each parking space. If the count is below 450, it marks the space as vacant, otherwise, it marks it as occupied.

### 2. ParkingSpacePicker.py

- **Function**: This script allows you to manually define parking space positions by clicking on an image.
- **Usage**: Run this script to open an image ('carParkImg.png') and define parking space positions by left-clicking. Right-click to remove a position. Press 'q' to exit.
- **Dependencies**: OpenCV.
- **Configuration**: Make sure to have an image named 'carParkImg.png'.
- **How It Works**: It lets you interactively mark parking space positions and saves them in 'CarParkPos' for use with the main script.

### Note

- You can adjust the criteria for marking a space as vacant or occupied by modifying the threshold (450 in the provided code).
- Ensure you have the necessary dependencies installed, especially OpenCV.

This project provides a simple way to monitor and manage parking spaces in a given area.

Enjoy using it! If you have any questions or need further assistance, feel free to ask.
