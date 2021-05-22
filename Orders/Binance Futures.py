#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from binance.client import Client
from binance.enums import *

api_key = '5LzrB7qgTo8JdE2FLyQaeETUzqe9VPnvuhyNZR8cnWiWaHKnEd63TtszjiittRel'
api_secret = 'OAmvCjkfmznyrK176n7uN3vZYgLQ3rmHUnrmbkmRx9mprdFQNz5BrnV5UQtJUczJ'

client = Client(api_key=api_key, api_secret=api_secret)

order = client.futures_create_order(
                        symbol='ETHUSDT_210625',
                        side=SIDE_SELL,
                        type=ORDER_TYPE_LIMIT,
                        quantity=0.006,
                        timeInForce=TIME_IN_FORCE_GTC,
                        price='2450',
                        )
print(order)

