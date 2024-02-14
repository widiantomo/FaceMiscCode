#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:54:15 2022

@author: u1
"""


import cv2
import os
import string  
import random # define the random module  
S = 10
rootdir = '/home/u1/pic/google-images-download/downloads'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        image_path = os.path.join(subdir, file)
        # Read the input image
        img = cv2.imread(image_path)
          
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
          
        # Load the cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        i = 0
          
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.4, 1)
        if (faces is None):
            print('Failed to detect face')
            os.remove(image_path)
        #cv2.imwrite('face.jpg', faces)
                  
        # Display the output
        #cv2.imwrite('detcted.jpg', img)
        #cv2.waitKey()
    