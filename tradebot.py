from binance.client import Client
import time

import os
from dotenv import load_dotenv



load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("Secret_Key")

# print(API_KEY,API_SECRET)

client=Client(API_KEY,API_SECRET,testnet=True)

# print(client.get_account())

symbol='BTCUSDT'
buy_price_threshold=60000
sell_price_threshold=68000
trade_quantity=0.001


def get_current_price(symbol):
    ticker=client.get_symbol_ticker(symbol=symbol)
    print(ticker)
    return float(ticker['price'])

# get_current_price(symbol)


def place_buy_order(symbol,quantity):
    order=client.order_market_buy(symbol=symbol,quantity=quantity)
    print(f"buy order done {order}")

# place_buy_order(symbol,trade_quantity)


def place_sell_order(symbol,quantity):
    order=client.order_market_sell(symbol=symbol,quantity=quantity)
    print(f"sell order done {order}")


# place_sell_order(symbol,trade_quantity)



def trading_bot():
    in_position=False

    while True:
        curr_price=get_current_price(symbol)
        print(f"current price of{symbol}:{curr_price}")

        if not in_position:
            if curr_price<buy_price_threshold:
                place_buy_order(symbol,trade_quantity)
                in_position=True
        
        else:
            if curr_price>sell_price_threshold:
                place_sell_order(symbol,trade_quantity)      
                in_position=False

        time.sleep(5)          


if __name__=="__main__":
    trading_bot()