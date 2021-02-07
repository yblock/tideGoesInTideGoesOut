#!/usr/bin/env python

# DO NOT UPLOAD THIS FILE WITH YOUR CREDENTIALS IN IT! TURN ON 2 FACTOR AUTHENTICATION JUST IN CASE!
rh = {
    'username': 'yourUserNameHere',
    'password': 'yourPasswordHere',
}

# Modify these values to fit your trading strategy.
config = {
    'sellLimit': 0.01, # Percentage profit required to sell. 
    'movingAverageWindows': 20, # How many periods to consider for MA.
    'runMinute': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58,], # What minute, on the minute, data will bre refreshed. (this is also when buy/sell conditions are checked and executed) 
    'coinList': ['BTC', 'LTC', 'ETH',],
    'tradesEnabled': False, # When set to True, real buys/sells are possible.
    'rsiWindow': 10, # How many periods to consider for RSI.
}
