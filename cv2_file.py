import cv2


def capter():
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') # без это херни ничего не заработает, хрень для поиска лиц на картинке

	image = cv2.VideoCapture(0) # указываем свою вебку

	while 1:
		res, img = image.read() # считывае изображение с камеры, в res попадает результат True or False

		#img = cv2.imread('IMG.jpg') # загружаем фотку
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # делаем фотку серой

		face = face_cascade.detectMultiScale(img, 1.1, 19) # указывае с какой картинки распознаём лица
		for (x, y, w, h) in face:
			cv2.rectangle(img, (x, y), (x + w, y + h), (100, 200, 99), 2) # указывае картинку на которой будет рамка, ширину, высоту, цвет, толщину

		cv2.imshow('name', img) # выводим всё это дело на экран

		if cv2.waitKey(1) & 0xff == ord('e'): # задержка
			break

	image.release() # чтоб прекратить обращение к вебке
	cv2.destroyAllWindows() # уничтожение объектов


if __name__ == '__main__':
	capter()