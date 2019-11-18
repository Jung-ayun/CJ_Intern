# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:11:49 2019

@author: Administrator
"""

import requests
import json
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.
subscription_key = "80d68f1211af4c5aa5dac482757a9488"
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'


# Set image_path to the local path of an image that you want to analyze.
image_path = "C:\\Users\\Administrator\\Desktop\\cj 인턴자료\\ryu\\ryu5.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
          'Content-Type': 'application/octet-stream'}
#headers = {'Ocp-Apim-Subscription-Key': subscription_key}
#params = {'visualFeatures': 'Categories,Description,Color'}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(
    face_api_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

#response = requests.post(face_api_url, params=params,
#                         headers=headers, json={"url": image_url})
print(response)
print(json.dumps(response.json()))
#The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
#analysis = response.json()
#print(analysis)
#image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
#image = Image.open(BytesIO(image_data))
#plt.imshow(image)
#plt.axis("off")
#_ = plt.title(image_caption, size="x-large", y=-0.1)