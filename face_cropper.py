import cv2
import sys
import os
import string   
from PIL import Image 
import random # define the random module  
S = 10

class FaceCropper(object):
    CASCADE_PATH = "haarcascade_frontalface_default.xml"

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        #cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        #self.face_cascade = cv2.CascadeClassifier(self.CASCADE_PATH)

    def generate(self, image_path, show_result):
# =============================================================================
#         try :
#             with Image.open(image_path) as im:
#                 print('ok')
#         except :
#             print(image_path)
#             os.remove(image_path)
#             return 0
# =============================================================================
        
        img = cv2.imread(image_path)
        if (img is None):
            print("Can't open image file")
            return 0

        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(img, 1.2, 4, minSize=(300, 300))
        if (faces is None):
            print('Failed to detect face')
            os.remove(image_path)
            return 0
        padding = 50
        if (show_result):
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x-padding,y-padding),(x+w+padding,y+h+padding),(255,0,0),2)
                #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)                
            #cv2.imshow('img', img)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()

        facecnt = len(faces)
        print("Detected faces: %d" % facecnt)
        i = 0
        height, width = img.shape[:2]
        for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r) 
            ny = int(centery - r)
            nr = int(r * 2)

            faceimg = img[ny-padding:ny+nr+padding, nx-padding:nx+nr+padding]
            heighta, widtha = faceimg.shape[:2]
                       
            if heighta > 256:
                if faceimg is None:
                    print('error')
                else:
                    try :
                        lastimg = cv2.resize(faceimg, (256, 256))
                        i += 1
                        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))   
                        exitpath = str(ran) + "_image_%d.jpg" % i
                        cv2.imwrite(exitpath, lastimg)
                                                #img = cv2.imread(exitpath)
                          
                        # Convert into grayscale
                        gray = cv2.cvtColor(lastimg, cv2.COLOR_BGR2GRAY)
                          
                        # Load the cascade
                        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                        i = 0
                          
                        # Detect faces
                        faces = face_cascade.detectMultiScale(gray, 1.2, 1, minSize=(256, 256))
                        if (faces is None):
                            print('Failed to detect face')
                            os.remove(exitpath)
                    except :
                        os.remove(image_path)
                        return 0
        os.remove(image_path)

if __name__ == '__main__':
    args = sys.argv
    argc = len(args)

    if (argc != 2):
        print('Usage: %s [image file]' % args[0])
        quit()

    detecter = FaceCropper()
    detecter.generate(args[1], True)
