# Haar Cascade Model
A project for real-time object detection (stop sign detection) using Haar Cascade classifiers with OpenCV. This repository includes the trained cascade XML model, example of negative + positive image paths, a positive image training vector file, a Python script to format negative image paths, and Python script for detection with a webcam.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- OpenCV provided tools/exe's (opencv_annotation.exe, opencv_traincascade.exe, etc.)
- Webcam
- Optional: Raspberry Pi, thumb drive

## Training the Model
- Utilize Google's Open Images Dataset + Tool Kit (OIDv4_ToolKit).
- Download around 1000 positive images and 600 negative images (choose a large positive dataset to detect).
- Run negformat.py to generate a customized neg.txt
- Download opencv.exe from sourceforge.net/projects/opencvlibrary/files/3.4.11
- Utilize the annotation tool with this command.
    C:/Users/.../.../opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/
- Generate positive samples from the annotation + pos.vec with this command.
    C:/Users/.../.../opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
- Train your model using this command.
    C:/Users/.../.../opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24
- Play with these numbers to get the best results for your model (don't increase numStages too much, that can lead to overtraining). Also play with other arguments like precalcValBufSize, precalcIdxBufSize, maxFalseAlarmRate, and minHitRate.

## Raspberry Pi Integration
- Upload vision.py and cascade.xml onto the thumb drive.
- Connect your Raspberry Pi to power, use an HDMI cable to connect to a monitor, connect a webcam, connect to a mouse + keyboard, and connect the thumb drive.
- Then use terminal commands to make sure opencv is downloaded and the webcam works.
- Use "python3 video.py" to run the script.
