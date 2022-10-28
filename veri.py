import urllib.request
import json
from urllib.parse import urljoin, urlencode
import requests as r
import pandas as pd
import talib.stream
import time
import hmac 
import hashlib
from passap import* 

BASE_URL = "https://fapi.binance.com/"



def testfonks():
    params={
        'symbol':'BTCUSDT', 'interval':'5m', 'limit':200, 'timestamp':timestamp()
    }
    query_string=urlencode(params)
    params['signature']=hmac.new(secretKey.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url = urljoin(BASE_URL, "fapi/v1/klines")
    payload={}
    headers={
        'Content-Type': 'application/json' ,
        'X-MBX-APIKEY': apiKey,
    }
    response = r.request("GET", url, headers=headers, params=params).json()
    return response

def positionInformation():
    params={
        'symbol':'BTCUSDT', 'timestamp':timestamp(), 
    }
    query_string=urlencode(params)
    params['signature']=hmac.new(secretKey.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url=urljoin(BASE_URL, "/fapi/v2/positionRisk")
    payload={}
    headers={
        'Content-Type': 'application/json' ,
        'X-MBX-APIKEY': apiKey,
    }
    response = r.request("GET", url, headers=headers, params=params).json()
    data=pd.DataFrame(response)
    return data



def leverage():
    params={
        'symbol':'BTCUSDT', 'leverage':'50', 'timestamp':timestamp()
    }
    query_string=urlencode(params)
    params['signature']=hmac.new(secretKey.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url=urljoin(BASE_URL, "/fapi/v1/leverage")
    payload={}
    headers={
        'Content-Type': 'application/json' ,
        'X-MBX-APIKEY': apiKey,
    }
    response = r.request("POST", url, headers=headers, params=params).json()
    return response

def emirGonder():
    params={
        'symbol':'BTCUSDT', 'side':'BUY', 'type':'MARKET',  'quantity':'0.08', 'workingType':'CONTRACT_PRICE', 'timestamp':timestamp(), 'positionSide':'BOTH'
    }
    query_string=urlencode(params)
    params['signature']=hmac.new(secretKey.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url=urljoin(BASE_URL, "/fapi/v1/order")
    payload={}
    headers={
        'Content-Type': 'application/json' ,
        'X-MBX-APIKEY': apiKey,
    }
    response = r.request("POST", url, headers=headers, params=params).json()
    return response

def marginType():
    params={
        'symbol':'BTCUSDT', 'marginType':'CROSS', 'timestamp':timestamp()
    }
    query_string=urlencode(params)
    params['signature']=hmac.new(secretKey.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    url=urljoin(BASE_URL, "/fapi/v1/marginType")
    payload={}
    headers={
        'Content-Type': 'application/json' ,
        'X-MBX-APIKEY': apiKey,
    }
    response = r.request("POST", url, headers=headers, params=params).json()
    return response



def get_all_symbols():
    response = urllib.request.urlopen(f"{BASE_URL}fapi/v1/exchangeInfo").read()
    return list(map(lambda symbol: symbol['symbol'], json.loads(response)['symbols']))


def get_data_symbols(symbol_name, period, limit):
    params = {
         'symbol': symbol_name, 'interval': period, 'limit': limit
    }
    query_string = urlencode(params)
    url = urljoin(BASE_URL, "fapi/v1/klines")
    payload = {}
    headers = {
        'Content-Type': 'application/json'
    }
    response = r.request('GET', url, headers=headers, params=params).json()
    converted = pd.DataFrame(response, columns=["open time", "open", "high", "low", "close", "volume", "closeTime", "asset-volume", "numberTrades", "baseassetvol", "quoteassetvol", "ignores"])
    return converted



def get_buy_sell_volume(symbol_name, period , limit):

    params = {
         'symbol':symbol_name, 'period': period , 'limit':limit, 
    }
    query_string = urlencode(params)
    url = urljoin(BASE_URL, "futures/data/takerlongshortRatio")
    payload = {}
    headers = {
    'Content-Type': 'application/json'
    }
    response = r.request('GET', url, headers=headers, params=params).json()
    converted=pd.DataFrame(response)
    return converted

def timestamp():
    return int(time.time()*1000)

print(timestamp())


a=get_buy_sell_volume('BTCUSDT', '5m', 100)
print(a)

"""l1=200
btc_data = get_data_symbols('BTCUSDT', '1m', 'l1')
open_btc = btc_data['open']
close_btc = btc_data['close']

print(open_btc)
print(close_btc)

rsi_btc = talib.RSI(close_btc,14)
print(rsi_btc[len(rsi_btc)-1])

sma_btc = talib.SMA(close_btc,50)
print(sma_btc[len(sma_btc)-1])"""