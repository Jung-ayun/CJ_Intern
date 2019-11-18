# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:55:01 2019

@author: Administrator
"""


import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests

subscription_key = "80d68f1211af4c5aa5dac482757a9488"
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    "name": "group1",
    "userData": "user-provided data attached to the person group.",
    "recognitionModel": "recognition_02"
})


#try:
#    conn = http.client.HTTPSConnection('koreacentral.api.cognitive.microsoft.com')
#    conn.request("PUT", "/face/v1.0/persongroups/{personGroupId}?%s" % params, "{body}", headers)
#    response = conn.getresponse()
#    data = response.read()
#    print(data)  ###에러
#    conn.close()
#except Exception as e:
#    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
###create persongroup
    
personGroupId="friends"
body = dict()
body["name"] = "F.R.I.E.N.D.S"
body["userData"] = "All friends cast"
body["recognitionModel"] = "recognition_02"
body = str(body)

#Request URL 
FaceApiCreateLargePersonGroup = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId 

try:
    # REST Call 
    response = requests.put(FaceApiCreateLargePersonGroup, data=body, headers=headers) 
    print(response)
    print("RESPONSE:" + str(response.status_code)) ##에러 404

except Exception as e:
    print(e)
    
#Request Body
body = dict()
body["name"] = "Chandler"
body["userData"] = "Friends"
body = str(body)

#Request URL 
FaceApiCreatePerson = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons' 

try:
    # REST Call 
    response = requests.post(FaceApiCreatePerson, data=body, headers=headers) 
    responseJson = response.json()
    personId = responseJson["personId"]
    print("PERSONID: "+str(personId))
    
except Exception as e:
    print(e)


chandlerImageList = ["http://www.imagozone.com/var/albums/vedete/Matthew%20Perry/Matthew%20Perry.jpg?m=1355670659",
                     "https://i.pinimg.com/236x/b0/57/ff/b057ff0d16bd5205e4d3142e10f03394--muriel-matthew-perry.jpg",
                     "https://qph.fs.quoracdn.net/main-qimg-74677a162a39c79d6a9aa2b11cc195b1",
                     "https://pbs.twimg.com/profile_images/2991381736/e2160154f215a325b0fc73f866039311_400x400.jpeg",
                     "https://i.pinimg.com/236x/f2/9f/45/f29f45049768ddf5c5d75ff37ffbfb3f--hottest-actors-matthew-perry.jpg"]

#Request URL 
FaceApiCreatePerson = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/persons/'+personId+'/persistedFaces' 

for image in chandlerImageList:
    body = dict()
    body["url"] = image
    body = str(body)

    try:
        # REST Call 
        response = requests.post(FaceApiCreatePerson, data=body, headers=headers) 
        responseJson = response.json()
        persistedFaceId = responseJson["persistedFaceId"]
        print("PERSISTED FACE ID: "+str(persistedFaceId))
    
    except Exception as e:
        print(e)
        
######train 
#Request Body
body = dict()

#Request URL 
FaceApiTrain = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/persongroups/'+personGroupId+'/train'

try:
    # REST Call 
    response = requests.post(FaceApiTrain, data=body, headers=headers) 
    print("RESPONSE:" + str(response.status_code))

except Exception as e:
    print(e)


###face detect 
# Request Body
body = dict()
#body["url"] = "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Matthew_Perry_as_Chandler_Bing.jpg/220px-Matthew_Perry_as_Chandler_Bing.jpg"
body['url']= 'https://i.pinimg.com/236x/f2/9f/45/f29f45049768ddf5c5d75ff37ffbfb3f--hottest-actors-matthew-perry.jpg'
body = str(body)
print(body)
# Request URL 
FaceApiDetect = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId=true' 

try:
    # REST Call 
    response = requests.post(FaceApiDetect, data=body, headers=headers) 
    print(response)
    responseJson = response.json()
    print(responseJson)
    faceId = responseJson[0]["faceId"] #결과값 0
    print("FACE ID: "+str(faceId))

except Exception as e:
    print(e)
    
##face identify


faceIdsList = [faceId]
print(faceIdsList)
# Request Body
body = dict()
body["personGroupId"] = personGroupId
body["faceIds"] = faceIdsList
body["maxNumOfCandidatesReturned"] = 1 
body["confidenceThreshold"] = 0.5
body = str(body)

# Request URL 
FaceApiIdentify = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/identify' 

try:
    # REST Call  ####에러
    response = requests.put(FaceApiIdentify, data=body, headers=headers) 
    print(response) ###404
    responseJson = response.json()
    print(responseJson)
    personId = responseJson[0]["candidates"][0]["personId"]
    confidence = responseJson[0]["candidates"][0]["confidence"]
    print("PERSON ID: "+str(personId)+ ", CONFIDENCE :"+str(confidence))
        
except Exception as e:
    print("Could not detect")
    