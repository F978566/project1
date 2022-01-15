import numpy as np
import cv2
#https://www.pyimagesearch.com/2015/01/19/find-distance-camera-objectmarker-using-python-opencv/

#https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
face_cascade = cv2.CascadeClassifier('C:/Users/User/PycharmProjects/Akimov/Lesson01/face_haar1')
cap = cv2.imread("mob.jpg")
gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(cap, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = cap[y:y + h, x:x + w]

cv2.imshow('img', cap)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
