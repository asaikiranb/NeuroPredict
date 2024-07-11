from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask import redirect
import tensorflow as tf


from tensorflow.keras.preprocessing.image import  img_to_array
import numpy as np
from PIL import Image
import json


from sklearn.metrics import f1_score
def f1_score_metric(y_true, y_pred):
    # Implement the F1 score calculation here
    return f1_score(y_true, y_pred)

# Register the custom metric function
tf.keras.utils.get_custom_objects()['f1_score'] = f1_score_metric



def predict_mri(image, model):

    if image is None or image == '':
        return None    

    img = Image.open(image).convert('RGB')
  
    target_size = (224, 224)
    img = img.resize(target_size)
    input_array = img_to_array(img)
    input_array /= 255.0
    input_array = np.expand_dims(input_array, axis=0)

    predictions = model.predict(input_array)

    predictions_list = predictions.tolist()
    
    # class_labels = ['Class 1', 'Class 2', 'Class 3: NON-DEMENTED', 'Class 4']
    
    
    # predicted_label = class_labels[int(predictions.argmax(axis=1))]

    # response_data = {"prediction":predicted_label}

    # json_data = json.dumps(predictions_list)
    # print(json_data)
    
    return predictions_list

    






app = Flask(__name__)







# @app.route('/')
# def index_view():
#     return render_template('index.html')
@app.route('/')
def nuero():
    return render_template('neuro.html')



@app.route('/predict', methods =['POST','GET'])
def predict():

    model_cnn = tf.keras.models.load_model('model_01.h5')

    image = request.files['image']
    

    predicted_label = predict_mri(image, model_cnn)

    response_data = {'prediction' : predicted_label}
    return jsonify(response_data)


# @app.route('/result.html', methods=['POST', 'GET'])
# def result():
#     return render_template('result.html')



@app.route('/info.html', methods = ['GET','POST'])
def info():
    return render_template('info.html')


@app.route('/device-info', methods = ['GET','POST'])
def device_info():
    return render_template('device.html')


@app.route('/more-info', methods =['GET'])
def more_info():
    return render_template('extra.html')