# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:49:42 2019

@author: Administrator
"""
import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
#import cv2

class storeData:
    def __init__(self):
        self.subscription_key = "80d68f1211af4c5aa5dac482757a9488"
        self.endpoint= 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'
        self.ImgUrl='C:\\Users\\Administrator\\Desktop\\cj_biosemester\\'
    
    def createPersongroup(self):
        personGroupId="famous27"
        body = dict()
        body["name"] = "F.A.M.O.U.S"
        body["userData"] = "All famous cast"
        #body["recognitionModel"] = "recognition_02"
        body = str(body)

        #Request URL 
        FaceApiCreateLargePersonGroup = self.endpoint+personGroupId 
        headers = {
                # Request headers
                'Content-Type': 'application/json',
                #'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': self.subscription_key
                }
        
        try:
            # REST Call 
            response = requests.put(FaceApiCreateLargePersonGroup, data=body, headers=headers) 
            print("RESPONSE:" + str(response.status_code)) 

        except Exception as e:
            print(e)
        
        return(personGroupId)
    

    def createPerson(self,personGroupId):
        famousList=['son','you','ryu']
        for i in famousList:
            body=dict()
            body["name"]=i
            body['userData']='famous'+i
            body=str(body)
    
            #Request URL 
            FaceApiCreatePerson = self.endpoint+personGroupId+'/persons' 
        
            headers = {
                    # Request headers
                    'Content-Type': 'application/json',
                    #'Content-Type': 'application/octet-stream',
                    'Ocp-Apim-Subscription-Key': self.subscription_key
                    }
    
            try:
                # REST Call 
               response = requests.post(FaceApiCreatePerson, data=body, headers=headers) 
               responseJson = response.json()
               personId = responseJson["personId"]
               print("PERSONID: "+str(personId))
    
            except Exception as e:
                print(e)
    
            personImageList=[]
        
            for j in range(1,5):
                personImageList.append(self.ImgUrl+i+'\\'+i[0]+str(j)+'.jpg')
                headers = {
                        # Request headers
                        #'Content-Type': 'application/json',
                        'Content-Type': 'application/octet-stream',
                        'Ocp-Apim-Subscription-Key': self.subscription_key
                        }  

            #Request URL 
            FaceApiCreatePerson = self.endpoint+personGroupId+'/persons/'+personId+'/persistedFaces' 

            for image in personImageList:
                body = dict()
                body["url"] = image
                body = str(body)
                data=open(image,'rb')
    
                try:
                    # REST Call 
                    response = requests.post(FaceApiCreatePerson, data=data, headers=headers) 
                    responseJson = response.json()
                    persistedFaceId = responseJson["persistedFaceId"]
                    print("PERSISTED FACE ID: "+str(persistedFaceId))
    
                except Exception as e:
                    print(e)
                    print('에러에러')
    