import cv2


videoCapture = cv2.VideoCapture('ow_reunion.mp4')
# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('fps={}, size={}'.format(fps, size))

saveImage = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', saveImage, fps, size)

cv2.namedWindow('Video', 0)
cv2.namedWindow('dstVideo', 0)
# 读帧
success, frame = videoCapture.read()
while success:
    cv2.imshow('Video', frame)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyImage = cv2.Canny(grayImage, 50, 150)
    dst = cv2.bitwise_and(frame, frame, mask=cannyImage)
    cv2.imshow('dstVideo', dst)
    out.write(dst)
    qKey = cv2.waitKey(int(1000 / fps))
    if qKey == (ord('q') or ord('Q')):
        break
    success, frame = videoCapture.read()  # 获取下一帧

videoCapture.release()
