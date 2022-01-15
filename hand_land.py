import cv2
import mediapipe as mp
import dlib
import time


def hand_func():
    cap = cv2.VideoCapture(0)

    pTime = 0
    fps = 0
    cTime = 0

    handsMp = mp.solutions.hands
    hands = handsMp.Hands(max_num_hands=4)
    drawing = mp.solutions.drawing_utils

    while 1:
        res, img = cap.read()
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        r = hands.process(img_rgb)

        xr1 = 70
        xr2 = 70
        yr1 = 150
        yr2 = 150
        colorRect = (0, 0, 0)
        

        if r.multi_hand_landmarks:
            for landmarks in r.multi_hand_landmarks:
                for id, landm in enumerate(landmarks.landmark):
                    h, w, c = img.shape
                    cx = int(landm.x*w)
                    cy = int(landm.y*h)
                    if id == 8:
                        if xr1-yr1//2 < cx and xr1+yr1//2 > cx and xr2-yr2//2 < cy and cy < xr2+yr2//2:
                            colorRect = (255, 255, 255)
                            xr1, xr2 = cx, cy

                drawing.draw_landmarks(img, landmarks, handsMp.HAND_CONNECTIONS)

        rec = cv2.rectangle(img, (xr1-yr1//2, xr2-yr2//2), (xr1+yr1//2, xr2+yr2//2), colorRect, cv2.FILLED)
        #rec_off = cv2.rectangle(img, (xr3-yr3//2, xr4-yr4//2), (xr3+yr3//2, xr4+yr4//2), colorRect1, cv2.FILLED)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        

        cv2.imshow('name', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def func_face():
    predictor = dlib.shape_predictor('C:/Users/I/Documents/lesson_python/open_cv_lesson/effect_1/shape.dat')
    detector = dlib.get_frontal_face_detector()

    handsMp = mp.solutions.hands
    hands = handsMp.Hands(max_num_hands=4)
    drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while 1:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        r = hands.process(img_rgb)

        if r.multi_hand_landmarks:
            for landmarks in r.multi_hand_landmarks:
                drawing.draw_landmarks(img, landmarks, handsMp.HAND_CONNECTIONS)

        f = detector(img)
        for face in f:
            landmarks = predictor(img_gray, face)

            for lan in range(0, 68):
                x = landmarks.part(lan).x
                y = landmarks.part(lan).y
                cv2.circle(img, (x, y), 1, (255, 255, 255), 1)
            
            
            cv2.imshow('name', img)

        
        if cv2.waitKey(1) & 0xff == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()


def main():
    #func_face()
    hand_func()


if __name__ == '__main__':
    main()
