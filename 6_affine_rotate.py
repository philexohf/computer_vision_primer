import cv2
import numpy as np


srcImg = cv2.imread('./image/summer.png')
cv2.namedWindow('summer', 0)

while True:
    for i in range(360):
        theta = i*np.pi/180  # 定义角度
        # 定义仿射矩阵
        rotArr = np.array([
            [np.cos(theta), -np.sin(theta), 1000],
            [np.sin(theta), np.cos(theta), 1000]
        ], dtype=np.float32)
        # 调用仿射变换函数
        rotImg = cv2.warpAffine(srcImg, rotArr, (2000, 2000))
        cv2.imshow('summer', rotImg)
        cv2.waitKey(30)

cv2.destroyAllWindows()