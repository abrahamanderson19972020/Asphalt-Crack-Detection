import os
import session_info
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator


session_info.show()

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
training_set = train_datagen.flow_from_directory(
        f"{os.getcwd()}/tools/out",
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary')

test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
        f"{os.getcwd()}/tools/test",
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary')

print(training_set[2])


cnn = Sequential()

cnn.add(Conv2D(filters=32, kernel_size=3, activation="relu",input_shape=[128,128,3]))

cnn.add(MaxPool2D(pool_size=2, strides=2))

cnn.add(Conv2D(filters= 32, kernel_size=3, activation= "relu"))

cnn.add(MaxPool2D(pool_size=2, strides=2))

cnn.add(Flatten())

cnn.add(Dense(units=128,activation="relu"))

cnn.add(Dense(units=256,activation="relu"))

cnn.add(Dense(units=1,activation="sigmoid"))

cnn.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

cnn.summary()

history= cnn.fit(x=training_set,validation_data=test_set,epochs=20)

cnn.save("models/model-crop.h5")
print("Saved model to disk")