#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from binance import ThreadedWebsocketManager

symbol = 'ETHUSDT'

twm = ThreadedWebsocketManager()
twm.start()

def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)
        
socket = twm.start_symbol_ticker_socket(callback=handle_socket_messages, symbol=symbol)

