from binance.client import Client
import time
import logging
import argparse

import os
from dotenv import load_dotenv

from colorama import Fore, Style, init


#FUTURE TRADING BOT

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("Secret_Key")


logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



class Trading_bot():
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'



    def get_price(self, symbol):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            logging.info(f"Fetched price for {symbol}: {price}")
            return price
        except Exception as e:
            logging.error(f"Failed to fetch price for {symbol}: {e}")
            return None





    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market order successful: {order}")
            print(f"[SUCCESS] Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Market order failed: {e}")
            print(f"[ERROR] Market order failed: {e}")
            return None



    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f"Limit order successful: {order}")
            print(f"[SUCCESS] Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Limit order failed: {e}")
            print(f"[ERROR] Limit order failed: {e}")
            return None
        

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP_MARKET',  
                stopPrice=stop_price,
                price=limit_price,   
                quantity=quantity,
                timeInForce='GTC'
            )
            logging.info(f"Stop-Limit Order: {order}")
            print(f"[SUCCESS] Stop-Limit order placed:\n{order}")
            return order
        except Exception as e:
            logging.error(f"Stop-Limit Order Error: {e}")
            print(f"[ERROR] Stop-Limit order failed: {e}")
            return None

init(autoreset=True)

def print_intro():
    print(f"{Fore.CYAN}{Style.BRIGHT} Binance Futures Trading Bot CLI")
    print(f"{Fore.YELLOW}What you can do:")
    print(f"{Fore.GREEN}- Place a Market Buy or Sell Order")
    print(f"{Fore.GREEN}- Place a Limit Buy or Sell Order")
    print(f"{Fore.BLUE}Use --type, --side, --quantity (and --price for limit) to place orders\n")


def parse_args():
    print_intro()
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Testnet)")
    parser.add_argument('--type', choices=['market', 'limit'], help="Order type: market or limit")
    parser.add_argument('--side', choices=['buy', 'sell'], required=True, help="Order direction: buy or sell")
    parser.add_argument('--symbol', type=str, default='BTCUSDT', help="Trading pair (default: BTCUSDT)")
    parser.add_argument('--quantity', type=float, required=True, help="Amount to buy/sell")
    parser.add_argument('--price', type=float, help="Limit price (required for limit orders)")
    
    parser.add_argument('--strategy', choices=['stop_limit'], help="Optional strategy mode")
    parser.add_argument('--stop_price', type=float, help="Trigger price for stop-limit")
    parser.add_argument('--limit_price', type=float, help="Execution price for stop-limit")

    return parser.parse_args()


if __name__ == "__main__":
    print_intro()
    args = parse_args()
    bot = Trading_bot(API_KEY, API_SECRET)

    if args.strategy == 'stop_limit':
        if args.stop_price is None or args.limit_price is None:
            print("[ERROR] Stop-Limit order requires both --stop_price and --limit_price.")
        else:
            bot.place_stop_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                stop_price=args.stop_price,
                limit_price=args.limit_price
            )

    elif args.type == 'market':
        bot.place_market_order(args.symbol, args.side, args.quantity)

    elif args.type == 'limit':
        if args.price is None:
            print("[ERROR] Limit order requires a --price argument.")
        else:
            bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)

    else:
        print("[ERROR] You must specify either --type (market/limit) or --strategy (like stop_limit).")

        





# Normal trading bot (not future)

# client=Client(API_KEY,API_SECRET,testnet=True)

# # print(client.get_account())

# symbol='BTCUSDT'
# buy_price_threshold=60000
# sell_price_threshold=68000
# trade_quantity=0.001


# def get_current_price(symbol):
#     ticker=client.get_symbol_ticker(symbol=symbol)
#     print(ticker)
#     return float(ticker['price'])

# # get_current_price(symbol)


# def place_buy_order(symbol,quantity):
#     order=client.order_market_buy(symbol=symbol,quantity=quantity)
#     print(f"buy order done {order}")

# # place_buy_order(symbol,trade_quantity)


# def place_sell_order(symbol,quantity):
#     order=client.order_market_sell(symbol=symbol,quantity=quantity)
#     print(f"sell order done {order}")


# # place_sell_order(symbol,trade_quantity)



# def trading_bot():
#     in_position=False

#     while True:
#         curr_price=get_current_price(symbol)
#         print(f"current price of{symbol}:{curr_price}")

#         if not in_position:
#             if curr_price<buy_price_threshold:
#                 place_buy_order(symbol,trade_quantity)
#                 in_position=True
        
#         else:
#             if curr_price>sell_price_threshold:
#                 place_sell_order(symbol,trade_quantity)      
#                 in_position=False

#         time.sleep(5)          


# if __name__=="__main__":
#     trading_bot()