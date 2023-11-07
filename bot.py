import telebot
from openai import OpenAI
import re
import os
import time
import requests
import random
import time
import json
import urllib
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
from datetime import datetime
from conf.varsg import FTLIST, CDLIST,DRPG
from telebot import types


#TYPES É O SISTEMA DO TELEBOT 
bot = telebot.TeleBot("") #ID do bot do telegram
start_sequence = "\nIA:"
restart_sequence = "\nHumano:"
lockKey = False
olaM = "oi","oi!", "opa","opa!", "viva","viva!", "fala" , "fala!","eae","eae!","eai","eai!","ola","ola!","olá","olá!"
botName = bot.get_me().first_name
TheOneToken = ""#Chave API para o Api do Senhor dos Aneis
openai.api_key = "" #Chave API para o OpenAI


def generate_response(prompt):
  completions = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.98,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    )

  message = completions.choices[0].text
  return message

@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user.first_name
    chat_id =message.chat.id
    response_message = "Olá,"+user+". Eu sou o "+botName+" 2.0, uma versão melhorada de meu antecessor! Aproveite!"
    bot.send_message(chat_id, response_message)

def get_pessoas():
    p = requests.get('http://api.open-notify.org/astros.json').json()
    pessoas = p['people']
    for pe in pessoas:
        pes = print(pe)

@bot.message_handler(commands=['iss'])
def iss(message):
    #o r[''] serve para pegar o conteudo dentro do json ou de qualquer outro modelo 
    chat_id = message.chat.id 
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    p = requests.get('http://api.open-notify.org/astros.json').json()
    h = requests.get('http://worldtimeapi.org/api/timezone/ETC/UTC').json()   
    nPessoas = p['number']
    pessoas = p['people']
    latitude = r['iss_position']['latitude']
    longitude = r['iss_position']['longitude']
    horarioC = r['timestamp']
    horarioISS = h['datetime']
    dt_horarioC = datetime.fromtimestamp(horarioC)
    bot.send_message(chat_id,text= "A Posição atual da ISS[Internacional Space Station] é: \n[Latitude]= "+latitude+" "
    +"\n[Longitude]= "+longitude+"\nTempo do Cliente: "+str(dt_horarioC)+"\nTempo na ISS(UTC): "+str(horarioISS)+
    "\nPessoas a bordo da ISS: "+str(nPessoas))
    bot.send_message(chat_id,text="-----------Nome dos Tripulantes e suas Naves-------------")
    for pe in pessoas:
        bot.send_message(chat_id,text="Nome: "+pe['name']+" // Nave Atual: "+pe['craft'])
    bot.send_message(chat_id,text="--Localização Geográfica Visual da ISS em relação à Terra (para ver melhor reduza o zoom do mapa)--")  
    bot.send_location(chat_id=chat_id, latitude=latitude,longitude=longitude)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@bot.message_handler(commands=['meme'])
def meme(message):
   chat_id = message.chat.id
   m = requests.get('https://api.imgflip.com/get_memes').json()
   meme = m['data']['memes']
   for mems in meme:
    bot.send_photo(chat_id,photo=mems['url'],caption=mems['name'])

@bot.message_handler(commands=['lotr'])
def lotr(message):
    chat_id = message.chat.id
    req = requests.get("https://the-one-api.herokuapp.com/v1/book").json()
    l = req['docs']
    telebot.types.InlineKeyboardButton('')
    for lords in l :
        telebot.types.InlineKeyboardButton(text=lords['name'],callback_data=lords['_id'])



@bot.message_handler(commands=['doggo'])
def doggo(photo):
    url = get_image_url()
    chatid = photo.chat.id
    bot.send_photo(chat_id=chatid, photo=url)
    

@bot.message_handler(commands=['curiosidades'])
def curiosidades(message):
    cdList = CDLIST
    rp_message = random.choice(cdList)
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id,text=rp_message) 

@bot.message_handler(commands=['dicasrpg'])
def dicasrpg(message):
    dRpg = DRPG
    rp_message = random.choice(dRpg)
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id,text=rp_message) 


@bot.message_handler(commands=['future'])
def future (message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Qual será meu futuro?')
    bot.send_message(chat_id, "Clique no botão e eu lhe mostrarei até onde vai a toca do coelho", reply_markup=keyboard)


@bot.message_handler(commands=['ia'])
def ask(message):
    client = OpenAI()
    chat_id = message.chat.id
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
  
    bot.send_message(chat_id=chat_id,text=response.strip())
  # Send the response back to the user


bot.polling(interval=1)