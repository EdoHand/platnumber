import cv2
import numpy as np

width = 640
heigh = 480
minArea = 400
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(5, 100)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
platCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plat_number.xml')
print(platCascade)
color = (0, 255, 0)
count = 0

while True:
    success, frame = cap.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    numberPlates = platCascade.detectMultiScale(imgGray, 1.3, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(frame, 'PLAT NOMOR', (x, y - 5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            imgRoi = frame[y:y + h, x:x + w]
            cv2.imshow('result', imgRoi)
            cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('Resources/Scan/NoPlate_' + str(count) + '.jpg', imgRoi)
        cv2.rectangle(frame, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, "Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow('Result', frame)
        cv2.waitKey(500)
        count += 1
        break
