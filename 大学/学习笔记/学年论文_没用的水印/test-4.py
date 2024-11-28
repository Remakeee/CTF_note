
import cv2
import numpy as np


# 读取图像
img = cv2.imread('2023-04-20 140554.png')

\

# 将图像转换为浮点数格式
img_float = np.float32(img)

# 定义高斯核大小和标准差
ksize = (5, 5)
sigma = 1.0

# 使用高斯滤波器平滑图像
img_smooth = cv2.GaussianBlur(img_float, ksize, sigma)

# 将浮点数格式的图像转换为整数格式
img_smooth = np.uint8(img_smooth)

#img = cv2.imread('2023-04-20 140554.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_b, img_g, img_r = cv2.split(img_smooth)

watermark = np.zeros(gray_img.shape, np.uint8)
cv2.putText(watermark, 'My Watermark', (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2)
watermark_fft = np.fft.fft2(watermark)
watermark_fft_shift = np.fft.fftshift(watermark_fft)



watermark_fft = np.fft.fft2(gray_img)
watermark_magnitude = np.abs(watermark_fft.real)
#watermark_magnitude = watermark_fft.real

watermark_phase_b = np.angle(watermark_fft.imag)
watermark_phase_g = np.angle(watermark_fft.imag)
watermark_phase_r = np.angle(watermark_fft.imag)

f_b = np.fft.fft2(img_b)
f_g = np.fft.fft2(img_g)
f_r = np.fft.fft2(img_r)

fshift_b = np.fft.fftshift(f_b)
fshift_g = np.fft.fftshift(f_g)
fshift_r = np.fft.fftshift(f_r)





alpha = 0.99
combined_fft_shift_b = alpha*fshift_b + (1-alpha)*watermark_fft_shift
combined_fft_shift_g = alpha*fshift_g + (1-alpha)*watermark_fft_shift
combined_fft_shift_r = alpha*fshift_r + (1-alpha)*watermark_fft_shift






fshift_b_complex = fshift_b#np.zeros_like(fshift_b, dtype=complex)
fshift_g_complex = fshift_g#np.zeros_like(fshift_g, dtype=complex)
fshift_r_complex = fshift_r#np.zeros_like(fshift_r, dtype=complex)

fshift_b_complex.real = fshift_b.real
fshift_b_complex.imag = watermark_magnitude * np.exp(1j * watermark_phase_b)
fshift_g_complex.real = fshift_g.real
fshift_g_complex.imag = watermark_magnitude * np.exp(1j * watermark_phase_b)
fshift_r_complex.real = fshift_r.real
fshift_r_complex.imag = watermark_magnitude * np.exp(1j * watermark_phase_b)


img_back_complex_b_1 = np.fft.ifft2(np.fft.ifftshift(combined_fft_shift_b))
img_back_complex_g_1 = np.fft.ifft2(np.fft.ifftshift(combined_fft_shift_g))
img_back_complex_r_1 = np.fft.ifft2(np.fft.ifftshift(combined_fft_shift_r))
img_back_b_1 = np.abs(img_back_complex_b_1)
img_back_g_1 = np.abs(img_back_complex_g_1)
img_back_r_1 = np.abs(img_back_complex_r_1)
img_back_normalized_b_1 = cv2.normalize(img_back_b_1, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
img_back_normalized_g_1 = cv2.normalize(img_back_g_1, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
img_back_normalized_r_1 = cv2.normalize(img_back_r_1, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
img_back_normalized_2 = cv2.merge((img_back_normalized_b_1, img_back_normalized_g_1,img_back_normalized_r_1))
cv2.imshow('img_back_normalized_2',img_back_normalized_2)

gray = cv2.cvtColor(img_back_normalized_2, cv2.COLOR_BGR2GRAY)
fft = np.fft.fft2(gray)
fft_shift = np.fft.fftshift(fft)
magnitude_spectrum = 20*np.log(np.abs(fft_shift))
cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))


img_back_complex_b = np.fft.ifft2(np.fft.ifftshift(fshift_b_complex))
img_back_complex_g = np.fft.ifft2(np.fft.ifftshift(fshift_g_complex))
img_back_complex_r = np.fft.ifft2(np.fft.ifftshift(fshift_r_complex))

img_back_b = np.abs(img_back_complex_b)
img_back_g = np.abs(img_back_complex_g)
img_back_r = np.abs(img_back_complex_r)

img_back_normalized_b = cv2.normalize(img_back_b, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
img_back_normalized_g = cv2.normalize(img_back_g, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
img_back_normalized_r = cv2.normalize(img_back_r, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

img_back_normalized_1 = cv2.merge((img_back_normalized_b, img_back_normalized_g,img_back_normalized_r))
cv2.imshow('img_back_normalized_1',img_back_normalized_1)

print("1")
cv2.waitKey(0)
cv2.destroyAllWindows()








# 将图像转换为灰度图像
gray = cv2.cvtColor(img_back_normalized_2, cv2.COLOR_BGR2GRAY)

# 计算灰度图像的傅里叶变换
fft = np.fft.fft2(gray)

# 将频谱移动到中心位置
fft_shift = np.fft.fftshift(fft)

# 恢复到空域图像
recovered_img = np.fft.ifft2(np.fft.ifftshift(fft_shift)).real

# 二值化处理
threshold, recovered_img = cv2.threshold(recovered_img, 240, 255, cv2.THRESH_BINARY_INV)

# 显示恢复的水印
cv2.imshow('Recovered Watermark', recovered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
