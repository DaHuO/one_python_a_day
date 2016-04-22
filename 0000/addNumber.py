# -*- coding: UTF-8 -*-

import sys
from PIL import Image, ImageDraw, ImageFont

def addNumber(img, image_name, number):
    newPicName, img_format = getNewName(image_name)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    size_for_number = min(width,height)/4
    number_length = getNumberLength(number)
    font = ImageFont.truetype('arial.ttf', size_for_number)
    draw.text((width - size_for_number/1.6*number_length, 0), str(number),\
        font = font)
    img.show()
    img.save(newPicName, img_format)


def getNewName(image_name):
    image = image_name.split('.')
    return image[0] + '_new.' + image[1], image[1]

def getNumberLength(number):
    """
        used to get the length of the number, otherwise when the number is more
        than 9, bugs will show up that the number can not display completely.
    """
    number = int(number)
    count = 0
    while(number):
        count += 1
        number /= 10
    return count

if __name__ == "__main__":
    image_name = 'test.png'
    number = 0
    if len(sys.argv) == 1:
        pass
    else:
        image_name = sys.argv[1]
        number = sys.argv[2]
    img = Image.open(image_name)
    addNumber(img, image_name, number)
