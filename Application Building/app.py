import flask
from flask import request, render_template
from flask_cors import CORS
import joblib

app = flask.Flask(__name__, static_url_path='')
CORS(app)

@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictSpecies():
    Age=float(request.form['Age'])
    EstimatedSalary = float(request.form['EstimatedSalary'])
    X = [[ Age,EstimatedSalary]]
    model = joblib.load('Social_Network_Ads.pkl')
    Purchased = model.predict(X)[0]
    return render_template('predict.html',predict=Purchased)
if __name__ == '__main__':
    app.run()