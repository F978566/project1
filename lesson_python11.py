import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    cap = cv2.VideoCapture(0)

    while 1:
        _, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower_red = np.array([30, 150, 50])
        upper_red = np.array([255, 255, 180])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img, img, mask=mask)

        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        if cv2.waitKey(5) & 0xff == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()