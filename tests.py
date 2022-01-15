import cv2
import mediapipe as mp
import pyautogui
import win32api
from math import dist, sqrt


def find_pos():
    handLM = mp.solutions.hands
    hand = handLM.Hands(max_num_hands=4)
    draw = mp.solutions.drawing_utils

    click = 0

    cap = cv2.VideoCapture(0)

    while 1:
        _, img = cap.read()
        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_w, img_h, centr = img.shape

        res = hand.process(img_rgb)

        if res.multi_hand_landmarks:
            for landmarks in res.multi_hand_landmarks:
                for id, lm in enumerate(landmarks.landmark):
                    draw.draw_landmarks(img, landmarks, handLM.HAND_CONNECTIONS)


        if res.multi_hand_landmarks != None:
            for handLandmarks in res.multi_hand_landmarks:
                for point in handLM.HandLandmark:
                    normalizedaHandLand = handLandmarks.landmark[point] # point это точка
                    normalizadePixelCord = draw._normalized_to_pixel_coordinates(normalizedaHandLand.x, normalizedaHandLand.y, img_w, img_h)

                    point = str(point)
                    if point == 'HandLandmark.INDEX_FINGER_TIP':
                        finger_x = normalizadePixelCord[0]
                        finger_y = normalizadePixelCord[1]
                        win32api.SetCursorPos((finger_x*4, finger_y*2))

                    if point == 'HandLandmarks.THUMB_TIP':
                        finger_x1 = normalizadePixelCord[0]
                        finger_y1 = normalizadePixelCord[1]

                        dist_x = sqrt((finger_x-finger_x1)**2 + (finger_x-finger_x1)**2)
                        dist_y = sqrt((finger_y-finger_y1)**2 + (finger_y-finger_y1)**2)
                        if dist_x<5 or dist_x<-5:
                            if dist_y<5 or dist_y<-5:
                                click += 1
                                if click % 5 == 0:
                                    print('click')
                                    pyautogui.click()


        cv2.imshow('nama', img)
        
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    find_pos()