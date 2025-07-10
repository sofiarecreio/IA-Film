# app/api.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('app/model.pkl')
labels = joblib.load('app/labels.pkl')

@app.route('/recomendar', methods=['POST'])
def recomendar():
    data = request.json
    x_input = np.array([[data['criatividade'], data['extroversao'], data['racionalidade']]])
    prediction = model.predict(x_input)[0]
    genero = labels[prediction]
    return jsonify({'genero_recomendado': genero})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
