# import platform
# import numpy as np
# import pymongo

# client = pymongo.MongoClient('mongodb://localhost:27017')
# print(client)
# db= client['python']
# col = db['first']
# col.insert_one({ 'name': 'Akshit', 'class': 9 })
# x = col.delete_many({})

# for i  in x:
#     print(i)

# arr = np.array(range(1000))
# print(arr)

'''
---Platform stuff---
print(platform.node())
print(platform.platform())
print(platform.machine())
print(platform.processor())

print(platform.python_branch())
print(platform.python_compiler())
print(platform.python_build())

print(platform.release())
print(platform.system())

print(platform.uname())

print(platform.architecture())
'''

import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # img = cv2.flip(img, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]  

    cv2.imshow('video',frame)

    if cv2.waitKey(30) & 0xff == ord('q'): # press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()