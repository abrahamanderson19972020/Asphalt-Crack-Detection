import cv2
import os
import numpy as np
from datetime import timedelta
from tensorflow.keras.models import load_model

def predictor3(img):
    test_image = cv2.resize(img, (64,64))
    test_image = np.expand_dims(test_image, axis=0)
    result=model.predict(test_image)
    #training_set.class_indices
    if result[0][0] == 1:
        return False
    else:
        return True

model = load_model('models/model2.h5')

model.summary()

if (not os.path.exists(f"{os.getcwd()}/Examples/out")):
    os.mkdir(f"{os.getcwd()}/Examples/out")

cap = cv2.VideoCapture(f"{os.getcwd()}/Examples/video-3.webm")

fps = cap.get(cv2.CAP_PROP_FPS)
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frameCount/fps

frameNumber = 0


while(cap.isOpened()):
    
    ret, frame = cap.read()

    if (not ret):
        break

    crop = frame[800:1000, 600:1920-600]

    if (predictor3(crop) == 1):
        time = str(timedelta(seconds=(frameNumber/fps)))
        td = time.split(':')
        print(f"Crack at {td[1]}:{td[2]}")
        cv2.imwrite(f"{os.getcwd()}/Examples/out/{td[1]}-{td[2]}_crack.jpg", crop)
    
    frameNumber += 1


cap.release()