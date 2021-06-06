from flask import Flask, render_template, request
import jsonify
import requests
import joblib
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = joblib.load('estate.pkl')

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        house_age=float(request.form['house_age'])
        market_distance=float(request.form['market_distance'])
        no_of_conveniance_store=float(request.form['no_of_conveniance_store'])
        lat=float(request.form['lat'])
        long=float(request.form['long'])
        prediction=model.predict([[house_age,market_distance,no_of_conveniance_store,lat,long]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Not Valid")
        else:
            return render_template('index.html',prediction_text="price =  {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

