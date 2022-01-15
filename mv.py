import cv2
import mediapipe as mp
from playsound import playsound


def main():
    handsMp = mp.solutions.hands
    hands = handsMp.Hands(max_num_hands=4)
    draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while 1:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = hands.process(img_rgb)
        color = (0, 100, 12)
        xr = 70
        yr = 70
        wr = 200
        hr = 200
        color1 = (40, 100, 12)
        xr1 = 10
        yr1 = 10
        wr1 = 30
        hr1 = 30


        if result.multi_hand_landmarks:
            for landmarks in result.multi_hand_landmarks:
                for id, landm in enumerate(landmarks.landmark):
                    w, h, c = img.shape
                    cx = int(landm.x*w)
                    cy = int(landm.y*h)
                    if id == 8:
                        if cx > xr and cx < wr and cy > yr and cy < hr:
                            color = (200, 100, 50)
                            xr, yr = cx, cy
                            #cv2.rectangle(img, (xr, yr), (wr, hr), color, cv2.FILLED)
                            #playsound('C:/Users/I/Downloads/RU.mp3')
                        if cx < xr1 and cy < yr1:
                            color1 = (200, 100, 50)
                            cv2.rectangle(img, (xr1, yr1), (wr1, hr1), color, cv2.FILLED)
                            cap.release()
                            cv2.destroyAllWindows()

                draw.draw_landmarks(img, landmarks, handsMp.HAND_CONNECTIONS)

        cv2.rectangle(img, (xr1, yr1), (wr1, hr1), color1, cv2.FILLED)
        cv2.rectangle(img, (xr, yr), (wr, hr), color, cv2.FILLED)


        cv2.imshow('name', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()