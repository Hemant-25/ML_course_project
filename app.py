from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    sex=request.form.value(['sex'])
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    output='success'
    return render_template('index2.html', prediction_text=' Probability of Heart Disease is : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)