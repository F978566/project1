import cv2
import dlib


def main():

	img = cv2.imread('triangle1.png')
	#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	cv2.imshow('name', img)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()