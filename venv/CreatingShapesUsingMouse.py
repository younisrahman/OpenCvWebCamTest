import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)
windowName = 'Frame'
cv2.namedWindow(windowName)

drawing = False
x1, y1 = -1, -1

def dwar_circle(event, x, y, flags, param):
    global x1, y1, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1,y1 = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(x1,y1),(x,y),(0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (x1, y1), (x, y), (0, 255, 0), -1)

cv2.setMouseCallback(windowName, dwar_circle)

while True:
    cv2.imshow(windowName, img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()