import cv2
import numpy as np
import pywt

# 读取原始图像和水印图像
img = cv2.imread('R.jpg')
watermark = cv2.imread('2023-04-20 140536.png', 0)

# 对水印图像进行小波变换
coeffs_watermark = pywt.wavedec2(watermark, 'haar', level=1)
coeffs_watermark = np.tile(coeffs_watermark, (113, 1, 1))

# 对原始图像进行小波变换
coeffs_img = pywt.wavedec2(img, 'haar', level=1)

# 将水印嵌入到低频分量中
coeffs_img = list(coeffs_img)
coeffs_img[0] = (coeffs_img[0][0], coeffs_img[0][1] + coeffs_watermark, coeffs_img[0][2])

# 对嵌入了水印的原始图像进行小波逆变换
watermarked_img = pywt.waverec2(coeffs_img, 'haar')

# 保存结果
cv2.imwrite('watermarked_image.jpg', watermarked_img)
