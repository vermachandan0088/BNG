from flask import Flask,render_template,url_for,request
from flask import jsonify
import  ner
import json
import pandas as pd 
import pickle
import numpy as np
#from sklearn.externals import joblib
import joblib
import language_detection_function

app = Flask(__name__)
svm_model=joblib.load("Svm_Model.pkl")
nb_model=joblib.load("nb_Model.pkl")
tf_vectorize=joblib.load("tf_vectorizer.pkl")
@app.route('/')
def bng():
    return "bng"
@app.route('/predictAdmin',methods=['POST'])
def predict():
    input_keyword=request.get_data()
    input_keyword=input_keyword.decode("utf-8")
    input_keyword=str(input_keyword)
    result_keyword=language_detection_function.language_detection(input_keyword)
    lang=result_keyword[0]
    word_=result_keyword[2]
    ner_=ner.ner_detection(input_keyword)
    if lang=="English":
         #print(ner_)
         vec=tf_vectorize.transform([word_])
         cat1=nb_model.predict(vec)
         cat2=svm_model.predict(vec)
         Naive_Model =str(cat1)
         Svm_model=str(cat2)
         print(f"{word_} categories by Model1:Naive_Bays is  {cat1} and By model2:SVM {cat2}")
         #classify_list=np.array([cat1,cat2])
         #result=list(np.unique(classify_list))
    if lang != "English" and lang!="un":
        print(f"Very Soon BNG Also Avialable for {result_keyword[0]} Language")
        print("May be enter keyword by You is not sufficient for detecting English Language")
        print("Enter some more keyword for detecting English Language")
        Naive_Model="Input Keyword is in "+lang+" Language BNG Model Only work for English"
        Svm_model="Input Keyword is in "+lang+" Language BNG Model Only work for English"
    if lang!="English" and lang=="un":
         print(f"BNG Model Could Not be able to Detect any Language for Input {word_}")
         print("May be enter keyword by You is not sufficient for detecting English Language")
         print("Enter some more keyword for detecting English Language")
         Naive_Model="BNG Model Could Not be able to Detect any Language for Input Keyword "
         Svm_model="BNG Model Could Not be able to Detect any Language for Input Keyword "
    return jsonify(
        naiveModel=Naive_Model,
        svmModel=Svm_model,
        inputkeyword=input_keyword,
        NameEntity=ner_
        
    )
@app.route('/predictUser',methods=['POST'])
def predictUser():
    input_keyword=request.get_data()
    input_keyword=input_keyword.decode("utf-8")
    input_keyword=str(input_keyword)
    ner_=ner.ner_detection(input_keyword)
    result_keyword=language_detection_function.language_detection(input_keyword)
    lang=result_keyword[0]
    word_=result_keyword[2]
    if lang=="English":
         vec=tf_vectorize.transform([word_])
         cat1=nb_model.predict(vec)
         cat2=svm_model.predict(vec)
         Naive_Model =str(cat1)
         Svm_model=str(cat2)
         print(f"{word_} categories by Model1:Naive_Bays is  {cat1} and By model2:SVM {cat2}")
         classify_list=np.array([Naive_Model,Svm_model])
         result=list(np.unique(classify_list))
    if lang != "English" and lang!="un":
        print(f"Very Soon BNG Also Avialable for {result_keyword[0]} Language")
        print("May be enter keyword by You is not sufficient for detecting English Language")
        print("Enter some more keyword for detecting English Language")
        result="Input Keyword is in "+lang+" Language BNG Model Only work for English"
    if lang!="English" and lang=="un":
         print(f"BNG Model Could Not be able to Detect any Language for Input {word_}")
         print("May be enter keyword by You is not sufficient for detecting English Language")
         print("Enter some more keyword for detecting English Language")
         result="BNG Model Could Not be able to Detect any Language for Input Keyword "
    return jsonify(
        Category=result,
        inputkeyword=input_keyword,
        NameEntity=ner_
    )

   
if __name__ == "__main__":
    app.run(debug=True,port=8086)
    
