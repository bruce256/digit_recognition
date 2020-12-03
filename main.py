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
    image = mpimg.imread(name)
    for each in image:
        for e in each:
            if e == 255:
                data.append(0)
            else:
                data.append(1)
    #print((data))
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
            train_result.append(dir)


def train():
    knn.fit(train_data, train_result)


def test_image_vectorize():
    data = []
    image = mpimg.imread("data/test/test_9.bmp")
    for each in image:
        for e in each:
            if e[0] == 255:
                data.append(0)
            else:
                data.append(1)

    print(len(data))
    tmp = [data]
    return tmp


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    traverse_dir()
    train()
    test_vec = test_image_vectorize()
    print(test_vec)
    print(train_result)
    print(len(train_result))
    print(len(train_data))
    predict_result = knn.predict(test_vec)
    # print(train_data)
    # print(train_result)
    print(predict_result)
    time.sleep(100000)
    ## print_hi('PyCharm')aa

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
