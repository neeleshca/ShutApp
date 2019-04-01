import time
from inspect import getsourcefile
from os import path
from os.path import abspath
from PIL import Image
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, jsonify, session


#crops to 200x200
PATH = abspath(getsourcefile(lambda: 0)).rsplit("/", 1)[0]
def crop(file,name):
    # print(file)
    # name = file.filename
    print('Starting task')
    target_o = path.join(PATH, "static", "original", name)
    target_r = path.join(PATH, "static", "resized", name)

    image = file
    # with Image.open(file) as image:
    image.save(target_o, image.format)
    # size = 200, 200
    # with Image.open(file) as image:
    image = image.resize((200,200))
    # image.thumbnail(size)
    image.save(target_r, image.format)

    # for i in range(seconds):
    #     print(i)
    #     time.sleep(1)
    print('Task completed')