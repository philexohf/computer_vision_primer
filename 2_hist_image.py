# ===========程序功能：彩色图像直方图的绘制============ #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2
import numpy as np


def color_hist(image, color):
    hist = cv2.calcHist([image],       # 传入图像（列表）
                        [0],           # 使用的通道（使用通道：可选[0],[1],[2]）
                        None,          # 不使用mask
                        [256],         # HistSize
                        [0.0, 255.0])  # 直方图柱的范围
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)  # 矩阵元素的最大最小值和最大最小值的位置
    hist_img = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(hist_img, (h, 256), (h, 256 - intensity), color)
    return hist_img


if __name__ == '__main__':
    original_img = cv2.imread("./image/lancelot_guinevere.jpg")
    # 图像缩放，水平缩放因子fx,垂直缩放因子fy
    img = cv2.resize(original_img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)  # 拆分成B、G、R三通道

    hist_B = color_hist(b, [255, 0, 0])
    hist_G = color_hist(g, [0, 255, 0])
    hist_R = color_hist(r, [0, 0, 255])
    hist_RGB = np.hstack([hist_R, hist_G, hist_B])  # R、G、B三个直方图水平拼接

    cv2.imshow('hist', hist_RGB)
    cv2.imshow("img", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
