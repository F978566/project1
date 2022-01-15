import cv2
import numpy as np # библиотека для создания матрицы

photo = np.zeros((300, 300, 3), dtype='uint8') # матрица, которая состоит из 300 элементов и в каждом этом элементе 300 элементов, она трёх слойная

#photo[90:200, 200:280] = 200, 32, 100 # окрашиваем изображение в синий

cv2.rectangle(photo, (0, 0), (100, 100), (255, 0, 0), cv2.FILLED)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (0, 255, 0), 3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (100, 100, 100), 3)

cv2.imshow('name', photo)
cv2.waitKey(0)