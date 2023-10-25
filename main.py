import cv2 as cv
import pickle

# Initialize the video capture from 'carPark.mp4'
cap = cv.VideoCapture('data/carPark.mp4')

# Define the width and height of the parking rectangles
width, height = 107, 48

# Load the parking positions from a file
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Function to add text inside a colored rectangle
def putTextRect(img, text, pos, scale=3, thickness=3, colorT=(255, 255, 255), colorR=(255, 0, 255), font=cv.FONT_HERSHEY_PLAIN, offset=10, border=None, colorB=(0, 255, 0)):
    ox, oy = pos
    (w, h), _ = cv.getTextSize(text, font, scale, thickness)

    x1, y1, x2, y2 = ox - offset, oy + offset, ox + w + offset, oy - h - offset

    cv.rectangle(img, (x1, y1), (x2, y2), colorR, cv.FILLED)
    if border is not None:
        cv.rectangle(img, (x1, y1), (x2, y2), colorB, border)
    cv.putText(img, text, (ox, oy), font, scale, colorT, thickness)

    return img, [x1, y2, x2, y1]

# Function to check parking spots
def carparkcheck(img):
    carparkcount = 0
    for pos in posList:
        x, y = pos
        carpark_img = img[y:y+height, x:x+width]
        countwhite = cv.countNonZero(carpark_img)

        if countwhite < 450:
            carparkcount += 1
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)

        cv.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, 4)
        putTextRect(frame, str(countwhite), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=countwhite)

    putTextRect(frame, f'Free: {carparkcount}/{len(posList)}', (100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))

# Main loop for video processing
while True:
    ret, frame = cap.read()
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv.adaptiveThreshold(imgBlur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv.medianBlur(imgThreshold, 5)
    carparkcheck(imgMedian)
    if ret:
        cv.imshow('video', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
cv.destroyAllWindows()