import os
import sys
from datetime import datetime
import base64

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)


# You can use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.mobilenet_v2 import MobileNetV2
#model = MobileNetV2(weights='imagenet')

print('Model loaded. Check http://127.0.0.1:5000/')


# Model saved with Keras model.save()
MODEL_PATH = 'models/unet_and_512weights.h5'
#MODEL_PATH = 'models/model1.h5'
# Load your own trained model
model = load_model(MODEL_PATH)

model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')
print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img, model):
    img = img.resize((512, 512))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Make prediction
        ##preds = model_predict(img, model)
        pred_proba = model_predict(img, model)

        pred_class = np.argmax(pred_proba)
        # Process your result for human
        ##pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_proba = "{:.3f}".format(np.argmax(pred_proba)) 
        
        if pred_class < 0.9:
            result = 'No_fire'
        elif pred_class >= 0.9:
            result = 'Fire'
            sendEmail()
            
        #Make threshold basis results coming along

        result = result.replace('_', ' ').capitalize()

        #sendEmail()

        # Process your result for human
        ##pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        ##pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        ##result = str(pred_class[0][0][1])               # Convert to string
        ##result = result.replace('_', ' ').capitalize()
        
        # Serialize the result, you can add additional fields


        this_image = f"./images/{datetime.now().timestamp()}.png"
        
        ################# ACTION: SAVE YOUR MASKED IMAGE HERE ##################
        #Watever function you have change the `img.save`
        img.save(this_image)
        ################# ACTION END ##################
        
        image_file = open(this_image, "rb")
        image = base64.b64encode(image_file.read())
        image_string = str(image)[2:-1] #converting it into string and removing the 'b' and the quotes from the start and end

        return jsonify(result=result, probability=pred_proba, image=image_string)

    return None

def sendEmail():

    yag = yagmail.SMTP('aifiredetectionsystem@gmail.com', 'password')

    # Alternatively, with a simple one-liner:

    yagmail.SMTP('aifiredetectionsystem').send('am****@gmail.com', 'Fire Detected', 'Fire Detected')

    
if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
