from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('dia.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
	if request.method == 'POST':
		Pregnancies = int(request.form['pregnancies'])
		Glucose = float(request.form['glucose'])
		BloodPressure = float(request.form['blood_pressure'])
		SkinThickness = float(request.form['skin_thickness'])
		Insulin = float(request.form['ensulin'])
		BMI = float(request.form['BMI'])
		DiabetesPedigreeFunction = float(request.form['DPF'])
		Age = float(request.form['age'])

		prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
		if prediction == 1:
			return render_template('positive.html')
		else:
			return render_template('negative.html' )
	else:
		return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
