import cv2
import numpy as np
import dlib



def main():
	images = cv2.imread('images/image.png')

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

	image = cv2.VideoCapture(0)

	while 1:
		res, img = image.read()
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img2 = cv2.imread('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/pig_nose.png')
		img2 = cv2.resize(img2, (50, 50))

		faces = detector(img_gray, 1)
		for face in faces:
			landmarks = predictor(img, face)

			left_eys = (landmarks.part(37).x, landmarks.part(37).y)
			left_eys1 = (landmarks.part(40).x, landmarks.part(40).y)
			right_eys = (landmarks.part(43).x, landmarks.part(43).y)
			right_eys1 = (landmarks.part(46).x, landmarks.part(46).y)

			cv2.rectangle(img, left_eys, left_eys1, (0, 255, 0), 2)
			cv2.rectangle(img, right_eys, right_eys1, (0, 2255, 0), 2)


		cv2.imshow('name', img)

		if cv2.waitKey(1) & 0xff == ord('q'):
			break


	image.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()