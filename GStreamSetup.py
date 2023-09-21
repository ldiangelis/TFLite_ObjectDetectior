# update and upgrade
sudo apt update && sudo apt full-upgrade -y
sudo reboot

# compile OpenCV with GStreamer 

git clone https://github.com/ldiangelis/TFLite_ObjectDetection.git
cd TFLite_ObjectDetection
sudo chmod +x OpenCV-4-8-0-Compile.sh
./OpenCV-4-8-0-Compile.sh
sudo reboot

# clone the TFLite examples repo
git clone https://github.com/tensorflow/examples
cd examples/lite/examples/object_detection/raspberry_pi

# create (optional) symlink
cd
ln -s ~/examples/lite/examples/object_detection/raspberry_pi ~/PiDectector

# edit the requirements file w/ these versions 
nano requirements.txt
tflite-support==0.4.3

# run the setup script
sudo chmod +x setup.sh
./setup.sh

# edit the config file
sudo nano /boot/config.txt
arm_freq=1900
over_voltage=6
dtoverlay=vc4-kms-v3d,cma-512
	
# save changes and reboot
sudo reboot

# copy the GStreamer Detection Script from the TFLite_ObjectDetection Dir to the PiDectector Dir
cd ~/PiDetector
cp  ~/TFLite_ObjectDetection/GStreamerDetect.py .

# replace the utils.py script with the GStreamer Utils Script from the TFLite_ObjectDetection Dir to the PiDectector Dir
mv ~/TFLite_ObjectDetection/GStreamerUtils.py ./utils.py
