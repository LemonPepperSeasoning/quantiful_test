"""
Weekly stock data for Tesla, Twitter, and
Amazon for the last 15 years. 
(I am going to save data from 2005~)

Seach Endpoint : https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=KEYWORD_YOU_WANT_TO_SEARCH&apikey=YOUR_KEY


Tesala : TSLA
Twitter : TWTR
Amazon : AMZN
"""

import sqlite3 as sql
import requests

def create_table():
    with connection:
        cursor.execute("""
            CREATE TABLE stock_weekly(
                DATE INTEGER,
                STOCK TEXT,
                OPEN REAL,
                HIGH REAL,
                LOW REAL,
                CLOSE REAL,
                VOLUME INTEGER )
            """)
        
def insert_data(data):
    with connection:
        cursor.execute(
            "INSERT INTO stock_weekly VALUES (?,?,?,?,?,?,?)", 
            data)

def print_all():
    with connection:
        cursor.execute("SELECT * FROM stock_weekly")
    for i in cursor.fetchall():
        print (i)

def fetch_stock_api(symbol):
    request_url = (base_url + "function="+function+"&symbol="+symbol+
                   "&apikey="+api_key+"&datatype=" + datatype ) 
    data = requests.get(request_url)
    return data.content.decode("utf-8")


if __name__ == "__main__":
        
    ### Get data from API
    # Alphavantage api key
    api_key = "DJTDDX1NG5JH8Z39"
    base_url = "https://www.alphavantage.co/query?"
    function = "TIME_SERIES_WEEKLY"
    datatype = "csv"
    symbols = ["TSLA","TWTR","AMZN"]
    
    # Define a connection and a cursor for sqlite3
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    
    # Create sql table
    create_table()
    
    # Fetch data and store in db
    for symbol in symbols:
        
        raw_data = fetch_stock_api( symbol )
        
        #First item is always "timestamp,open,high,low,close,volume"
        list_data = raw_data.split()[1:] 
        
        for datum in list_data:
            # split into "timestamp,open,high,low,close,volume"
            x = (datum.split(","))
            
            # Only inserting data after 2005. (Bc we only want last 15 years)
            if x[0] < "2005-0-0":
                continue
            
            # add symbol
            x.insert(1,symbol)

            # insert into sql db
            insert_data(x)

    # print_all()