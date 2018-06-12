# encoding: utf-8
"""
@Time   : 2018/6/10 21:21
@Author : XJH
"""
import cv2

clicked = False


def onMouse(event, x, y, flags, param):
    """
    判断是否收到鼠标左键事件
    :param event: 
    :param x: 
    :param y: 
    :param flags: 
    :param param: 
    :return: 
    """
    global clicked
    if event == cv2.EVENT_LBUTTONUP:                    # 如果获取鼠标左键事件
        clicked = True



cameraCapture = cv2.VideoCapture(0)                     # 视频获取类
cv2.namedWindow('MyWindows')
cv2.setMouseCallback('MyWindows', onMouse)               # 获取键盘输入
print("showing camera feed. Click window or press any key to stop")
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyAllWindows()
cameraCapture.release()