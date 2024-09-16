from flask import Flask, render_template, request, jsonify 
from PIL import Image  # for image processing
import numpy as np # for numerical operations and arrays for pixels of images
import tensorflow as tf # this a macine learning library 


app = Flask(__name__)

#load the file
model = tf.keras.models.load_model('model.h5')

#size of the image
target_size = (224, 224) 

#function to preprocess the image
def preprocess_image(image_path):
    img=Image.open(image_path)
    #resize the image
    img = img.resize(target_size)
    #convert the image to array
    img_array = np.array(img)
    #normalize the image
    img_array = img_array / 255.0
    #expand the dimensions
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

@app.route("/")
def page():
    return render_template('index.html')

#route to handle the image upload 
@app.route("/upload", methods=["POST"])
def upload():


    if 'file' not in request.files:
        return jsonify({
            "error" : "No file "
        })

    #get the file
    file = request.files['file']

    if file.filename == " " :
        return jsonify({
            "error" : "No Selected file"
        })

    try:
        #preprocess the image
        img_array= preprocess_image(file)

        #predict the image
        prediction = model.predict(img_array)
        class_index= np.argmax(prediction[0])

        if class_index == 0:
            result = "Cat"
        else:
            result = "Dog"

        return jsonify ({
            "result" : result
        })


    except IOError as e:
        return jsonify ({
            "error" : str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
