"""
Retrieve the average volume of weekly trade per year for each stock.
store result in csv
"""

import sqlite3 as sql
import pandas as pd
from collections import defaultdict

if __name__ == "__main__":
    
    connection = sql.connect("AlphaVantage.db")
    cursor = connection.cursor()
    
    # Query 
    with connection:
        cursor.execute("""
                       SELECT stock, strftime('%Y', date) as 'Year', AVG(volume)
                       FROM stock_weekly 
                       GROUP BY Year, stock
                       """)
        
    data = cursor.fetchall()
    
    group_by_year = defaultdict(list)
    for datum in data:
        group_by_year[datum[1]].append(datum[2])
    
    df = pd.DataFrame.from_dict(group_by_year, 
                                orient='index',
                                columns = ['AMZN', 'TSLA', 'TWTR'])
    
    # Write to csv
    df.to_csv('stock_avg_volume_per_year.csv')