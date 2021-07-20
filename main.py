from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

'''
import numpy as np
import cv2
from matplotlib import pyplot as plt


def detector_pollution(img):
    min_area = 60
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([((r - g) / (r + g)) * 0.3, ((r - g) / (r + g)) * 0.3, ((r - g) / (r + g)) * 0.3])

    mask = cv2.inRange(im_rgb, 65, 255)
    fgMask = cv2.Canny(mask, 10, 100, 3)

    contours_prev, hierarchy = cv2.findContours(fgMask.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    for i in contours_prev:
        (x, y, w, h) = cv2.boundingRect(i)
        if cv2.contourArea(i) > min_area:
            img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)

    plt.imshow(img2)
    plt.show()


if __name__ == '__main__':
    img = cv2.imread('1-1.png', cv2.IMREAD_COLOR)
    detector_pollution(img)

'''