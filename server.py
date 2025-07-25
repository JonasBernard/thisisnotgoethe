from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)


# model=load_model('./model_mnist.h5')

# model.make_predict_function()

def predict(text):
    return "This is not generated by AI"

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
    input = ""
    output = ""
    if request.method == 'POST':
        input = request.form['inputField']
        output = predict(input)

    return render_template("index.html", input=input, output=output)


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)