# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : sixBit                  #
# File Name             : handler.py              #
# ----------------------------------------------- #

import config as config
from telegram import Bot
from discord_webhook import DiscordWebhook
import tweepy
import smtplib, ssl
from email.mime.text import MIMEText

telegram = config.send_telegram_alerts
discord  = config.send_discord_alerts
twitter  = config.send_twitter_alerts
email    = config.send_email_alerts

if telegram:
    tg_bot = Bot(token=config.tg_token)

if twitter:
    tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
    tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
    tw_api = tweepy.API(tw_auth)
    
def send_buy_order(data):
    if telegram:
        tg_bot.sendMessage(config.channel, data)
    else:
        pass
        
    if discord:
        discord_alert = DiscordWebhook(url=config.discord_webhook, content=data)
        response = discord_alert.execute()
    else:
        pass
        
    if twitter:
        tw_api.update_status(status=data)
    else:
        pass
        
    if email:
        email_msg = MIMEText(data)
        email_msg['Subject'] = config.email_subject
        email_msg['From']    = config.email_sender
        email_msg['To']      = config.email_sender
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.email_host, config.email_port, context=context) as server:
            server.login(config.email_user, config.email_password)
            server.sendmail(config.email_sender, config.email_receivers, email_msg.as_string())
            server.quit()
    else:
        pass
  
def send_sell_order(data): 
    if telegram:
        tg_bot.sendMessage(config.channel, data)
    else:
        pass
        
    if discord:
        discord_alert = DiscordWebhook(url=config.discord_webhook, content=data)
        response = discord_alert.execute()
    else:
        pass
        
    if twitter:
        tw_api.update_status(status=data)
    else:
        pass
        
    if email:
        email_msg = MIMEText(data)
        email_msg['Subject'] = config.email_subject
        email_msg['From']    = config.email_sender
        email_msg['To']      = config.email_sender
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(config.email_host, config.email_port, context=context) as server:
            server.login(config.email_user, config.email_password)
            server.sendmail(config.email_sender, config.email_receivers, email_msg.as_string())
            server.quit()
    else:
        pass