#realizzae un sito web che restituisca la mappa dei quartieri di milano
#ci deve essere una home page con un link ''quartieeri di milano'': cliccando su questo link si deve visualizzare la mappa dei quartieri di milano 
from flask import Flask, render_template, send_file, make_response, url_for, Response, request
app = Flask(__name__)

import io
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

quartieri = gpd.read_file('/workspace/flask/ds964_nil_wm (1).zip')

@app.route('/', methods=['GET'])
def home():
    return render_template('home1.html')



@app.route('/result', methods=['GET'])
def mpl():
    global quartieri2
    value = request.args['value']
    quartieri2 = quartieri[quartieri.NIL.str.contains(value)]
    nome = quartieri[quartieri.NIL.str.contains(value)]['NIL'].values[0]
    return render_template('result.html', nome=nome)


@app.route('/result.png', methods=['GET'])
def result():

    
    fig, ax = plt.subplots(figsize = (12,8))
    quartieri2.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)