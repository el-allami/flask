#realizzare un server web che permetta di effettuare il login 
#l'utente inserisce lo username e la password:
#se lo username è l'admin e la password xxx123##
#il sito ci saluta con un messaggio di benvenuto altrimenti ci da un messaggio di errore
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world():
    return render_template('user1.html')

@app.route('/data', methods = ['GET'])
def data():
    username = request.args['username']
    password = request.args['password']
    if username == 'admin' and  password == 'xxx123##':
         return render_template('welcome.html',Name=username)
    else:
         return render_template('error.html',Name=username)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)