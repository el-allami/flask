#realizzare un server web che permetta di conoscere i capoluoghi di regione
#l'utente inserisce il nome della regione e il programma restituisce il nome della regione
#caricare i capoluoghi di regioni in una lista di dizionari
# modificare l'es precedente e permettere l'utente di inserire il capoluogo della regione 
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio button
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

capoluoghiRegione = {"Abruzzo":"L'Aquila", "Basilicata":"Potenza", "Calabria":"Catanzaro", "Campania":"Napoli", "Emilia-Romagna":"Bologna", "Friuli-Venezia Giulia":"Trieste", "Lazio":"Roma", "Liguria":"Genova", "Lombardia":"Milano", "Marche":"Ancona", "Molise":"Campobasso", "Piemonte":"Torino", "Puglia":"Bari", "Sardegna":"Cagliari", "Sicilia":"Palermo", "Toscana":"Firenze", "Trentino-Alto Adige":"Trento", "Umbria":"Perugia", "Valle d'Aosta":"Aosta", "Veneto":"Venezia"}

@app.route('/', methods=['GET'])
def index():
    return render_template('capoluoghi.html')


@app.route('/risp', methods=['GET'])
def risp():
    indice = request.args['indice']
    radio = request.args['sel']
    if radio == 'regione':
        if indice in capoluoghiRegione:
            capo = capoluoghiRegione[indice]
            return render_template('capoluoghi1.html', capol=capo)
        return render_template('error.html')
    if radio == 'capoluogo':
        dct = {v: a for a, v in capoluoghiRegione.items()}
        if indice in dct:
            capo = dct[indice]
            return render_template('capoluoghi.html', capol=capo)
        return render_template('error.html')
    return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)