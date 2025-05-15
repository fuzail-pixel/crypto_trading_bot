from binance.client import Client
from binance.enums import (
    SIDE_BUY,
    SIDE_SELL,
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC
)
from app.config import API_KEY, API_SECRET, TESTNET
from app.logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Binance client initialized (Testnet mode: %s)", TESTNET)

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            order_params = {
                'symbol': symbol,
                'side': SIDE_BUY if side.lower() == "buy" else SIDE_SELL,
                'quantity': quantity,
            }

            if order_type.lower() == "market":
                order_params['type'] = ORDER_TYPE_MARKET

            elif order_type.lower() == "limit":
                order_params['type'] = ORDER_TYPE_LIMIT
                order_params['price'] = price
                order_params['timeInForce'] = TIME_IN_FORCE_GTC

            elif order_type.lower() == "stop_limit":
                order_params['type'] = "STOP_MARKET"
                order_params['stopPrice'] = stop_price

            else:
                logger.error("Unsupported order type: %s", order_type)
                return None

            logger.info("Placing order: %s", order_params)
            order = self.client.futures_create_order(**order_params)
            logger.info("Order successful: %s", order)
            return order

        except Exception as e:
            logger.error("Error placing order: %s", str(e))
            return None

    def place_oco_order(self, symbol, side, quantity, take_profit, stop_loss):
        try:
            side_enum = SIDE_SELL if side.lower() == "sell" else SIDE_BUY

            # Take-Profit (Limit)
            limit_order = self.client.futures_create_order(
                symbol=symbol,
                side=side_enum,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=take_profit,
                timeInForce=TIME_IN_FORCE_GTC
            )

            # Stop-Loss (Stop-Market)
            stop_order = self.client.futures_create_order(
                symbol=symbol,
                side=side_enum,
                type="STOP_MARKET",
                stopPrice=stop_loss,
                quantity=quantity
            )

            logger.info("Simulated OCO: Limit: %s, Stop: %s", limit_order, stop_order)
            return {"limit_order": limit_order, "stop_order": stop_order}

        except Exception as e:
            logger.error("Error placing OCO order: %s", str(e))
            return None

    def check_order_status(self, symbol, order_id):
        try:
            logger.info("Checking status for order ID: %s", order_id)
            result = self.client.futures_get_order(symbol=symbol, orderId=order_id)
            logger.info("Order status: %s", result)
            return result
        except Exception as e:
            logger.error("Error checking order status: %s", str(e))
            return None
