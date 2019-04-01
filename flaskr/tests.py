import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, jsonify, session

from flask import Flask
from PIL import Image
import datetime

import os
import requests
from tasks import crop
import time
# db.init_app(app)

os.environ['NO_PROXY'] = '127.0.0.1'


import unittest 
  
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
    
    #Asserts that unique name gives 201, and duplicate gives 400
    def test_successfull_insert(self):
        url = 'http://127.0.0.1:5000/submitted'
        data = {"username":"hello"}
        files = {'file': (open("jm.png", 'rb'))}
        r = requests.post(url, files=files, data=data)
        files['file'].close()
        time.sleep(2)
        os.remove("flaskr/static/original/hello.png")
        os.remove("flaskr/static/resized/hello.png")
        self.assertEqual(r.status_code,201)
        
        data = {"username":"hello"}
        files = {'file': (open("jm.png", 'rb'))}
        r = requests.post(url, files=files, data=data)
        files['file'].close()
        self.assertEqual(r.status_code,400)

    
    #Checks that the width and height are 200 each
    def test_crop(self):
        im = Image.open("jm.png")
        crop(im,"jm.png")
        im = Image.open("flaskr/static/resized/jm.png")
        width,height = im.size
        os.remove("flaskr/static/original/jm.png")
        os.remove("flaskr/static/resized/jm.png")
        im.close()
        self.assertEqual(width,200)
        self.assertEqual(height,200)

if __name__ == '__main__': 
    unittest.main() 

