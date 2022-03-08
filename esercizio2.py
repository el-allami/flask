#realizzare un sito web che permetta la registraione degli utenti
#l'utente inserisce il nome,un username, una password
#la conferma della password e il sesso.
#se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna(una lista di dizionario)
#prevedre la possibilita di fare il login 
#username e password 
#se sono corrette fornire un messaggio di benvenuto diverso a seconda del sesso 
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('reg.html')


@app.route('/data', methods = ['GET'])
def data():
    nome = request.args['Name']
    Cognome = request.args['Cognome']
    username = request.args['username']
    Sex = request.args['Sex']
    password = request.args['password']
    Conferma_Password  = request.args['Conferma_Password']
    if password == Conferma_Password:
        if Sex == 'M':
            msg= 'BENVENUTO' + nome
        elif Sex  == 'F':
             msg= 'BENVENUTA' + nome
        else:
            msg = 'BENVENUT*' + nome
        return render_template('welcome2.html',messaggio=msg)      
    else:
        msg = 'PASSWORD NON COINCIDENTI'
        return render_template('welcome2.html',messaggio=msg)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)