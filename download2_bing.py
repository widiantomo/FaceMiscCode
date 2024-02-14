#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:12:38 2022

@author: u1
"""

import os

#response = bing()   #class instantiation

with open('daerah3.txt') as f:
   for line in f:
       # For Python3, use print(line)
           os.system("python3 bbid.py -o pasfoto -a -t 5 %s" % line)

       
               #print(paths)   
# =============================================================================
#                detecter = FaceCropper()
#                detecter.generate(path, False)
# =============================================================================
              
               # Read the input image
#print(paths)   #printing absolute paths of the downloaded images