from flask import Flask, render_template
import sqlite3 as sql
import plotly
import plotly.express as px
import plotly.graph_objects as go

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
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    with connection:
        cursor.execute("SELECT DISTINCT stock FROM stock_weekly")
    available_stock = cursor.fetchall()
    return str(available_stock)


@app.route('/PLOT/candlestick/<page_id>')
def index(page_id):
    data = connect_db().execute('SELECT date,open,high,low,close FROM stock_weekly WHERE stock={stock}'.format(stock="'"+page_id+"'")).fetchall()
  
    df = pd.DataFrame(data, columns=['year',
                                     'open', 'high', 'low', 'close'])
    
    fig = go.Figure(data=[go.Candlestick(x=df['year'],
                        open=df['open'],
                        high=df['high'],
                        low=df['low'],
                        close=df['close'])])
    fig.update_layout(title='Candlestick chart',yaxis_title='Price',)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('plot.html', graphJSON=graphJSON)


@app.route('/PLOT/volume')
def plot_volume():        
    data = connect_db().execute(
        'SELECT date,volume,stock FROM stock_weekly').fetchall()
    
    df = pd.DataFrame(data, columns=['date', 'volume', 'stock'])
    
    fig = px.line(df, x="date", y="volume", color='stock',
                  title='Volume of Weekly trade')
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template('plot.html', graphJSON=graphJSON)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)