# Crack-Detector
Project in IKT213-G21H Machine Vision to automatically detect cracks in roads.


Run `trainer.py` to train a model on images in `/tools/out` and `/tools/test`. Images not included.

View `modle_trainer.ipynb` to get a more detailed view of how we trained our models.

Run `tester.py` to preform a quick test of the model on a few example images in `/Examples/`.

Run `analyzeVideo.py` to analyze a video file and save every detected crack into `/Examples/out/`.

Run `analyzeCamera.py` to analyze video stream from a the Jetson Nano camera and save every detected crack into `/Examples/out/`.


To create image sets from videos quickly use `videoToImages.py` in `/tools/`. It takes two parameters  `<input-video> <output-folder>`.