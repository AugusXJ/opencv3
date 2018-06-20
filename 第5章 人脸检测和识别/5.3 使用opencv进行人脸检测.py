# -*- coding: utf-8 -*-
"""
@Time    : 19/06/18 09:38
@Author  : XJH
"""

import cv2

filename = '../test.jpg'

def detect(filename):
    """
    根据图片进行人脸检测
    :param filename:
    :return:
    """
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (80, 80))
        for (ex, ey, ew, eh) in eyes:
            img = cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.namedWindow('Vikings Detected!!')                  # 创建窗口
    cv2.imshow('Vikings Detected!!', img)
    cv2.imwrite('./5_3.jpg', img)
    cv2.waitKey()


def detect2():
    """
    视频中的人脸检测
    :return:
    """
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    while(True):
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        cv2.imshow("camera", frame)
        # cv2.waitKey(1)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()


def test():
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        cv2.imshow("camera", frame)
        cv2.waitKey(1)
    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect(filename)
    # detect2()
    # test()