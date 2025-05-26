import sys
from config import create_client
from utils import log_and_print

class BasicBot:
    def __init__(self):
        self.client = create_client()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            order = None
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            log_and_print(f"Order placed: {order}")
        except Exception as e:
            log_and_print(f"Error placing order: {e}")

def main():
    bot = BasicBot()
    log_and_print("Welcome to Binance Futures Bot")

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))
    price = None

    if order_type == 'LIMIT':
        price = float(input("Enter limit price: "))

    bot.place_order(symbol, side, order_type, quantity, price)

if __name__ == "__main__":
    main()
