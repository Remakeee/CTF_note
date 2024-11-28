import cv2
import numpy as np

# 读取图像
img = cv2.imread('2023-04-20 140554.png')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行FFT变换和FFT Shift变换
fft = np.fft.fft2(gray)
fft_shift = np.fft.fftshift(fft)

# 进行对数变换，以便更好地可视化频域信息
magnitude_spectrum = 20*np.log(np.abs(fft_shift))

# 在频域的高频成分中添加水印
watermark = np.zeros(gray.shape, np.uint8)
cv2.putText(watermark, 'My Watermark', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2)
watermark_fft = np.fft.fft2(watermark)
watermark_fft_shift = np.fft.fftshift(watermark_fft)
alpha = 0.5
combined_fft_shift = alpha*fft_shift + (1-alpha)*watermark_fft_shift

# 进行FFT Shift逆变换和FFT逆变换，得到还原的彩色图像
combined_fft = np.fft.ifftshift(combined_fft_shift)
combined_ifft = np.fft.ifft2(combined_fft)
result = np.abs(combined_ifft)

# 将结果转换回彩色图像
result_color = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

# 显示原始图像、频域图像和还原的图像
cv2.imshow('Original Image', img)
cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))
cv2.imshow('Watermarked Image', result_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

