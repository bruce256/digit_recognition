# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.、
import time

import matplotlib.image as mpimg  # mpimg 用于读取图片
import os
from sklearn.neighbors import KNeighborsClassifier


train_data = []
train_result = []
knn = KNeighborsClassifier(n_neighbors=1)

train_dir = "data/train"


def image_vectorize(name):
    data = []
    lena = mpimg.imread(name)  # 读取和代码处于同一目录下的 lena.png
    for each in lena:
        data.extend(each)
    print(len(data))
    train_data.append(data)
    # print(data)
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def traverse_dir():
    dirs = os.listdir(train_dir)
    print(dirs)
    for dir in dirs:
        current_dir = train_dir + "/" + dir
        files = os.listdir(current_dir)
        for file in files:
            image_vectorize(current_dir + "/" + file)
            train_result.extend(dir)


def train():
    knn.fit(train_data, train_result)


def test_image_vectorize():
    data = []
    lena = mpimg.imread("data/test/test_8.bmp")  # 读取和代码处于同一目录下的 lena.png
    #print(lena)
    for each in lena:
        for e in each:
            data.extend(e)

    print(len(data))
    tmp = [data]
    return tmp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    traverse_dir()
    train()
    test_vec = test_image_vectorize()
    print(test_vec)
    predict_result = knn.predict(test_vec)
    # print(train_data)
    #print(train_result)
    print(predict_result)
    time.sleep(100000)
    ## print_hi('PyCharm')aa

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
