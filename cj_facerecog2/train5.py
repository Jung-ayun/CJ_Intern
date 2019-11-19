# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:39:14 2019

@author: setgo
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests


class Train:
    def __init__(self):
        self.subscription_key = "80d68f1211af4c5aa5dac482757a9488"
        self.endpoint= 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'
        self.ImgUrl='C:\\Users\\Administrator\\Desktop\\cj_biosemester\\'
    
    def trainModel(self,personGroupId):
        body = dict()
        #Request URL
        FaceApiTrain = self.endpoint+personGroupId+'/train'
        headers = {
            # Request headers
            'Content-Type': 'application/json',
            #'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.subscription_key
            }
        try:
        # REST Call 
            response = requests.post(FaceApiTrain, data=body, headers=headers) 
            print("RESPONSE:" + str(response.status_code))

        except Exception as e:
            print(e)
    