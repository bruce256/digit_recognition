import matplotlib.image as mpimg  # mpimg 用于读取图片


def test_image_vectorize():
    data = []
    lena = mpimg.imread("data/test/test_8_1.bmp")  # 读取和代码处于同一目录下的 lena.png
    #print(lena)
    for each in lena:
        for e in each:
            data.extend(e)
    print(data)
    print(len(data))
    return data


test_image_vectorize()

