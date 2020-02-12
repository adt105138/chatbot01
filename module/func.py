from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

import requests
import twder  #匯率套件

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


currencies = {'美金':'USD','美元':'USD','港幣':'HKD','英鎊':'GBP','澳幣':'AUD','加拿大幣':'CAD',\
              '加幣':'CAD','新加坡幣':'SGD','新幣':'SGD','瑞士法郎':'CHF','瑞郎':'CHF','日圓':'JPY',\
              '日幣':'JPY','南非幣':'ZAR','瑞典幣':'SEK','紐元':'NZD','紐幣':'NZD','泰幣':'THB',\
              '泰銖':'THB','菲國比索':'PHP','菲律賓幣':'PHP','印尼幣':'IDR','歐元':'EUR','韓元':'KRW',\
              '韓幣':'KRW','越南盾':'VND','越南幣':'VND','馬來幣':'MYR','人民幣':'CNY' }  #幣別字典
keys = currencies.keys()

def sendTextJ(event):  #傳送文字
    try:
        money = '日幣'
        if not money == '':  #匯率類幣別存在
                if money in keys:
                    rate = float(twder.now(currencies[money])[3])  #由匯率套件取得匯率
                    message = money + '的匯率為 ' + str(rate)
                    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendTextA(event):  #傳送文字
    try:
        message = TextSendMessage( text = "我是美元，\n幫你查！" )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def sendTextC(event):  #傳送文字
    try:
        message = TextSendMessage(  
            text = "親親您好，\n這就幫您查人民幣！"
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

