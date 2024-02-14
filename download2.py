#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:05:44 2022

@author: u1
"""
from face_cropper import FaceCropper
#import face_cropper

from google_images_download import google_images_download   #importing the library
S = 10

response = google_images_download.googleimagesdownload()   #class instantiation

with open('daerah.txt') as f:
   for line in f:
       # For Python3, use print(line)
       try:
           arguments = {"keywords":"%s" % line,"limit":1000, "size": ">6MP", "chromedriver": "/usr/bin/chromedriver"}   #creating list of arguments
           paths = response.download(arguments)   #passing the arguments to the function

           for x in paths:
               if isinstance(x, int) :
                   break
               for path in x[line]:
    		       #print(path)
                   if isinstance(path, int) :
                       break
    		       #print(paths)
                   detecter = FaceCropper()
                   detecter.generate(path, False)
       except Exception:
           print(line + "An exception occurred")
           continue
		       # Read the input image


#print(paths)   #printing absolute paths of the downloaded images
