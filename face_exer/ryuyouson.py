# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 12:41:20 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:16:41 2019

@author: setgo
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import cv2

subscription_key = "80d68f1211af4c5aa5dac482757a9488"
headers = {
    # Request headers
    'Content-Type': 'application/json',
    #'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
}

params = urllib.parse.urlencode({
    "name": "group1",
    "userData": "user-provided data attached to the person group.",
    "recognitionModel": "recognition_02"

})
####################################
###create persongroup##############
    
personGroupId="famous26"
body = dict()
body["name"] = "F.A.M.O.U.S"
body["userData"] = "All famous cast"
#body["recognitionModel"] = "recognition_02"
body = str(body)

#Request URL 
FaceApiCreateLargePersonGroup = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId 

try:
    # REST Call 
    response = requests.put(FaceApiCreateLargePersonGroup, data=body, headers=headers) 
    print("RESPONSE:" + str(response.status_code)) 

except Exception as e:
    print(e)
    
    

    
#Request Body
##############persongroup만들기###########
famousList=['son','ryu','you']
for i in famousList:
    body=dict()
    body["name"]=i
    body['userData']='famous'
    body=str(body)
    
    #Request URL 
    FaceApiCreatePerson = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons' 

    headers = {
    # Request headers
    'Content-Type': 'application/json',
    #'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
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
         personImageList.append('C:\\Users\\Administrator\\Desktop\\cj_intern\\'+i+'\\'+i[0]+str(j)+'.jpg')
         headers = {
                 # Request headers
                 #'Content-Type': 'application/json',
                 'Content-Type': 'application/octet-stream',
                 'Ocp-Apim-Subscription-Key': subscription_key
                 }  

    #Request URL 
    FaceApiCreatePerson = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId+'/persistedFaces' 

    for image in personImageList:
        body = dict()
        print(image)
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


######train 
#Request Body
body = dict()

#Request URL 
FaceApiTrain = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/train'
headers = {
    # Request headers
    'Content-Type': 'application/json',
    #'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
}
try:
    # REST Call 
    response = requests.post(FaceApiTrain, data=body, headers=headers) 
    print("RESPONSE:" + str(response.status_code))

except Exception as e:
    print(e)


###face detect 
# Request Body
body = dict()
body["url"]= 'C:\\Users\\Administrator\\Desktop\\cj_intern\\you\\y1.jpg'
img_bgr= cv2.imread(body['url'],cv2.IMREAD_COLOR)


data=open(body['url'],'rb')
# Request URL 
FaceApiDetect = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true' 
headers = {
    # Request headers
    #'Content-Type': 'application/json',
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key
}


try:
    # REST Call 
    response = requests.post(FaceApiDetect, data=data, headers=headers) 
    print(response)
    responseJson = response.json()
    print(responseJson)
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
    
######face identify
faceIdsList = [faceId]
faceIdsList.append(faceId)
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
    'Ocp-Apim-Subscription-Key': subscription_key
}
try:
    # REST Call 
    response = requests.post(FaceApiIdentify, data=body, headers=headers) 
    responseJson = response.json()
    
    print(responseJson)
    personId = responseJson[0]["candidates"][0]["personId"]
    confidence = responseJson[0]["candidates"][0]["confidence"]
    print("PERSON ID: "+str(personId)+ ", CONFIDENCE :"+str(confidence))
    
except Exception as e:
    print("Could not detect")

FaceApiGetPerson = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId

try:
    response = requests.get(FaceApiGetPerson, headers=headers) 
    responseJson = response.json()
    print("This Is "+str(responseJson["name"]))
    cv2.putText(img_bgr,str(responseJson["name"]),(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.rectangle(img_bgr,(left,top),(bottom,right),(255,0,0),1)
    cv2.imshow('1',img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except Exception as e:
    print(e)