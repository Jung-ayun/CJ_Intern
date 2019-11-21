# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:49:22 2019

@author: setgo
"""


import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import cv2
import pymongo
import pprint
#myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#mydb=myclient["employee"]
#mycol=mydb["person"]

#mydict={"name":"jay","personId":"afdsfasdf"}
#x=mycol.insert_one(mydict)
#print(x.inserted_id)
#print(myclient.list_database_names())

class storeData:
    def __init__(self):
        self.subscription_key = "80d68f1211af4c5aa5dac482757a9488"
        self.endpoint= 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'
        self.ImgUrl='C:\\Users\\Administrator\\Desktop\\cj_biosemester\\'
    
    def createPersongroup(self):
        personGroupId="famous34"
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
    
    def newPerson(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb=myclient["employee"]
        mycol=mydb["person"]
        name = str(input("이름을 입력하세요 : "))
        
        personDict={"name":name}
        mycol.insert_one(personDict)
        
        for i in mycol.find(personDict):
            personID=i['_id']
            personID=repr(personID)
        return name, personID
        
        
    def savePersonImage(self,personID,personList,name):
        cap =cv2.VideoCapture(0)
        frame_count = 0
        personList.append(personID)
        personImageList=[]
        while(True):
            ret, frame = cap.read()
            frame_count+=1
            cv2.imshow('unknown',frame)
            if frame_count%10==0:
                personImageList.append(self.ImgUrl+'data\\images\\'+personID+str(int(frame_count/10))+'.jpg')
                cv2.imwrite(self.ImgUrl + 'data\\images\\' +personID + str(int(frame_count/10))+'.jpg',frame)
            if cv2.waitKey(20)&0xFF == 13:
                break
        cap.release()
        cv2.destroyAllWindows()
        return personList,personImageList


    def createPerson(self,personGroupId,personID,personImageList,name):
       myclient = pymongo.MongoClient("mongodb://localhost:27017/")
       mydb=myclient["employee"]
       mycol=mydb["person"]
        
       body=dict()
       body["name"]=personID
       body['userData']= "person1"
       body=str(body) 
       FaceApiCreatePerson = self.endpoint+personGroupId+'/persons'         
       
       headers = {
               'Content-Type': 'application/json',
               'Ocp-Apim-Subscription-Key': self.subscription_key
               }
       try:
           response = requests.post(FaceApiCreatePerson, data=body, headers=headers) 
           print(response)
           responseJson = response.json()
           print(responseJson)
           apipersonId = responseJson["personId"]
           print("PERSONID: "+str(apipersonId))
           personDict={"name":name,"personId":str(apipersonId)}
           mycol.update({"name":name},personDict)
         
       except Exception as e:
           print(e)
           
       FaceApiCreatePerson = self.endpoint+personGroupId+'/persons/'+apipersonId+'/persistedFaces' 

       for image in personImageList:
            body = dict()
            body["url"] = image
            body = str(body)
            data=open(image,'rb')
    
            headers = {
                        'Content-Type': 'application/octet-stream',
                        'Ocp-Apim-Subscription-Key': self.subscription_key
                        }  
            try:
                response = requests.post(FaceApiCreatePerson, data=data, headers=headers) 
                responseJson = response.json()
                persistedFaceId = responseJson["persistedFaceId"]
                print("PERSISTED FACE ID: "+str(persistedFaceId))
    
            except Exception as e:
                print(e)
                print('에러에러')