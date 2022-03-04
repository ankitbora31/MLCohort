import pandas as pd
import os
import cv2

df = pd.read_csv('C:/Users/ankit/PycharmProjects/cuvette/Task3_data/train_labels.csv')

id = df['id'].tolist()
labels = df['label'].tolist()

