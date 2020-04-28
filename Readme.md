This project is about the development of smoke detection algorithms in case of forest fires.
Our main problem statement is applying classification and object detection to identify smoke / fire through images
I am using Mask RCNN model for object detection in this case.

Step 1: Data gathering and collection:
We have gathered data available online at below location.
https://sintecsys-omdena.s3.amazonaws.com/images3.zip
Dataset have almost 16.5K images (~8k masked and ~8k original images). 

Step 2: Exploration of data:
Masked images have been already created. The model needs to be trained on existing masked images and start predicting.
Size of images is: 1920 X 1080
 
Step 3: Applying Image recognition and Object detection models.

Iteration 1:  Simple image recognition model and tried to train with simple CNN model

Iteration 2: Alexnet model for classification


Iteration 3: Mask RCNN model

![alt text](https://i.ibb.co/VDXNhgN/Screen-Shot-2020-04-28-at-4-13-10-AM.png)
![alt text](https://i.ibb.co/n0vRYGZ/Screen-Shot-2020-04-28-at-4-13-20-AM.png)

Step 4:
Generating Alerts: Generating alerts through emails
![alt text](https://i.ibb.co/f8C2Fts/Screen-Shot-2020-04-28-at-4-13-33-AM.png)



Result of the model has been deployed in the basic front end, where you can upload images and it will tell you if there is fire or not.
