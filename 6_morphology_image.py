# ============程序功能：图像的形态学处理============== #
# https://github.com/philexohf/Computer_Vision_Primer
import cv2

srcImg = cv2.imread('./image/summer.png')
cv2.namedWindow('src', 1)
cv2.imshow('src', srcImg)
# 构造一个3×3的结构元素
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate = cv2.dilate(srcImg, element)
erode = cv2.erode(srcImg, element)
# 将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
result = cv2.absdiff(dilate, erode)
# 上面得到的结果是灰度图，将其二值化以便更清楚的观察结果
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
print("retval=" + str(retval))
# 反色，即对二值图每个像素取反
result = cv2.bitwise_not(result)

cv2.namedWindow("alter", 0)
cv2.imshow("alter", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
