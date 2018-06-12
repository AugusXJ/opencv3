"""
2.1.4 视频文件的读写
"""
import cv2

root = 'G:/temp_data/test_mp4.mp4'
videoCapture = cv2.VideoCapture(root)
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi',
                              cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)  # 未压缩的YUV进行编码
success, frame = videoCapture.read()        # 获取帧
while success:                  # Loop until there are no more frames
    videoWriter.write(frame)
    success, frame = videoCapture.read()