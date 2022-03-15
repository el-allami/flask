#si vuole analizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia covid nel nostro paese
#a partire dai dati presenti nel file ''
# l'utente sceglie la regione da un elenco (menu a tendina)
#clicca su un bottone  e il sito deve visualizzare una tabella contenente le informazioni relative a quella regione
#i dati da inserire nel menu a tendina devono essere caricati autoamticamente dalla pagina
from flask import Flask, render_template, request 
app = Flask(__name__)

import pandas as pd 



@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route('/data', methods=['GET'])
def data():
    #prende la regione inserita dall'utente
    regione = request.args['regioni']
    #carica le informazioni riguardanti platea-dose-addizionale-booster
    df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv")
    #selezioniamo tutti i record relativi alla regione inserita dall'utente
    dati = df[df['nome_area'] == regione]
    #restituisce i dati della regione scelta in formato html
    return dati.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)