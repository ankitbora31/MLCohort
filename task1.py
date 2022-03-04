import os
import cv2


def img_to_gray(directory_name):
    obj = os.listdir(directory_name)
    img_array = []
    for n in obj:
        img = cv2.imread(os.path.join(directory_name, n), 0)
        img_array.append(img)
        cv2.imwrite(f'C:/Users/ankit/PycharmProjects/cuvette/Task1_result/gray_{n}', img)
    return img_array

# driver
if __name__ == "__main__":
    directory = input("Directory Name: ")
    imgs = img_to_gray(directory)
    print(len(imgs))