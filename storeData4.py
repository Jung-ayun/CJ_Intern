# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:49:22 2019

@author: setgo
"""


import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import cv2
import pymongo

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
        
 #   def savePersonImage(self,name,famousList):
 #       cap =cv2.VideoCapture(0)
 #       frame_count = 0
 #       famousList.append(name)
 #       while(True):
 #           ret, frame = cap.read()
 #           frame_count+=1
 #           cv2.imshow('unknown',frame)
 #           if frame_count%5==0:
 #               cv2.imwrite(name+str(frame_count)+'.jpg',frame)
 #           if cv2.waitKey(20)&0xFF == ord('q'):
 #               break
 #       cap.release()
 #       cv2.destroyAllWindows()
 #       return famousList


    def createPerson(self,personGroupId):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb=myclient["employee"]
        mycol=mydb["person"]

        famousList=['han','son','you','ryu','jay','yoon','yyy','lee']
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
               personDict={"name":i,"personId":str(personId)}
               x=mycol.insert_one(personDict)
               print(x)
    
            except Exception as e:
                print(e)
    
            personImageList=[]
        
            for j in range(1,2):
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