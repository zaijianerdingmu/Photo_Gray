import numpy as np
import matplotlib.pyplot as plt
import cv2

# 灰度化
img = cv2.imread("picture2.png")
h, w = img.shape[:2]  # 获取图片的high和wide
img_gray = np.zeros([h, w], img.dtype)  # 创建一张和当前图片大小一样的单通道图片
for i in range(h):
    for j in range(w):
        m = img[i, j]  # 取出当前high和wide中的BGR坐标
        img_gray[i, j] = int(m[0] * 0.11 + m[1] * 0.59 + m[2] * 0.3)  # 将BGR坐标转化为gray坐标并赋值给新图像
print(img_gray[2,1])
# 二值化
img_binary = np.where(img_gray/255 >= 0.5, 1, 0)

# 画图
img = plt.imread("picture2.png")
plt.subplot(221)
plt.imshow(img)
plt.title('Color map')

plt.subplot(222)
plt.imshow(img_gray, cmap='gray')
plt.title('gray')
plt.savefig("example2")

plt.subplot(223)
plt.imshow(img_binary, cmap='gray')
plt.title('img_binary')
plt.savefig('mytestplt.png')
plt.show()
