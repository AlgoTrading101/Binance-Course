from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance import ThreadedWebsocketManager
from time import sleep

api_key = 'Yn1i6aNWBdp9YxLsdPLUNFE4BPMXroZv6tZ9syC7xhhkvBiVUGOddrf3TEQvsUZU'
api_secret = '59IXgQHzoEjuxy6qHkMvW15U6pxnIw71YHI4lsIXE8lOE7q58Xrn8zYcFCUP2xzh'

client = Client(api_key=api_key, api_secret=api_secret)

price = {'BTCUSDT': None, 'error':False}

def btc_pairs_trade(msg):
    #process incoming messages 
    if msg['e'] != 'error':
        price['BTCUSDT'] = float(msg['c'])
    else:
        price['error']:True

twm = ThreadedWebsocketManager()
twm.start()
socket = twm.start_symbol_ticker_socket(callback=btc_pairs_trade, symbol='BTCUSDT')

while not price['BTCUSDT']:
    sleep(0.1)

while True:
    if price['error']:
        twm.stop()
        twm.start()
        socket = twm.start_symbol_ticker_socket(callback=btc_pairs_trade, symbol='BTCUSDT')
        price['error'] = False

    else:
        if price['BTCUSDT'] > 33300:
            try:
                order = client.order_market_buy(symbol='ETHUSDT', quantity=0.006)
                break
            except BinanceAPIException as e:
                print(e)
            except BinanceOrderException as e:
                print(e)
    sleep(0.1)
    
twm.stop()

sleep(2)

try:
    status = client.get_order(symbol='ETHUSDT', orderId=order['orderId'])
except Exception as e:
    print('Error obtaining order status')

if status['status'] == 'FILLED' or 'NEW':
    print('Order placed successfully')
    print(status)
else:
    print('Order was rejected')  