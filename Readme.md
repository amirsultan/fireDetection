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

Step 4: Demonstration of Mask RCNN model

a. Overview of Mask RCNN:
![alt text](https://i.ibb.co/YNr6ybj/Screen-Shot-2020-05-05-at-12-41-48-AM.png)

b. Training and Validation Loss:
![alt text](https://i.ibb.co/SBqsddh/Screen-Shot-2020-05-05-at-12-42-14-AM.png)

c. Precision and Recall numbers:
![alt text](https://i.ibb.co/ts34QXm/Screen-Shot-2020-05-05-at-12-42-29-AM.png)

d. Result and comparison with Unet Masks:
![alt text](https://i.ibb.co/093jX9V/Screen-Shot-2020-05-05-at-12-42-55-AM.png)


Step 5: Demonstation using Flask and HTML / Javascript UI:
![alt text](https://i.ibb.co/VDXNhgN/Screen-Shot-2020-04-28-at-4-13-10-AM.png)
![alt text](https://i.ibb.co/n0vRYGZ/Screen-Shot-2020-04-28-at-4-13-20-AM.png)

Step 6:
Generating Alerts: Generating alerts through emails
![alt text](https://i.ibb.co/f8C2Fts/Screen-Shot-2020-04-28-at-4-13-33-AM.png)

https://ibb.co/hgqkZC8
https://ibb.co/GRgxttK
https://ibb.co/k8Mx51H
https://ibb.co/R6WpS64

Result of the model has been deployed in the basic front end, where you can upload images and it will tell you if there is fire or not.
