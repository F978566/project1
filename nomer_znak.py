import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

def func():
	img = cv2.imread('images/IMG.jpg')
	img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	filt = cv2.bilateralFilter(img2, 11, 15, 15) # первый параметр это картинка, второй параметр это сколько пикселей будет охвачено, третий параиетр указывает цыетовое пространство, четвёртый параметр координатно пространство
	edges = cv2.Canny(filt, 30, 150)

	cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_TREE находит все контуры и раставляет их в иирайхическом порядке
	cont = imutils.grab_contours(cont)
	cont = sorted(cont, key = cv2.contourArea, reverse=True)

	pos = None
	for c in cont:
		approx = cv2.approxPolyDP(c, 10, True) # мы перебираем список контуров. Чем больше первое число, тем больше фигура должна быть похожа на квадрат. Значение True означает то, что мы ищем только те контуры, чья форма является закрытой. Наприме квадрат или круг или ромб, но линия или полукруг не подходит
		if len(approx) == 4: # 4 так как у прямоугольника четыре стороны
			pos = approx
			break

	print(pos)

	pl.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
	pl.show()

func()