from flask import Flask
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def root():
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    
    return "root"

@app.route('/GET/stocks')
def get():
    return "TSLA, TWTR, AMZN"

if __name__ == "__main__":
    app.run(debug=True, threaded=True)