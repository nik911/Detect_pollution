import cv2
import numpy as np
from matplotlib import pyplot as plt


class VideoCamera(object):
    #def __init__(self):
    #    img = cv2.imread('1-1.png', cv2.IMREAD_COLOR)

    #def __del__(self):
        # Конец

    def get_frame(self):
        img = cv2.imread('1-1.png', cv2.IMREAD_COLOR)
        # Пофиксим :)
        img3 = cv2.imread('1-2.png', cv2.IMREAD_COLOR)

        min_area = 60
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b, g, r = cv2.split(img)
        img2 = cv2.merge([abs(((r - g) / (r + g)) * 0.3), abs(((r - g) / (r + g)) * 0.3), abs(((r - g) / (r + g)) * 0.3)])

        mask = cv2.inRange(img2, 65, 255)
        fgMask = cv2.Canny(mask, 10, 100, 3)

        contours_prev, hierarchy = cv2.findContours(fgMask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        for i in contours_prev:
            (x, y, w, h) = cv2.boundingRect(i)
            if cv2.contourArea(i) > min_area:
                img3 = cv2.rectangle(img3, (x, y), (x + w, y + h), (255, 0, 0), 2)
                img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)

        plt.imshow(img2)
        plt.show()

        # Пофиксим  :)
        ret, jpeg = cv2.imencode('.jpg', img3)
        return jpeg.tobytes()