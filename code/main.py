from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import requests
import os
from keras.models import load_model
import numpy as np
from PIL import Image, ImageOps
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('base.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
    
        model = load_model('static/model/keras_model(1).h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        # Replace this with the path to your image
        image = Image.open('static/uploads/'+file.filename)
        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)
        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        # Load the image into the array
        data[0] = normalized_image_array
        labels = ['Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust',
'Apple___healthy','Cherry_(including_sour)___healthy','Cherry_(including_sour)___Powdery_mildew',
'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_','Corn_(maize)___healthy',
'Corn_(maize)___Northern_Leaf_Blight','Grape___Black_rot','Grape___Esca_(Black_Measles)',
'Grape___healthy','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Orange___Haunglongbing_(Citrus_greening)'
,'Peach___Bacterial_spot','Peach___healthy','Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy'
,'Potato___Early_blight','Potato___healthy',
'Potato___Late_blight','Squash___Powdery_mildew'
,'Strawberry___healthy','Strawberry___Leaf_scorch','Tomato___Bacterial_spot','Tomato___Early_blight'
,'Tomato___healthy','Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot'
,'Tomato___Spider_mites Two-spotted_spider_mite','Tomato___Target_Spot','Tomato___Tomato_mosaic_virus'
,'Tomato___Tomato_Yellow_Leaf_Curl_Virus']
        # run the inference
        prediction = model.predict(data)
        v=prediction.argmax(axis=1)[0]
        url="http://vivekpzr.pythonanywhere.com/"
        r=requests.get(url).json()
        data={
            'nam':r['data'][v]['name'],
            'dis':r['data'][v]['discription'],
            'rem':r['data'][v]['remedy']
        }
    
        
        return render_template('index.html', filename=filename,data=data)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run()