import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)
windowName = 'Frame'
cv2.namedWindow(windowName)

def dwar_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 30,(0,0,255), -1)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y), 40,(0,255,0), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y), 20,(255,0,0), -1)

cv2.setMouseCallback(windowName, dwar_circle)

while True:
    cv2.imshow(windowName, img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()