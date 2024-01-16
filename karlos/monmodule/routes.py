from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import model as m
import matplotlib.pyplot as plt
from flask import send_file
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict_get():
    sectors = m.sectors
    return render_template('index.html',secteurs= sectors)
def get_line_plot(data_x, data_y, title=None) -> str:
    # Generate the figure
    fig = plt.figure(figsize=(10, 10))
    plt.plot(data_x, data_y, color='red')
    plt.xticks(rotation=40, ha="right")
    plt.xlabel('Date')
    plt.ylabel('Entrées mensuelles')

    if title is not None:
        plt.title(f'Entrées mensuelles pour le secteur "{title}"')

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    return base64.b64encode(buf.getbuffer()).decode("utf-8")

@app.route('/predict1', methods=['POST'])
def predict1():
    secteurs = m.sectors
    model = ""

    for items in m.modele:
        if items['secteur'] == request.form['secteur']:
            model = items
            break
    print(model)    

    if model == "":
        message = 'Erreur, veuillez vérifier le secteur'
        return render_template('predict.html', message=message)

    try:
        y = model['predict']
        x = model['month']
        
        fig = get_line_plot(data_x=x, data_y=y, title=request.form['secteur'])
        
        # Assurez-vous que prediction est une liste d'objets
        prediction = model
        print(prediction)
        return render_template('predict.html', img=fig, x=y, y=x)
    except Exception as e:
        error_message = f"Une erreur s'est produite : {str(e)}"
        # Faites quelque chose avec l'erreur, par exemple, imprimez-la
        print(error_message)
        # Retournez une réponse appropriée ou affichez un message d'erreur sur la page
        return render_template('predict.html', message=error_message)

@app.route('/statistique')
def visualize():
    
    return render_template('visualisation.html')




