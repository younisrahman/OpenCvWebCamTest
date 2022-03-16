import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

cv2.rectangle(img,pt1=(380,10),pt2=(500,150),color=(0,255,0),thickness=4) #create a rectangle

cv2.rectangle(img,pt1=(200,200),pt2=(300,300),color=(255,0,0),thickness=4) #create a square

cv2.circle(img,center=(100,100), radius=50, color=(0,0,255),thickness=4) #create a circle

cv2.line(img,pt1=(0,365),pt2=(512,365),color=(180,50,60),thickness=4) #create a line

while True:
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xff == 13:
        break

cv2.destroyAllWindows()