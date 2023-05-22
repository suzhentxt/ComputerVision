import numpy as np
from cv2 import cv2

cap = cv2.VideoCapture("1.mp4")

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
#vẽ line
    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 0), 5)
#vẽ hcn
    img = cv2.rectangle(frame, (0, 0), (200, 400), (0, 0, 0), -1)
#vẽ hình tròn
    img = cv2.circle(frame, (500, 500), 70, (125, 24, 78), -1)
#chèn text
    font = cv2.FONT_ITALIC
    img = cv2.putText(frame, "Chinh", (0, height-50), font, 3, 5)
    cv2.imshow("main", frame)

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()