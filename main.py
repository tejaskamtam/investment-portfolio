#   Tejas Kamtam

import requests
import csv
import time
from datetime import date

today = date.today().strftime('%Y-%m-%d')

API_KEY = ''

headers = ['Ticker','Name','Exchange','Sector','MarketCap','Close','52WkLo','52WkHi','Target','EPS','PE','PEG','EV/EBITDA','EV/Revenue','1YDel','3YDel','5YDel','50EMA','200EMA', 'Beta', 'Raw Score', 'Raw Weight', 'Rating', 'TK Score', 'Weight %', 'Weight $']

#   ommits ETFs: SPY, SPYG, QQQ, SLYG, VUG, VOO, VOOG, ARKK, IWP, GLD, XOP, TLT
tickers = ['TSLA','AMD','SHOP','MDB','NVDA','ETSY','AAPL','SQ','TGT','MSFT','PG','ADBE','ZEN','SONY','MA','EFX','TMO','INTU','TSM','PFE','CMG','V','KO','TRU','MU','AMZN','GOOGL','NKE','TWLO','NOK','YETI','ON','TXN','ACN','WMT','JNJ','AVGO','UNH','ALGN','BBY','MCD','NET','DIS','HD','DPZ','TM','MTH','DELL','PYPL','TTWO','IBM','QCOM','BLK','CRM','TWTR','CRWD','DOCU','ZM','NFLX','FB','EBAY','FDX','NIO','SNAP','DDOG','CVS','REGN','SHAK','CRSR','ULTA','ZG','UBER','SPOT','T','WOOF','SPCE','PTON','BABA','DASH','COIN','LYFT','XOM']

with open('stock-data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for i in range(len(tickers)):
        overview_url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol='+tickers[i]+'&apikey='+API_KEY
        overview = requests.get(overview_url).json()

        writer.writerow([overview['Symbol'],overview['Name'],overview['Exchange'],overview['Sector'],overview['MarketCapitalization'],'Close',overview['52WeekLow'],overview['52WeekHigh'],overview['AnalystTargetPrice'],overview['EPS'],overview['PERatio'],overview['PEGRatio'],overview['EVToEBITDA'],overview['EVToRevenue'],'1YDel','3YDel','5YDel',overview['50DayMovingAverage'],overview['200DayMovingAverage'], overview['Beta'], 'Raw Score', 'Raw Weight', 'Rating', 'TK Score', 'Weight %', 'Weight $'])
        if i%4 == 0:
            time.sleep(61)


