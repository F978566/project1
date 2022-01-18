import cv2
import dlib

def main():
    our_word = 'hello'

    cam = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

    while 1:
        _, img = cam.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        detect = detector(gray, 1)
        for face in detect:
            shape = predictor(img, face)
            x = shape.part(29).x
            y = shape.part(29).y

            cv2.putText(img, our_word, (x, y), cv2.FONT_ITALIC, 0.6, (255, 0, 0), 2)

        cv2.imshow('name', img)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()
    cam.release()


if __name__ == '__main__':
    main()