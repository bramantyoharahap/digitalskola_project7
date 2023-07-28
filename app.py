from flask import Flask
from flask import request
from flask import jsonify
import pandas as pd

from modules.insurance_predict import InsurancePredict

import json

app = Flask(__name__)

@app.route("/")
def home():
    return "API ML Modelin"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    data_length = len(df.index)
    typed = 'single'

    if data_length > 1:
        typed = 'multi'
    elif data_length < 1:
        return jsonify({
            "status": "predicted",
            "predict_code": predict_code,
            "result": predict_result,
            "data": data
        })
    
    predict_code = InsurancePredict.runModel(df,typed=typed)
    
    predict_result = 'interested' if predict_code == 1 else 'not interested'

    return jsonify({
        "status": "predicted",
        "predict_code": predict_code,
        "result": predict_result,
        "data": data
    })
