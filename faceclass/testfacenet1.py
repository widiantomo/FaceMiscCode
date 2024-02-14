#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:20:18 2022

@author: l
"""
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import numpy as np
import os

# If required, create a face detection pipeline using MTCNN:
#mtcnn = MTCNN(image_size=160, margin=0)
mtcnn = MTCNN()

# Create an inception resnet (in eval mode):
resnet = InceptionResnetV1(pretrained='vggface2').eval()#

directory = '/home/l/picproject/google-images-download/FaceOfIndonesia'
#/home/l/picproject/google-images-download/FaceOfIndonesia/

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = Image.open(f)
        newsize = (160, 160)
        img = img.resize(newsize)
        face_tensor, prob = mtcnn(img, save_path='./WNFKVMY4AW_image_x.jpg', return_prob=True)
        if prob is None:
            os.remove(f)