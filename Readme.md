{\rtf1\ansi\ansicpg1252\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;\f1\fnil\fcharset0 HelveticaNeue-Bold;\f2\froman\fcharset0 Times-Roman;
}
{\colortbl;\red255\green255\blue255;\red27\green31\blue34;\red10\green77\blue204;\red0\green0\blue0;
}
{\*\expandedcolortbl;;\cssrgb\c14118\c16078\c18039;\cssrgb\c1176\c40000\c83922;\cssrgb\c0\c0\c0;
}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f0\fs32 \cf2 \expnd0\expndtw0\kerning0
This project is about the development of smoke detection algorithms in case of forest fires.\
Our main problem statement is applying classification and object detection\'a0to identify smoke / fire through images\
I am using Mask RCNN model for object detection in this case.\
\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b \cf2 Step 1: Data gathering and collection:
\f0\b0 \
We have gathered data available online at below location.\
\pard\pardeftab720\sl360\sa320\partightenfactor0
{\field{\*\fldinst{HYPERLINK "https://sintecsys-omdena.s3.amazonaws.com/images3.zip"}}{\fldrslt \cf3 https://sintecsys-omdena.s3.amazonaws.com/images3.zip}}\
Dataset have almost 16.5K images (~8k masked and ~8k original images).\uc0\u8232 \
\
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b \cf2 Step 2: Exploration of data:
\f0\b0 \
Masked images have been already created. The model needs to be trained on existing masked images and start predicting.\
Size of images is: 1920 X 1080\
\uc0\u8232 \

\f1\b Step 3: Applying Image recognition and Object detection models.
\f0\b0 \

\f1\b \
Iteration 1:  S
\f0\b0 imple image recognition model and tried to train with simple CNN model\
\pard\pardeftab720\sl280\sa240\partightenfactor0

\f2\fs24 \cf4 \
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b\fs32 \cf2 Iteration 2: Alexnet\'a0model for classification
\f0\b0 \
\

\f1\b Iteration 2: Alexnet\'a0model for classification
\f0\b0 \
\pard\pardeftab720\sl280\sa240\partightenfactor0

\f2\fs24 \cf4 \
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f1\b\fs32 \cf2 Iteration 3: Mask RCNN\'a0model\
\
Result of the model has been deployed in the basic front end, where you can upload images and it will tell you if there is fire or not.
\f0\b0 \
}