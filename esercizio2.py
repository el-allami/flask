#realizzare un sito web che permetta la registraione degli utenti
#l'utente inserisce il nome,un username, una password
#la conferma della password e il sesso.
#se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna(una lista di dizionario)
#prevedre la possibilita di fare il login 
#username e password 
#se sono corrette fornire un messaggio di benvenuto diverso a seconda del sesso 
from flask import Flask, render_template, request
app = Flask(__name__)
lista = []

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
       lista.append({'Name':nome,'username':username,'password':password,'Sex':Sex})
       print(lista)
       return render_template('login.html')
    else:
        return render_template('error.html')

@app.route('/login', methods = ['GET'])
def login():
    username_log = request.args['username']
    password_log = request.args['password']
    for utente in lista:
        if utente['username'] == username_log and utente['password'] == password_log:
            if utente['Sex'] =='M':

              return render_template('welcome2.html',username=utente['Name'])
            else:
             return render_template('benvenuta.html',username=utente['Name'])
    return render_template('error.html',messaggio='username o password errati')
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)