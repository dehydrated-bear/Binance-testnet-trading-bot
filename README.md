Binance Futures Trading Bot

This is a simple crypto trading bot for the **Binance Futures Testnet**.  
You can use it through a clean **web UI (Flask)** or a fast **command-line interface (CLI)**.

It supports:
- ✅ Market & Limit orders (buy/sell)
- ✅ Stop-Limit orders 
- ✅ Secure API key handling via `.env`
- ✅ Logs & clean error handling

## 🖥️ Screenshots

### CLI

![Screenshot 2025-07-08 191453](https://github.com/user-attachments/assets/2b4bc4ac-536e-4872-b2cb-392d1f49621a)

## Web app

![Screenshot 2025-07-08 191833](https://github.com/user-attachments/assets/3a01157b-ea70-4af1-9473-963152371263)


to run it clone this repo , make a venv , install requirements , make a .env file and in it add the API_KEY and Secret_key 

run the flask webappfrom front.py 

and the cli from tradebot.py

CLI usage
You can run the trading bot directly from the command line with various options:

python tradebot.py --type ORDER_TYPE --side BUY_OR_SELL --symbol SYMBOL --quantity AMOUNT [--price PRICE] [--stop_price STOP] [--limit_price LIMIT]

i was not sure about Grid, Stop-Limit, or OCO with testnet.binancefuture so i did not added it .

