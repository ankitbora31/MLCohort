import os
import pandas as pd
import cv2


def task2(folder, csv_file):
    obj = os.listdir(folder)
    df = pd.read_csv(csv_file)
    img_arr = []
    for im in obj:
        img_arr.append(im)
    xmin = df['xmin'].tolist()
    ymin = df['ymin'].tolist()
    xmax = df['xmax'].tolist()
    ymax = df['ymax'].tolist()
    label = df['label'].tolist()
    width = df['width'].tolist()

    for i in range(len(img_arr)):
        img = cv2.imread(f'{folder}/{img_arr[i]}')
        img = cv2.rectangle(img, (xmin[i], ymin[i]), (xmax[i], ymax[i]), (i * 20, i * 16, i * 10), 2)
        img = cv2.putText(img, label[i], (0, width[i] // 2), font, 1, (i*20, i*16, i*10), 2)
        if img is not None:
            cv2.imwrite(f'C:/Users/ankit/PycharmProjects/cuvette/Task2_result/box_{i}.jpg', img)


if __name__ == "__main__":
    directory = input("Directory name: ")
    data = input("csv File: ")
    font = cv2.FONT_HERSHEY_SIMPLEX
    task2(directory, data)
