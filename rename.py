#coding:utf-8
import os

image_dir = input('input the image dir:')
image_names = os.listdir(image_dir)
count = 1
for image in image_names:
    stuffix = image[-3:]
    new_name = 'image' + str(count)+"."+stuffix
    os.rename(image_dir+"/"+image,image_dir+"/"+new_name)
    count = count+1