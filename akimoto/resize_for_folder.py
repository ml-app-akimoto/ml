import cv2
import glob
import re
import os

# ある特定のファイル内の写真をリサイズし、同一ファイル内に保存する

FOLDER = "imgs/akb_pre"
IMG_SIZE = 64

files = glob.glob(f'{FOLDER}/*.jpg')
# files = ["imgs/000002_cropped.jpg"]
print(len(files))

def crop_squre(img):
    h, w, c = img.shape
    x = w if h > w else h
    y = x

    # top = int((h - y) / 2)
    top = 0
    bottom = top + y
    left = int((w - x) / 2)
    right = left + x

    img = img[top:bottom, left:right]
    return img

# files = ['./imgs/saka/000002.jpg', './imgs/akb/000067.jpg']

for file in files:

    img = cv2.imread(file)
    img = crop_squre(img)

    img = cv2.resize(img, dsize=(IMG_SIZE, IMG_SIZE))

    cv2.imwrite(file, img)
