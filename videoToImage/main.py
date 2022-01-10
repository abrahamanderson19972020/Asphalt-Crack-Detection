import cv2
import os

# Read the video from specified path
KPS = 1# Target Keyframes Per Second
cam = cv2.VideoCapture("C:/Users/Bruker/crack/project_group11/videos/10.mp4")
fps = round(cam.get(cv2.CAP_PROP_FPS))
hop = round(fps / KPS)
try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        if currentframe % hop == 0:
        # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

        # writing the extracted images
            cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
