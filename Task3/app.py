from flask import Flask, render_template
import sqlite3 as sql
import plotly
import plotly.express as px
import pandas as pd
import json

app = Flask(__name__)

def connect_db():
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    return cursor

@app.route('/')
def root():
    return "root"

@app.route('/GET/stocks')
def get():
    connect_db()
    with connection:
        cursor.execute("""
                       SELECT DISTINCT stock FROM stock_weekly;
                       """)
    available_stock = cursor.fetchall()
    return str(available_stock)


@app.route('/PLOT/stocks')
def index():
   
    data = connect_db().execute('SELECT * FROM stock_weekly').fetchall()

    return render_template('plot.html', name=str(data))


@app.route('/plot/volume')
def plot_volume():        
    data = connect_db().execute(
        'SELECT date,volume,stock FROM stock_weekly').fetchall()
    
    df = pd.DataFrame(data, columns=['year', 'volume', 'stock'])
    
    fig = px.line(df, x="year", y="volume", color='stock',
                  title='Volume of Weekly trade')
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('plot.html', graphJSON=graphJSON)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)