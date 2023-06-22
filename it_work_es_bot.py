import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, un gusto en poder ayudarte.")

@bot.message_handler(commands=['ofertas'])

def get_offer_scraping(message):
    work_list = []
    url = requests.get('https://www.tecnoempleo.com/ofertas-trabajo/?te=python') 
    soup = BeautifulSoup(url.content, 'html.parser')
    item_list = soup.find_all('div', {'class': 'p-2 border-bottom py-3 bg-white'})
    
    for item in item_list:
        work_list.append(item.text)
    
    # Dividir work_list en mensajes más pequeños
    chunk_size = 5
    chunks = [work_list[i:i + chunk_size] for i in range(0, len(work_list), chunk_size)]
    
    # Enviar cada mensaje al usuario
    for chunk in chunks:
        mensaje = '\n'.join(chunk)
        bot.reply_to(message, mensaje)

bot.infinity_polling()
