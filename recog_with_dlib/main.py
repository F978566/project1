import cv2
import dlib


def main():
    detector = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

    cap = cv2.VideoCapture(0)

    while 1:
        res, img = cap.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector(img_gray, 1)
        for face in faces:
            landmarks = predict(img, face)

            top_nose = (landmarks.part(29).x, landmarks.part(29).y)
            left_nose = (landmarks.part(31).x, landmarks.part(31).y)
            right_nose = (landmarks.part(35).x, landmarks.part(35).y)

            cv2.circle(img, top_nose, 1, (0 ,255, 0), 2)
            cv2.circle(img, left_nose, 1, (0, 255, 0), 2)
            cv2.circle(img, right_nose, 1, (0, 255, 0), 2)

            #for lan in landmarks.parts():
            #    lan_pos = (lan.x, lan.y)
            #    cv2.circle(img, lan_pos, 2, (0, 255, 0), 2)

            cv2.imshow('name', img)

        cv2.imshow('name', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()