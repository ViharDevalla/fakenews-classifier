from flask import Flask,request, url_for, redirect, render_template, jsonify
from flask_ngrok import run_with_ngrok
import pickle
import requests
import numpy as np
import pandas as pd
import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import joblib
from bs4 import BeautifulSoup
import re

logrecsaved = joblib.load('logregmodel4.pkl')
tfidf_vectorizer = pickle.load(open('tfidf4.pkl','rb'))

def articlecheck(article):
  if article == "Invalid URL":
   return("Invalid URL")

  ps= PorterStemmer()
  stopWords = set(stopwords.words('english'))
  words = word_tokenize(article)
  stem=[]
  for w in words:
    if w not in stopWords:
      stem.append(ps.stem(w))
  finalart=' '.join(stem)
  final=[]
  final.append(finalart)
  print(final)
  test1=tfidf_vectorizer.transform(final)
  if logrecsaved.predict(test1)==0:
    return("Given news article is reliable")
  else:
    return("Given news article is unreliable")

def urlsearch(url):
  if re.search('^(ftp|http|https):\/\/[^ "]+$',url):
   pass
  else:
   return("Invalid URL")
  try:
   resp=requests.get(url)
  except:
   return("Invalid URL")
  text=[]
  news_soup = BeautifulSoup(resp.text, "html.parser")
  article = news_soup.find_all('p')
  y=[re.sub(r'<.+?>',r'',str(a)) for a in article]
  s = ''
  for i in y:
    if '{' in i or '[' in i or '(' in i or '@' in i or '|' in i or '..' in i or '/' in i or '\\' in i:
      pass
    else:
      s+=i
  if len(s)>0:
    text.append(s)
    return(text)
#print(logreg.predict(test1))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    articletext = str(request.form['article'])
    return render_template('home.html',pred=articlecheck(articletext))

@app.route('/predict_url',methods=['POST'])
def predict_url():
    
    articletext = str(urlsearch(request.form['url1']))
    return render_template('home.html',pred=articlecheck(articletext))

'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)
'''
if __name__ == '__main__':
    app.run()
