#!/usr/bin/env python

rh = {
    'username': '',
    'password': '',
}

config = {
    'sellLimit': 0.01, # % profit required to seel (default 1%)
    'movingAverageWindows': 20,
    'runMinute': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58,], # 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55
    'minutesBetweenUpdates': 2,
    'coinList': ['BTC', 'LTC', 'ETH',],
    'tradesEnabled': False,
    'rsiWindow': 10,
}
