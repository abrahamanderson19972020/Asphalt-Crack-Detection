import os
import cv2
import numpy as np
from datetime import date, datetime
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from os import listdir
from os.path import isfile, join

def get_jetson_gstreamer_source(capture_width=1280, capture_height=720, display_width=1280, display_height=720, framerate=2, flip_method=0):
    """
    Return an OpenCV-compatible video source description that uses gstreamer to capture video from the camera on a Jetson Nano
    """
    return (
            f'nvarguscamerasrc ! video/x-raw(memory:NVMM), ' +
            f'width=(int){capture_width}, height=(int){capture_height}, ' +
            f'format=(string)NV12, framerate=(fraction){framerate}/1 ! ' +
            f'nvvidconv flip-method={flip_method} ! ' +
            f'video/x-raw, width=(int){display_width}, height=(int){display_height}, format=(string)BGRx ! ' +
            'videoconvert ! video/x-raw, format=(string)BGR ! appsink'
            )

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

video_capture = cv2.VideoCapture(get_jetson_gstreamer_source(), cv2.CAP_GSTREAMER)


print("Analyzing camera feed...")
while(video_capture.isOpened()):
    
    ret, frame = video_capture.read()

    if (not ret):
            break

    # crop = frame[800:1000, 600:1920-600]
    
    if (predictor3(frame) == 1):
        dt = datetime.now()
        dtString = dt_string = dt.strftime("%d-%m-%Y_%H-%M-%S")
        print(f"Crack detected! Saved as: {dtString}_crack.jpg")
        cv2.imwrite(f"{os.getcwd()}/Examples/out/{dtString}_crack.jpg", frame)


video_capture.release()