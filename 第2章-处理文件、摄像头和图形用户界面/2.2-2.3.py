"""
2.3.1 使用manager.CaptureManager提取视频流
"""
import cv2
import numpy
import time

class CaptureManger(object):
    def __init__(self, capture, previewWindowManager=None, shouldMirrorPreview=False):
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        self._startTime = None
        self._frameElapsed = long(0)
        self._fpsEstimate = None