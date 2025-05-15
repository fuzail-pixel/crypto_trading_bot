from flask import Blueprint, render_template, request
from app.bot import BasicBot

views = Blueprint("views", __name__)
bot = BasicBot()

@views.route("/", methods=["GET", "POST"])
def index():
    message = None
    order = None

    if request.method == "POST":
        symbol = request.form["symbol"]
        side = request.form["side"]
        order_type = request.form["order_type"]
        quantity = float(request.form["quantity"])
        price = request.form.get("price")
        stop_price = request.form.get("stop_price")
        take_profit = request.form.get("take_profit")
        stop_loss = request.form.get("stop_loss")

        # Convert optional prices to float if provided
        price = float(price) if price else None
        stop_price = float(stop_price) if stop_price else None
        take_profit = float(take_profit) if take_profit else None
        stop_loss = float(stop_loss) if stop_loss else None

        if order_type == "oco":
            if not take_profit or not stop_loss:
                message = "Please provide both Take Profit and Stop Loss prices for OCO orders."
            else:
                result = bot.place_oco_order(symbol, side, quantity, take_profit, stop_loss)
                if result:
                    message = "✅ OCO order placed successfully!"
                    order = result
                else:
                    message = "❌ Failed to place OCO order."
        else:
            # For other order types
            if order_type == "limit" and price is None:
                message = "Price is required for Limit orders."
            elif order_type == "stop_limit" and stop_price is None:
                message = "Stop Price is required for Stop-Limit orders."
            else:
                result = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
                if result:
                    message = "✅ Order placed successfully!"
                    order = result
                else:
                    message = "❌ Failed to place order."

    return render_template("index.html", message=message, order=order)
