#!/usr/bin/python

from PIL import Image
from os import listdir
from os.path import isfile, join
import math

_PATH = './icons/'

_QTD = 20

q = 0
for f in listdir(_PATH):
	file_name = join(_PATH, f)
	if isfile(file_name):
		img = Image.open(file_name, 'r')
		img_w, img_h = img.size
		print file_name, '(', img_w, 'x', img_h, ')'
		q = q + 1

sprite_w = math.modf(math.sqrt(q))[1]
sprite_h = math.modf(q / sprite_w)

if sprite_h[0] > 0:
	sprite_h = sprite_h[1] + 1
else:
	sprite_h = sprite_h[1]
	
sprite_w, sprite_h = (int(sprite_w * 32), int(sprite_h * 32))

print q, sprite_w, sprite_h

background = Image.new('RGBA', (sprite_w, sprite_h), (255, 0, 0, 255))



#print img_w, img_h

#

#for c in range(0, __QTD):#
#	background.paste(img, (0, (img_h) * c))

background.save('out.png')
