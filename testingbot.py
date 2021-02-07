import pickle
import os.path as path
from datetime import datetime, timedelta
import time
import pytz
import pandas as pd
import math
import robin_stocks as r
import tideconfig as cfg
import talib
import mplfinance as mpf

r.login(cfg.rh['username'], cfg.rh['password'])

data = r.get_crypto_historicals('BTC', interval='5minute', span='week', info=None)
reformatted_data = dict()
reformatted_data['Date'] = []
reformatted_data['Open'] = []
reformatted_data['High'] = []
reformatted_data['Low'] = []
reformatted_data['Close'] = []
reformatted_data['Volume'] = []
for dict in data:
    reformatted_data['Date'].append(datetime.strptime(dict['begins_at'],"%Y-%m-%dT%H:%M:%SZ"))
    reformatted_data['Open'].append(float(dict['open_price']))
    reformatted_data['High'].append(float(dict['high_price']))
    reformatted_data['Low'].append(float(dict['low_price']))
    reformatted_data['Close'].append(float(dict['close_price']))
    reformatted_data['Volume'].append(float(dict['volume']))
# print(reformatted_data)
df = pd.DataFrame(reformatted_data)
df = df.set_index('Date')
print(df.tail(10))

mpf.plot(df, type='candle',mav=(20,40,60))
