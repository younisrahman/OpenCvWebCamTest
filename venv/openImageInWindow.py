import cv2

img = cv2.imread('butterfly.jpeg')

while True:
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xff == ord('c'):
        break

cv2.destroyAllWindows()