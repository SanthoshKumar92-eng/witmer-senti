# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:17:38 2020

@author: Santhosh.Witmer
"""
from flask import abort, Flask, request,render_template
from transformers import pipeline
# =============================================================================
# from flair.models import TextClassifier
# from flair.data import Sentence
# from flask import render_template
# =============================================================================


app = Flask(__name__)

@app.route("/")
def loadPage():
	return render_template('login.html', query="")

@app.route('/data', methods=['POST'])
# =============================================================================
# def sentimentAnalysis():
#     inputQuery = request.form['query']
#     sentence = Sentence(inputQuery)
#     classifier.predict(sentence)
#     print('Sentiment: ', sentence.labels)
#     label = sentence.labels[0]
#     labscore = (label.score)*100
#     response = {'result': label.value, 'score':"%.2f" % labscore}
#     return render_template('home.html', query=inputQuery, output=response)
# =============================================================================
def getdata():
   nlp = pipeline("sentiment-analysis")
   sent=request.form.get('Enter the Sentence')
   result = nlp(sent)[0]
   return(f"Entered Sentence is: {result['label']}, with Accuracy: {round(result['score'], 4)}")
   




if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
