import cv2
import dlib
import imutils

def recog_1():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

    while 1:
        image = cv2.imread('images/img3.jpg')
        image = cv2.flip(image, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        detect = detector(gray, 1)
        for face in detect:
            shape = predictor(image, face)

            for i in range(0, 68):
                x = shape.part(i).x
                y = shape.part(i).y

                cv2.circle(image, (x, y), 2, (0, 255, 0), -5)

        cv2.imshow('name', image)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

def recog_2():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

    face_data = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while 1:
        image = cv2.imread('images/img3.jpg')
        image = cv2.flip(image, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_data.detectMultiScale(gray, 1.1, 19)
        width = faces[0][2]
        height = faces[0][3]
        y = 0
        x = 0
        width1 = faces[0][2]
        height1 = faces[0][3]
        y1 = 0
        x1 = 0
        distance = 50

        marker = find_marker()

        for (x, y, w, h) in faces:
            if w < width1:
                width1 = w
                height1 = h
                y1 = y
                x1 = x
                cv2.rectangle(image, (x1, y1), (width1+x1, height1+y1), (0, 255, 0), 2)
            if w > width:
                width = w
                height = h
                y = y
                x = x
                cv2.rectangle(image, (x, y), (width+x, height+y), (0, 255, 0), 2)
            

        cv2.imshow('name', image)

        if cv2.waitKey(1) & 0xff == ord('q'):
            lenght = (width * distance) / width1
            print(lenght)
            break
    
    cap.release()
    cv2.destroyAllWindows()

def find_marker(image = cv2.imread('images/img3.jpg')):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)
	return cv2.minAreaRect(c)

def main():
    recog_2()


if __name__ == '__main__':
    main()