from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('gym.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        day_of_week = request.form['day']
        if day_of_week == 'monday':
            day_of_week = 0
        elif day_of_week == 'tuesday':
            day_of_week = 1
        elif day_of_week == 'wednesday':
            day_of_week = 2
        elif day_of_week == 'thurshday':
            day_of_week = 3
        elif day_of_week == 'friday':
            day_of_week = 4
        elif day_of_week == 'saturday':
            day_of_week = 5
        elif day_of_week == 'sunday':
            day_of_week = 6

        is_weekend = request.form['weekend']
        if is_weekend == 'Yes':
            is_weekend = 1
        else:
            is_weekend = 0

        is_holiday = request.form['holiday']
        if is_holiday == 'Yes':
            is_holiday = 1
        else:
            is_holiday = 0

        tempeature = (float(request.form['temperature']) * 1.8) + 32

        is_start_of_semester = request.form['semester_start']
        if is_start_of_semester == 'Yes':
            is_start_of_semester = 1
        else:
            is_start_of_semester = 0

        is_during_semester = request.form['semester_end']
        if is_during_semester == 'Yes':
            is_during_semester = 1
        else:
            is_during_semester = 0

        month = request.form['month']
        if month == 'January':
            month = 1
        elif month == 'February':
            month = 2
        elif month == 'March':
            month = 3
        elif month == 'April':
            month = 4
        elif month == 'May':
            month = 5
        elif month == 'June':
            month = 6
        elif month == 'July':
            month = 7
        elif month == 'Augest':
            month = 8
        elif month == 'September':
            month = 9
        elif month == 'October':
            month = 10
        elif month == 'November':
            month = 11
        elif month == 'December':
            month = 12

        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        second = int(request.form['second'])

        timestamp = (hour * 3600) + (minute * 60) + (second)
        output = model.predict([[timestamp, day_of_week, is_weekend, is_holiday, tempeature, is_start_of_semester, is_during_semester, month]])
        return render_template('predict.html', prediction = int(output), hr=hour, min=minute, sec=second)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)