# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:50:51 2019

@author: setgo
"""

import http.client, urllib.request, urllib.parse, urllib.error
import requests
import cv2

class Test:
    def __init__(self):
        self.subscription_key = "80d68f1211af4c5aa5dac482757a9488"
        self.endpoint= 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'
        self.ImgUrl='C:\\Users\\Administrator\\Desktop\\cj_biosemester\\'
    
    def faceDetect(self):
        body = dict()
        body["url"]= self.ImgUrl+'you\\y1.jpg'
        img_bgr= cv2.imread(body['url'],cv2.IMREAD_COLOR)

        data=open(body['url'],'rb')
        # Request URL 
        FaceApiDetect = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true' 
        headers = {
            # Request headers
            #'Content-Type': 'application/json',
            'Content-Type': 'application/octet-stream',
            'Ocp-Apim-Subscription-Key': self.subscription_key
            }

        try:
            # REST Call 
            response = requests.post(FaceApiDetect, data=data, headers=headers) 
            responseJson = response.json()
            faceId = responseJson[0]["faceId"] 
            print("FACE ID: "+str(faceId))
            rectangle=responseJson[0]["faceRectangle"]
            top=rectangle['top']
            left=rectangle['left']
            width=rectangle['width']
            height=rectangle['height']
            bottom=left+height
            right=top+width

        except Exception as e:
            print(e)
        return(img_bgr, faceId, left, top, bottom, right)
        
    def faceidentify(self, personGroupId, img_bgr,faceID, left, top, bottom, right):
        faceIdsList = [faceID]
        faceIdsList.append(faceID)
        # Request Body
        body = dict()
        body["personGroupId"] = personGroupId
        body["faceIds"] = faceIdsList
        body["maxNumOfCandidatesReturned"] = 1 
        body["confidenceThreshold"] = 0.5
        body = str(body)
    
        # Request URL 
        FaceApiIdentify = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/identify' 
        headers = {
                # Request headers
                'Content-Type': 'application/json',
                #'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': self.subscription_key
                }
        try:
            # REST Call 
            response = requests.post(FaceApiIdentify, data=body, headers=headers) 
            responseJson = response.json()
            personId = responseJson[0]["candidates"][0]["personId"]
            confidence = responseJson[0]["candidates"][0]["confidence"]
            print("PERSON ID: "+str(personId)+ ", CONFIDENCE :"+str(confidence))
        
        except Exception as e:
            print("Could not detect")

        FaceApiGetPerson = self.endpoint+personGroupId+'/persons/'+personId

        try:
            response = requests.get(FaceApiGetPerson, headers=headers) 
            responseJson = response.json()
            print("This Is "+str(responseJson["name"]))
            cv2.putText(img_bgr,str(responseJson["name"]),(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            cv2.rectangle(img_bgr,(left,top),(bottom,right),(0,0,255),1)
            cv2.imshow('1',img_bgr)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
        except Exception as e:
            print(e)

