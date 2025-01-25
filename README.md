# Tide Goes In, Tide Goes Out

Forked from [JasonRBowling/cryptoTradingBot](https://github.com/JasonRBowling/cryptoTradingBot)

### From [original author](https://github.com/JasonRBowling/):
Experimental crypto trading bot using robin-stocks. Such things are very risky. For educational purposes only. Write up at [Medium](https://medium.com/swlh/a-full-crypto-trading-bot-in-python-aafba122bc4e)

----------------

## Overview

This project is an experimental cryptocurrency trading bot that uses the Robinhood API via the `robin_stocks` package. The bot is designed to automate the buying and selling of cryptocurrencies based on predefined trading strategies.

## Features

- Automated trading using the Robinhood API
- Configurable trading strategies
- Uses technical analysis indicators such as Moving Averages and RSI
- Saves and loads state to/from disk

## Installation

### Prerequisites

- Python 3.x
- Robinhood account with API access

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tideGoesInTideGoesOut.git
    cd tideGoesInTideGoesOut
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure your Robinhood credentials and trading strategy in `tideconfig.py`:
    ```python
    # DO NOT UPLOAD THIS FILE WITH YOUR CREDENTIALS IN IT! TURN ON 2 FACTOR AUTHENTICATION JUST IN CASE!
    rh = {
        'username': 'yourUserNameHere',
        'password': 'yourPasswordHere',
    }

    # Modify these values to fit your trading strategy.
    config = {
        'sellLimit': 0.01, # Percentage profit required to sell. 
        'movingAverageWindows': 20, # How many periods to consider for MA.
        'runMinute': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58,], # What minute, on the minute, data will be refreshed. (this is also when buy/sell conditions are checked and executed) 
        'coinList': ['BTC', 'SOL', 'DOGE', 'ETH',], 
        'minutesBetweenUpdates': 2,
        'tradesEnabled': False, # When set to True, real buys/sells are possible.
        'rsiWindow': 10, # How many periods to consider for RSI.
    }
    ```

## Usage

### Running the Bot

Navigate to the directory where you cloned the repository and run the Python script:
```sh
python tideGoesInTideGoesOut.py
```

## Important Notes

- **Risk Warning**: Trading cryptocurrencies is highly risky. This bot is for educational purposes only. Use it at your own risk.
- **Security**: Do not upload your credentials to any public repository. Enable two-factor authentication on your Robinhood account.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [JasonRBowling](https://github.com/JasonRBowling) for the original crypto trading bot
- [robin_stocks](https://github.com/jmfernandes/robin_stocks) for the Robinhood API wrapper
