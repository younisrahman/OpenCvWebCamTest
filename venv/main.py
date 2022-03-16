import cv2


cap = cv2.VideoCapture(0)
print('Openning Camera ....')
while True:
    ref,frame = cap.read()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) ==13:
        break

cap.release()
cv2.destroyAllWindows()
print("finished..")