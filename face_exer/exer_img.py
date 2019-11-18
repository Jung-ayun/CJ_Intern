import cv2

body=dict()
body["url"]= 'C:\\Users\\Administrator\\Desktop\\cj_intern\\you\\y1.jpg'
img= cv2.imread(body['url'],cv2.IMREAD_COLOR)
cv2.putText(img,"name",(0,0),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,255),2)
cv2.imshow('4',img)
cv2.waitKey(0)
cv2.destroyAllWindows()