from twstock import stock
import twstock
import mail
from twstock.codes import __update_codes



def higher_than_2382_5ma():
    code='2382'
    days=5
    stock = twstock.Stock(code)                      
    realtime_stock=twstock.realtime.get(code)
    if realtime_stock['success'] == True:
        today = realtime_stock['info']['time']
        today_price = float(realtime_stock['realtime']['latest_trade_price'])     
        ma_price_as_of_yesterday = stock.moving_average(stock.price, days)[1]
        if today_price > ma_price_as_of_yesterday:
            msg="[%s] %s Price: %.2f is higher than %d-MA: %.2f"%(code, today, today_price, days, ma_price_as_of_yesterday)
            mail.Mail().send(msg)

def higher_than_2382_10ma():
    code='2382'
    days=10
    stock = twstock.Stock(code)                      
    realtime_stock=twstock.realtime.get(code)
    if realtime_stock['success'] == True:
        today = realtime_stock['info']['time']
        today_price = float(realtime_stock['realtime']['latest_trade_price'])     
        ma_price_as_of_yesterday = stock.moving_average(stock.price, days)[1]
        if today_price > ma_price_as_of_yesterday:
            msg="[%s] %s Price: %.2f is higher than %d-MA: %.2f"%(code, today, today_price, days, ma_price_as_of_yesterday)
            mail.Mail().send(msg)

def higher_than_2382_20ma():
    code='2382'
    days=20
    stock = twstock.Stock(code)                      
    realtime_stock=twstock.realtime.get(code)
    if realtime_stock['success'] == True:
        today = realtime_stock['info']['time']
        today_price = float(realtime_stock['realtime']['latest_trade_price'])     
        ma_price_as_of_yesterday = stock.moving_average(stock.price, days)[1]
        if today_price > ma_price_as_of_yesterday:
            msg="[%s] %s Price: %.2f is higher than %d-MA: %.2f"%(code, today, today_price, days, ma_price_as_of_yesterday)
            mail.Mail().send(msg)

def higher_than_6005_5ma():
    code='6005'
    days=5
    stock = twstock.Stock(code)                      
    realtime_stock=twstock.realtime.get(code)
    if realtime_stock['success'] == True:
        today = realtime_stock['info']['time']
        today_price = float(realtime_stock['realtime']['latest_trade_price'])     
        ma_price_as_of_yesterday = stock.moving_average(stock.price, days)[1]
        if today_price > ma_price_as_of_yesterday:
            msg="[%s] %s Price: %.2f is higher than %d-MA: %.2f"%(code, today, today_price, days, ma_price_as_of_yesterday)
            mail.Mail().send(msg)

def higher_than_6005_10ma():
    code='6005'
    days=10
    stock = twstock.Stock(code)                      
    realtime_stock=twstock.realtime.get(code)
    if realtime_stock['success'] == True:
        today = realtime_stock['info']['time']
        today_price = float(realtime_stock['realtime']['latest_trade_price'])     
        ma_price_as_of_yesterday = stock.moving_average(stock.price, days)[1]
        if today_price > ma_price_as_of_yesterday:
            msg="[%s] %s Price: %.2f is higher than %d-MA: %.2f"%(code, today, today_price, days, ma_price_as_of_yesterday)
            mail.Mail().send(msg)

def higher_than_6005_20ma():
    code='6005'
    days=20
    stock = twstock.Stock(code)                      
    realtime_stock=twstock.realtime.get(code)
    if realtime_stock['success'] == True:
        today = realtime_stock['info']['time']
        today_price = float(realtime_stock['realtime']['latest_trade_price'])     
        ma_price_as_of_yesterday = stock.moving_average(stock.price, days)[1]
        if today_price > ma_price_as_of_yesterday:
            msg="[%s] %s Price: %.2f is higher than %d-MA: %.2f"%(code, today, today_price, days, ma_price_as_of_yesterday)
            mail.Mail().send(msg)

__update_codes()
higher_than_2382_5ma()
higher_than_2382_10ma()
higher_than_2382_20ma()
higher_than_6005_5ma()
higher_than_6005_10ma()
higher_than_6005_20ma()
