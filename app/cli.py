import argparse
from app.bot import BasicBot

def main():
    print(" CLI started")
    parser = argparse.ArgumentParser(description="Crypto Trading Bot CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Order placing
    place_parser = subparsers.add_parser("order", help="Place a new order")
    place_parser.add_argument("--symbol", required=True)
    place_parser.add_argument("--side", required=True, choices=["buy", "sell"])
    place_parser.add_argument("--type", required=True, choices=["market", "limit", "stop_limit", "oco"])
    place_parser.add_argument("--quantity", type=float, required=True)
    place_parser.add_argument("--price", type=float, help="Price for limit orders")
    place_parser.add_argument("--stop-price", type=float, help="Stop price for stop-limit orders")
    place_parser.add_argument("--take-profit", type=float, help="Take-profit price for OCO")
    place_parser.add_argument("--stop-loss", type=float, help="Stop-loss price for OCO")

    # Status check
    status_parser = subparsers.add_parser("status", help="Check order status")
    status_parser.add_argument("--symbol", required=True)
    status_parser.add_argument("--order-id", required=True, type=int)

    args = parser.parse_args()
    bot = BasicBot()

    if args.command == "order":
        if args.type == "oco":
            if not args.take_profit or not args.stop_loss:
                parser.error("--take-profit and --stop-loss are required for OCO orders")
            result = bot.place_oco_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                take_profit=args.take_profit,
                stop_loss=args.stop_loss
            )
        else:
            if args.type == "limit" and args.price is None:
                parser.error("--price is required for limit orders")
            if args.type == "stop_limit" and args.stop_price is None:
                parser.error("--stop-price is required for stop-limit orders")

            result = bot.place_order(
                symbol=args.symbol,
                side=args.side,
                order_type=args.type,
                quantity=args.quantity,
                price=args.price,
                stop_price=args.stop_price
            )

        if result:
            print("Order placed successfully:")
            print(result)
        else:
            print(" Failed to place order. Check logs for details.")

    elif args.command == "status":
        print(f"🔍 Fetching status for order {args.order_id}...")
        result = bot.check_order_status(args.symbol, args.order_id)
        if result:
            print(" Order Status:")
            print(result)
        else:
            print(" Could not fetch order status.")

if __name__ == "__main__":
    main()
