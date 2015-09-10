#!/usr/bin/python

from PIL import Image
from os import listdir
from os.path import isfile, join
import math
import sys

_PATH = './icons/'

_QTD = 20

_W = 32
_H = 32


img_list = []

q = 0

for f in listdir(_PATH):
    file_name = join(_PATH, f)
    if isfile(file_name):
        img = Image.open(file_name, 'r')
        
        img_w, img_h = img.size
        print file_name, '(', img_w, 'x', img_h, ')'
        
        if (img_w == _W and img_h == _H):
            img_list.append(img)
            q += 1

if (q == 0):
    sys.exit("No Images.")

print img_list

sprite_w = math.modf(math.sqrt(q))[1]
sprite_h = math.modf(q / sprite_w)

if sprite_h[0] > 0:
    sprite_h = sprite_h[1] + 1
else:
    sprite_h = sprite_h[1]

sprite_w, sprite_h = (int(sprite_w * 32), int(sprite_h * 32))

print q, sprite_w, sprite_h

background = Image.new('RGBA', (sprite_w, sprite_h), (255, 0, 0, 255))


for c in img_list:
    background.paste(img, (0, (img_h) * c))

background.save('out.png')
background.show()
