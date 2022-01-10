import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from os import listdir
from os.path import isfile, join

def predictor2(location):
    test_image=image.load_img(location,target_size=(128,128))
    test_image=image.img_to_array(test_image)
    test_image=np.expand_dims(test_image, axis=0)
    result=model.predict(test_image)
    #training_set.class_indices
    if result[0][0] == 1:
        return False
    else:
        return True

model = load_model('models/model-crop.h5')

model.summary()


crackImages = [f for f in listdir(f"{os.getcwd()}/Examples/crack") if isfile(join(f"{os.getcwd()}/Examples/crack", f))]
noncrackImages = [f for f in listdir(f"{os.getcwd()}/Examples/non-crack") if isfile(join(f"{os.getcwd()}/Examples/non-crack", f))]

c  = 0
nc = 0

for i in crackImages:
    if predictor2(f"{os.getcwd()}/Examples/crack/{i}"):
        c += 1
        print(f"crack/{i}: ", end="")
        print("Crack detected!")

for i in noncrackImages:
    if predictor2(f"{os.getcwd()}/Examples/non-crack/{i}"):
        nc += 1
        print(f"non-crack/{i}: ", end="")
        print("Crack detected!")

print("Results: ")
print(f"{c}/{len(crackImages)} ({c/len(crackImages)*100:.2f}%) Detected in crack folder.")
print(f"{nc}/{len(noncrackImages)} ({nc/len(noncrackImages)*100:.2f}%) Detected in non-crack folder.")