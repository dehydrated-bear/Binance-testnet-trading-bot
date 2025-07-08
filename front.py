from flask import Flask, render_template, request, flash
from tradebot import Trading_bot
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'may_i_have_some_oats_brother'  

bot = Trading_bot(os.getenv("API_KEY"), os.getenv("Secret_key"))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol']
        side = request.form['side']
        type_ = request.form['type']
        quantity = float(request.form['quantity'])
        price = request.form.get('price', None)

        try:
            if type_ == 'market':
                result = bot.place_market_order(symbol, side, quantity)
            elif type_ == 'limit' and price:
                result = bot.place_limit_order(symbol, side, quantity, float(price))
            else:
                flash("Invalid input or missing price for limit order", 'error')
                return render_template('index.html')

            flash(f"Order placed: {result}", 'success')
        except Exception as e:
            flash(f"Error placing order: {e}", 'error')

    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)