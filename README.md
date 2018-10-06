# Make-Your-Own-Object-Detector
# Introduction
  The OpenCV library provides us a greatly interesting demonstration for a face detection. <br>
  Furthermore, it provides us programs (or functions) that they used to train classifiers for their face detection system, <br>
  called HaarTraining, so that we can create our own object classifiers using these functions.<br>
  
  Use the CascadeClassifier class to detect objects in a video stream. <br>
 
 # instructions
 There are many steps to create your own classifier. <br>
  * First : - we need a sample that divided into two parts. <br>
    - Positive Image (the object you want to detect) like <br>
    
    
      ![pos1](https://user-images.githubusercontent.com/28443900/46442315-86b06200-c769-11e8-8b31-b6b4494d232c.jpg)<br>
            
    - Negative Image (images without your object) like <br>
            ![neg-0002](https://user-images.githubusercontent.com/28443900/46442496-1bb35b00-c76a-11e8-8202-078d2faf8574.jpg)<br>
            and can download more from [here](https://github.com/JoakimSoderberg/haarcascade-negatives)<br>
      
  * Second :- Creating Samples of positive and negative images and choose all parameters to complete it like <br>
    - bgcolor , bgthresh , maxxangle , maxyangle , maxzangle , maxidev , width , height.<br>
  
  * Third :- Training the classifier with positive & negative images after take your sample from last step with specific parameters. <br>
    - numStages , minHitRate , maxFalseAlarmRate , numPos , numNeg , mode , precalcValBufSize , precalcIdxBufSize , w, h.<br>
 
 # Requirement
   Install Python 2.7 from [here](https://www.python.org/download/releases/2.7/) <br>
   Install OpenCV from [here](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/) <br>
   Install Numpy from [here](https://pypi.org/project/numpy/) <br>
   
 # Tools
   * This is a powerfull tool for Train Your Own OpenCV Haar Classifier. <br>
     it's a GUI tools for windows (32 & 64) bit and all details in this [link](http://amin-ahmadi.com/cascade-trainer-gui/) <br>
     
   * if you like linux you can follow [this](https://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html)<br>
   
   
   
  
