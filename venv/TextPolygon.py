import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

font = cv2.FONT_HERSHEY_DUPLEX  #select Font Family
cv2.putText(img,text='Younis Rahman',org=(50,50),fontFace=font,fontScale=1,color=(64,200,100),thickness=2) #put Text on image

var = np.array([[100,300],[200,200],[400,300],[200,400]],np.uint8)

pts = var.reshape((-1,1,2))
cv2.polylines(img,np.int32([pts]), isClosed=False,color=(0,255,0), thickness=4)

while True:
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xff == 13:
        break

cv2.destroyAllWindows()