from flask import Flask, render_template, request
import pandas as pd
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def w209():
    file = 'about9.jpg'
    return render_template('w209.html', file=file)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/api')
def api():
    return {"x": 42}

@app.route('/players/count')
def players_count():
    db_path = os.path.join(app.root_path, 'players_20.db')
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    count = cursor.fetchone()[0]

    conn.close()
    return {"count": count}

@app.route('/players/get_nationality')
def get_nationality():
    player = request.args.get('player')

    if not player:
        return {"error": "Please provide a player name"}, 400

    db_path = os.path.join(app.root_path, 'players_20.db')
    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()
    cursor.execute(
        "SELECT nationality FROM players WHERE short_name = ?",
        (player,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return {"nationality": result[0]}
    else:
        return {"error": "Player not found"}, 404

@app.route('/getData/<year>')
def getData(year):
    data = pd.read_csv('static/data/1_Revenues.csv')
    data = data[data['Year4'] == int(year)]
    return data.to_json(orient='records')

if __name__ == '__main__':
    app.run()
