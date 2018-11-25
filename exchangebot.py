import configparser
import time

import requests
import telegram


import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def main():
    bot = telegram.Bot('709901502:AAH1jqkKhh9qfmOAekjx0ckm2s61fPJGAuo')
    while True:
        msg = []
        response = requests.get('https://api.bitqi.com/api/po/MarketData/GetMarketPrices')
        res = response.json()
        for r in res:
            msg.append(r['marketName'] + " " + str(r['price']) + "\n")
        bot.sendMessage(chat_id='@test123', text="".join(msg))
        time.sleep(10)



main()