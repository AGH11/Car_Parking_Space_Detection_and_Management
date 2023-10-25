import cv2 as cv
import pickle

# Define the width and height of the rectangles
width, height = 107, 48

# Load saved positions or initialize an empty list
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except FileNotFoundError:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv.EVENT_LBUTTONDOWN:
        # Add the clicked position to the list
        posList.append((x, y))
    if events == cv.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                # Remove the clicked position from the list
                posList.pop(i)

    # Save the updated position list to a file
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    # Load the image
    img = cv.imread('data/carParkImg.png')

    # Draw rectangles based on the stored positions
    for pos in posList:
        cv.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    # Display the image and set the mouse callback
    cv.imshow('image', img)
    cv.setMouseCallback('image', mouseClick)

    # Exit the loop when 'q' is pressed
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# Close the OpenCV windows
cv.destroyAllWindows()