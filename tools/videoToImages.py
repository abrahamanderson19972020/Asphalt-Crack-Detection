import cv2
import sys
import os

def main(argv):
    cap = cv2.VideoCapture(argv[0])
    outFolder = argv[1]
    videoName, ext = os.path.splitext(argv[0])

    c  = 0
    nc = 0

    running = True

    if (not os.path.exists(outFolder)):
        os.mkdir(outFolder)
        os.mkdir(f"{outFolder}/crack")
        os.mkdir(f"{outFolder}/non-crack")
    else:
        if (not os.path.exists(f"{outFolder}/crack")):
            os.mkdir(f"{outFolder}/crack")

        if (not os.path.exists(f"{outFolder}/non-crack")):
            os.mkdir(f"{outFolder}/non-crack")

    defaultFrameSkips = 24
    frameSkips = defaultFrameSkips
    frameNumber = 0
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while (cap.isOpened() and running):
        # skip ahead, dont need to many frames
        cap.set(cv2.CAP_PROP_POS_FRAMES, frameNumber)
        ret, frame = cap.read()

        if (not ret):
            break

        crop = frame[800:1000, 600:1920-600]

        cv2.imshow("z: Non-crack, c: Crack", crop)

        key = cv2.waitKey(0)
        if (key == ord('q') or cv2.getWindowProperty("z: Non-crack, c: Crack", cv2.WND_PROP_VISIBLE) <1):
            running = False
            break
        elif (key == ord('z')):
            # Does not include crack
            nc += 1
            frameSkips = defaultFrameSkips
            cv2.imwrite(f"./{outFolder}/non-crack/{videoName}-{nc}.jpg", crop)

        elif (key == ord('c')):
            # Includes crack
            c += 1
            frameSkips = 1
            cv2.imwrite(f"./{outFolder}/crack/{videoName}-{c}.jpg", crop)
        else:
            frameSkips = defaultFrameSkips

        frameNumber += frameSkips

        if (frameNumber > frameCount):
            frameNumber = frameCount


    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    if (len(sys.argv) == 3):
        main(sys.argv[1:3])
    else:
        print("videoToImages.py <input-video> <output-folder>")