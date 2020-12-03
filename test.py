import matplotlib.image as mpimg  # mpimg 用于读取图片
import cv2
import numpy as np

# read an image using imread() function of cv2
# we have to  pass only the path of the image


def test_image_vectorize():
    data = []
    lena = mpimg.imread("data/test/test_9.bmp")  # 读取和代码处于同一目录下的 lena.png
    print(lena)
    for each in lena:
        for e in each:
            if e[0] == 255:
                data.append(0)
            else:
                data.append(1)
    print(data)
    print(len(data))

    arr = np.arange(784).reshape((28, 28))
    for i in range(28):
        for j in range(28):
            arr[i][j] = data[i * 28 + j]
    print(arr)
    return data


def rbg():
    img = cv2.imread("data/test/test_8.bmp")
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    data = mpimg.imread(HSV_img)
    print(data)


#rbg()
test_image_vectorize()

