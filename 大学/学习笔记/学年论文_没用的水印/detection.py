
import cv2
import numpy as np
import random


def encode(img_path, wm_path, res_path, alpha):
    img = cv2.imread(img_path)
    cv2.imshow("a",img)
    img_f = np.fft.fft2(img)
    height, width, channel = img.shape
    watermark = cv2.imread(wm_path)
    wm_height, wm_width = watermark.shape[:2]
    x = np.random.permutation(height // 2)
    y = np.random.permutation(width)
    tmp = np.zeros(img.shape)
    for i, x_i in enumerate(x):
        for j, y_j in enumerate(y):
            if x_i < wm_height and y_j < wm_width:
                tmp[x_i, y_j] = watermark[x_i, y_j]
                tmp[height - 1 - x_i, width - 1 - y_j] = tmp[x_i, y_j]
    res_f = img_f + alpha * tmp
    res = np.real(np.fft.ifft2(res_f))
    cv2.imwrite("text.jpg", res,[int(cv2.IMWRITE_JPEG_QUALITY), 100])


def decode(img_path, wm_path, alpha):
    img = cv2.imread(img_path)
    img_f = np.fft.fft2(img)
    height, width, channel = np.shape(img)
    watermark = cv2.imread(wm_path)
    wm_height, wm_width = watermark.shape[0], watermark.shape[1]
    x, y = list(range(int(height / 2))), list(range(width))
    random.seed(height + width)
    random.shuffle(x)
    random.shuffle(y)
    tmp = np.zeros(img.shape)
    for i in range(int(height / 2)):
        for j in range(width): 
            if x[i] < wm_height and y[j] < wm_width:
                tmp[i][j] = watermark[x[i]][y[j]]
                tmp[height - 1 - i][width - 1 - j] = tmp[i][j]
    wm_f = np.fft.fft2(tmp)
    res_f = (img_f - wm_f) / alpha
    res = np.fft.ifft2(res_f)
    res = np.real(res)
    diff = res - img
    diff = np.abs(diff)
    diff = np.uint8(diff)
    _, thresh = cv2.threshold(diff, 240, 255, cv2.THRESH_BINARY_INV)
    #cv2.imshow("-",_)
    return thresh


b = "2023-04-20 140536.png"
a = "2023-04-20 140554.png"

c = "D:study\python_1/formal"
encode('twxt.jpg','2023-04-20 140536.png',c,10)
a=decode("formal/2023-04-20 140536.png","text.jpg",20)
cv2.imshow("a",a)

cv2.waitKey(0)
cv2.destroyAllWindows()