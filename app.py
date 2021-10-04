from flask import Flask,request,render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)

#reading the train csv file in order to standardize the inputs
train_data = pd.read_csv("X_train.csv")
scaler = StandardScaler().fit(train_data)

# loading the model
pickle_in=open("bank_note_classifier.pkl","rb")
classifier = pickle.load(pickle_in)
# loading the standard scaler that was fit on train data before training the model
scaler = open("std_scaler.pkl","rb")
scaler = pickle.load(scaler)

@app.route("/", methods=['GET'])
def welcome():
	return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict_note_auth():
	result=""
	variance=request.form.get("variance")
	skewness=request.form.get("skewness")
	curtosis=request.form.get("curtosis")
	entropy=request.form.get("entropy")
	prod_inp = [[variance,skewness,curtosis,entropy]]
	prod_inp_standardized = scaler.transform(prod_inp)
	prediction=classifier.predict(prod_inp_standardized)
	if prediction[0]==1:
		result="Beware!! This note is FAKE!"
	else:
		result="This note is not counterfeit :)"
	return render_template('index.html',prediction=result,imageloc="IMG20211004183819.jpg")


if __name__=="__main__":
	app.run(host='0.0.0.0',port=8080)