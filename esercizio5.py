#si vuole realizzare un sito web per memorizare le squadre di uno sport a scelta.
#l'utente deve poter inserire il nome della squadra e la data di fondazione e la città 
#deve inoltre poter effettuare delle ricerche insrendo uno dei valori dele colonne e ottenendo i dati presenti
from flask import Flask, render_template, request 
app = Flask(__name__)

import pandas as pd 



@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/data', methods=['GET'])
def data():
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)