from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def w209():
    file = 'about9.jpg'
    return render_template('w209.html', file=file)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/getData/<year>')
def getData(year):
    data = pd.read_csv('static/data/1_Revenues.csv')
    data = data[data['Year4'] == int(year)]
    return data.to_json(orient='records')

if __name__ == '__main__':
    app.run()
