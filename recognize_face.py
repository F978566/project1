import dlib
import cv2

def eye_recog():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

    while 1:
        img = cv2.imread('images/img3.jpg')
        img = cv2.flip(img, 1)
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        det = detector(img_g, 1)
        for face in det:
            shape = predictor(img, face)

            for i in range(0, 68):
                x = shape.part(i).x
                y = shape.part(i).y
                #cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
            
            eye = (shape.part(37).x, shape.part(37).y)
            eye1 = (shape.part(40).x, shape.part(40).y)
            eye_0 = (shape.part(43).x, shape.part(43).y)
            eye1_0 = (shape.part(46).x, shape.part(46).y)
        #    faces_0 = (shape.part(18).x, shape.part(18).y)
        #    faces_1 = (shape.part(11).x, shape.part(11).y)
            cv2.rectangle(img, eye, eye1, (255, 0, 0), 2)
            cv2.rectangle(img, eye_0, eye1_0, (0, 255, 0), 2)
        #    cv2.rectangle(img, faces_0, faces_1, (0, 255, 0), 2)
        
        cv2.imshow('name', img)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    
    
    cap.release()
    cv2.destroyAllWindows()

def recog_face():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

    while 1:
        img = cv2.imread('images/img3.jpg')
        img = cv2.flip(img, 1)
        img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_g, 1.1, 19)
        max_width = faces[0][2]
        max_height = faces[0][3]
        max_x = 0
        max_y = 0
        max_width1 = faces[0][2]
        max_height1 = faces[0][3]
        max_x1 = 0
        max_y1 = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = img_g[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            if w < max_width:
                max_width = w
                max_height = h
                max_y = y
                max_x = x
                cv2.rectangle(img, (max_x, max_y), (max_x+max_width, max_y+max_height), (0, 255, 0), 2)
            if w > max_width:
                max_width1 = w
                max_height1 = h
                max_y1 = y
                max_x1 = x
                cv2.rectangle(img, (max_x1, max_y1), (max_x1+max_width1, max_y1+max_height1), (0, 0, 255), 2)


        det = detector(img_g, 1)
        for face in det:
            shape = predictor(img, face)

            for i in range(0, 68):
                x = shape.part(i).x
                y = shape.part(i).y
                #cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
            
            eye = (shape.part(37).x, shape.part(37).y)
            eye1 = (shape.part(40).x, shape.part(40).y)
            eye_0 = (shape.part(43).x, shape.part(43).y)
            eye1_0 = (shape.part(46).x, shape.part(46).y)
        #    faces_0 = (shape.part(18).x, shape.part(18).y)
        #    faces_1 = (shape.part(11).x, shape.part(11).y)
            cv2.rectangle(img, eye, eye1, (0, 255, 0), 2)
            cv2.rectangle(img, eye_0, eye1_0, (0, 255, 0), 2)
        #    cv2.rectangle(img, faces_0, faces_1, (0, 255, 0), 2)

        
        cv2.imshow('name', img)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


def main():
    recog_face()
    #eye_recog()

if __name__ == '__main__':
    main()