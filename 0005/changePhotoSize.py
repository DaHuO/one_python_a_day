# -*- coding: UTF-8 -*-

from os import listdir
from PIL import Image


def changePhotoSize():
    files = [f for f in listdir('pics')]
    ip5x = 1136.0
    ip5y = 640.0
    for pic in files:
        if pic[0]=='.':
            continue
        img = Image.open('pics/' + pic)
        img_name, img_format = parseName(pic)
        width, height = img.size
        imgy, imgx = sorted([width, height])
        tx = imgx / ip5x
        ty = imgy / ip5y
        if tx<1 and ty<1:
            img.save('pics_new/' + pic, img_format)
            continue
        if tx>=ty:
            imgx = ip5x
            imgy = imgy / tx
            img.thumbnail((imgx,imgy),Image.ANTIALIAS)
            img.save('pics_new/' + pic, img_format)
            continue
        if tx<ty:
            imgy = ip5y
            imgx = imgx / ty
            img.thumbnail((imgx,imgy),Image.ANTIALIAS)
            img.save('pics_new/' + pic, img_format)
            continue

def parseName(image_name):
    image = image_name.split('.')
    if image[1].lower() == 'jpg':
        image[1] = 'JPEG'
    return image[0], image[1]

if __name__ == '__main__':
    changePhotoSize()
