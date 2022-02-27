import cv2
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
import requests

font = cv2.FONT_HERSHEY_SIMPLEX

model = tf.keras.models.load_model('./Saved Model and Cascading/driver_drowsiness.h5')
frontalface_haar_cascade = cv2.CascadeClassifier('./Saved Model and Cascading/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./Saved Model and Cascading/haarcascade_eye.xml')
label_dict = {0 : 'Close Eyes', 1: 'Open Eyes'}

camera = cv2.VideoCapture('video 2.mp4')
fcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter('output.avi', fcc, 20.0, (640, 480)) 

while True:
    success, frame = camera.read()
    if success:
        face = frontalface_haar_cascade.detectMultiScale(frame, scaleFactor= 1.2, minNeighbors=3)
        for (x,y,w,h) in face:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (225,255,225), 2)
            face_img = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(face_img, scaleFactor= 1.2, minNeighbors=3)
            for (ex,ey,ew,eh) in eyes:
                eye_img = face_img[ey:ey+eh, ex:ex+ew]
                resize_image = cv2.resize(eye_img, (80,80))
                normalize_img = resize_image/225
                img_pixels = normalize_img.reshape(80,80,3)
                img_pixels = np.expand_dims(img_pixels, axis=0)

                predictions = model.predict(img_pixels)
                final_label = np.argmax(predictions)

                if final_label == 0:
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,225),2)
                    cv2.putText(frame,'Driver Drowsiness', (x, y), font, 0.5,(0,0,225), 1)
                
                else:
                    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,225,0),2)
                    cv2.putText(frame,'Awake', (x, y), font, 0.5,(0,225,0), 1)
                
                cv2.imshow('Video', frame)
                result.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        result.release() 
        break

cv2.destroyAllWindows()
result.write(frame)