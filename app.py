from flask import Flask,render_template
import random
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/meteo', methods=['GET'])
def meteo():
    # generazione numero casuale 
    numero_casuale= random.randrange(1, 10)
    # se il numero è minore di 2 
    if numero_casuale <= 2:
        return render_template('pagina1.html',previsione = 'pioggia' )
    # se il numero è comreso tra 3 e 5 nuvoloso 
    elif numero_casuale <=5:
        return render_template('pagina1.html',previsione = 'nuvoloso' )
    # se e maggiore di 5 sole
    else:
        return render_template('pagina1.html',previsione = 'sole' )


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)