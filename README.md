TFLite Object Detection on Raspberry Pi

This repository contains scripts to run TFLite object detection on a Raspberry Pi using the libcamera stack and GStreamer with OpenCV.

I. Background:

This work is an extension of the Khanhlvg implementation, updating the OS from Raspbian Buster 32-bit to Raspberry Pi OS 64-bit 
as well as updating from the legacy to libcamera stack (Khanhlvg(1), 2023).

II. Usage:

1. Set up the environment as detailed in GStreamSetup.py

2. Customize the detector appearance

3. Run the object detector

III. Customizations:

Customize text or bounding boxes (color, size, width, etc) by editing the GStreamerDetect.py and GStreamerUtils.py scripts.
There are several modifications to these scripts compared to the original TFLite examples repo scripts for reference.

IV. Run the script:

1. Optional Arguments

    --model: Set the object detection model (defaults to efficientdet_lite0.tflite).
    --frameWidth: Set the frame width (defaults to 640).
    --frameHeight: Set the frame height (defaults to 480).

2. Run the default script

python3 GStreamerDetect.py

3. Run script with optional arguments

python3 GStreamerDetect.py \ </br>
--model <model.tflite> \ </br>
--frameWidth <width> \ </br>
--frameHeight <height>

V. Results:

640x480: ~11.8 FPS </br>
480x360: ~12.3 FPS </br>
Full Screen: ~8.1 FPS </br>
X11 Forwarding from RPi: ~11.3 FPS

The results demonstrate > 300% increase in FPS from the reference project (Khanhlvg(1), 2023) by implementing the 64-bit OS, upgrading 
to libcamera stack, and compiling OpenCV w/ Gstreamer support!

References

    Khanhlvg(1) (2023). Setup RPi for TFLite
    Qengineering(1) (2023). Install OpenCV on Raspberry 64 OS
    Qengineering(2) (2023). Install GStreamer 1.18 on Raspberry Pi 4
    Raspberry Pi(1) (2023). The config.txt file
