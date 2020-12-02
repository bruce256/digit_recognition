# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.、

import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np
import os

train_data = []
train_result = []

train_dir = "data/train"


def image_vectorize(name):
    data = []
    lena = mpimg.imread(name)  # 读取和代码处于同一目录下的 lena.png
    for each in lena:
        data.extend(each)

    train_data.append(data)
    print(data)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def traverse_dir():
    dirs = os.listdir(train_dir)
    print(dirs)
    for dir in dirs:
        current_dir = train_dir + "/" + dir
        files = os.listdir(current_dir)
        for file in files:
            image_vectorize(current_dir + "/" + file)
            train_result.extend(dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    traverse_dir()
    print(train_data)
    print(train_result)
    ## print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
