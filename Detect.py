import numpy as np
import cv2
Custome_Object = cv2.CascadeClassifier('banana_haar_cascade.xml')
cap = cv2.VideoCapture(0)
if (cap.isOpened()== False): 
  print("Error opening Camera")


while (cap.isOpened()):
    ret,Img = cap.read()
    gray = cv2.cvtColor(Img, cv2.COLOR_BGR2GRAY)
    
    detected = Custome_Object.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in detected:
        cv2.rectangle(Img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Get Image For User",Img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()
    
