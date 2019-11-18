# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
import cv2
from io import BytesIO
from PIL import Image,ImageDraw
import cognitive_face as CF 
import numpy as np


# set to your own subscription key value
subscription_key = "80d68f1211af4c5aa5dac482757a9488"
assert subscription_key



# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'
#CF.BaseUrl.set(face_api_url)

#image_url='https://github.com/kairess/simple_face_recognition/blob/master/img/neo.jpg'
#image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'
image_url='C:\\Users\\Administrator\\Desktop\\cj 인턴자료\\ryu\\r1.jpg'
#faces =CF.face.detect(image_url,True,False,'age,gender')
headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

#def getRectangle(faceDictionary):
#    rect= faceDictionary['faceRectangle']
#    left = rect['left']
#    top = rect['top']
#    bottom = left + rect['height']
#    right = top + rect['width']
#    return ((left, top), (bottom, right))

#img=Image.open(image_url)
#draw = ImageDraw.Draw(img)
#for face in faces:
#    draw.rectangle(getRectangle(face),outline='red')
#img.show()
#def showImage():
 #  image = cv2.imread(image_url,cv2.IMREAD_COLOR)
   # cv2.namedWindow('1',cv2.WINDOW_NORMAL)
   # print(image)
    #cv2.imshow('1',image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
data=open(image_url,'rb')
response = requests.post(face_api_url, params=params,
                         headers=headers, data=data)
print(response.json())
print(json.dumps(response.json()))
#showImage()