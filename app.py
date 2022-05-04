from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('modelfinal.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    sex=request.form.get('sex')
    age=request.form.get('age')
    cp=request.form.get('chest_pain')
    rbp=request.form.get('resting_bp')
    fbs=request.form.get('fasting_bs')
    recg=request.form.get('resting_ecg')
    mhr=request.form.get('max_hr')
    ea=request.form.get('exercise_angina')
    op=request.form.get('old_peak')
    sts=request.form.get('st_slope')
    features=[]
    features.append(age)
    features.append(rbp)
    features.append(mhr)
    features.append(op)
    features.append(sex)
    if cp==2:
        features.append(1)
        features.append(0)
        features.append(0)
    elif cp==1:
        features.append(0)
        features.append(1)
        features.append(0)
    elif cp==0:
        features.append(0)
        features.append(0)
        features.append(0)
    else:
        features.append(0)
        features.append(0)
        features.append(1)
    features.append(fbs)
    if recg==0:
        features.append(1)
        features.append(0)
    elif recg==1:
        features.append(0)
        features.append(1)
    else:
        features.append(0)
        features.append(0)
    features.append(ea)
    if sts==0:
        features.append(0)
        features.append(1)
    elif sts==1:
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(0)
    # int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]


    prediction = model.predict(final_features)
    if(prediction[0]==0):
        output="Safe"
    else:
        output='At Risk'
    return render_template('index.html', prediction_text=' Report Result : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)