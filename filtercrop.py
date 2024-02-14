#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:31:03 2022

@author: u1
"""
from face_cropper import FaceCropper
#import face_cropper
import os
rootdir = '/home/u1/pic/google-images-download/downloads'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        #FaceCropper.generate(os.path.join(subdir, file), True)
        detecter = FaceCropper()
        detecter.generate(os.path.join(subdir, file), True)
        #os.system("python3 face_cropper.py "+ os.path.join(subdir, file))
        #face_cropper(os.path.join(subdir, file))
        