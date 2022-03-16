#si vuole realizzare un sito web per memorizare le squadre di uno sport a scelta.
#l'utente deve poter inserire il nome della squadra e la data di fondazione e la città 
#deve inoltre poter effettuare delle ricerche insrendo uno dei valori dele colonne e ottenendo i dati presenti
from flask import Flask, render_template,request
app = Flask(__name__)
import pandas as pd

@app.route('/', methods=['GET'])
def home():
    return render_template('squadra.html')

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('inserisci.html')

@app.route('/dati', methods=['GET'])
def dati():
    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    # lettura dei dati daal file nel dataframe
    df1 = pd.read_csv('/workspace/flask/templates/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    nuovi_dati = {'squadra':squadra,'anno':anno,'citta':citta}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    
    # salviamo il dataframe sul file dati.csv
    df1.to_csv('/workspace/flask/templates/dati.csv', index=False)
    return df1.to_html()
@app.route('/ricerca', methods=['GET'])
def ricerca():
    return render_template('ricerca.html')

@app.route('/risultato', methods=['GET'])
def risultato():
    
    df1 = pd.read_csv('/workspace/flask/templates/dati.csv')
    #if (len(squadra) != 0):
        # cerchiamo tutte le informazioni sulla squadra inserita dall'utente 
       # anno = df1[df1['squadra'] == squadra ]['anno']
    indice= request.args['Indice']
    risultato= request.args['sel']
    df2= df1[df1[risultato] == indice]
    return df2.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)
  app.run(host='0.0.0.0', port=3245, debug=True)