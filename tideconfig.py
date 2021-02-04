#!/usr/bin/env python

rh = {
    "username": "",
    "password": "",
}

config = {
    "statusEmailAddress": "fake@gmail.com",
    "buyLimit": 0.0075, # how far below the MA the price has to be to trigger a buy (default is 0.75%)
    "sellLimit": 0.01, # % profit required to seel (default 1%)
    "movingAverageWindows": 20, # 2 hours * 60 samples per hour
    "runMinute": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58,], # 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55
    "coinList": ["BTC", "LTC", "ETH", "DOGE"],
    "tradesEnabled": True,
    "rsiWindow": 10,
}
