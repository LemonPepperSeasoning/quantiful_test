from flask import Flask, render_template
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def root():
    return "root"

@app.route('/GET/stocks')
def get():
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    
    with connection:
        cursor.execute("""
                       SELECT DISTINCT stock FROM stock_weekly;
                       """)
    available_stock = cursor.fetchall()
    return str(available_stock)

# @app.route('/GET/stocks/{id}')
# def get():
#     connection = sql.connect("AlphaVantage.db")
#     cursor = connection.cursor()
    
#     with connection:
#         cursor.execute("""
#                        SELECT DISTINCT stock FROM stock_weekly;
#                        """)
#     available_stock = cursor.fetchall()
#     return str(available_stock)

@app.route('/PLOT/stocks')
def index():
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    
    data = cursor.execute('SELECT * FROM stock_weekly').fetchall()
   
    return render_template('index.html', name=str(data))


if __name__ == "__main__":
    app.run(debug=True, threaded=True)