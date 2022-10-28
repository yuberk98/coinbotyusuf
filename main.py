from tradingview_ta import TA_Handler, Interval, Exchange
from veri import *
import time


"""marginType()
time.sleep(2)
leverage()
time.sleep(2)
emirGonder()"""
info=print(positionInformation())
pnl=info["unRealizedProfit"]
print("Realize Edilmemiş Kar (PNL):", pnl[0])
liquidationPrice=info['liquidationPrice'][0]
print("Likidasyon:", liquidationPrice)