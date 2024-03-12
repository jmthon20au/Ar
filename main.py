import requests
import telebot
from telebot import types

token = "6894757333:AAGpsI_QdLqvhMZdPNjY1-PUDOMdIEZpmAg"
bot = telebot.TeleBot(token)
#تذكر مصدري قناتي @Crrazy_8
#برمجة @BRoK8
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://www.7koko.com',
    'Referer': 'http://www.7koko.com/apps/tashkil/index.php',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}

@bot.message_handler(commands=['start'])
def welcome(message):
	name = message.from_user.first_name
	btn = types.InlineKeyboardButton('قناة التحديثات',url='t.me/my00002')
	btn1 = types.InlineKeyboardButton('مطور البوت',url='t.me/altaee_z')
	xx = types.InlineKeyboardMarkup()
	xx.add(btn , btn1)
	bot.reply_to(message,f"""
مرحبا بك {name}🌹✨
~انا بوت اقوم بتشكيل الكلمات باللغة العربية 〽️
🔰ارسل النص الان والانتظر بضع ثواني"""
	
	,reply_markup=xx)

@bot.message_handler(func=lambda m:True)
def ar(message):
	msg = message.text
	data = f'textArabic={msg} .'.encode()
	url = requests.post('http://www.7koko.com/api/tashkil/index.php', headers=headers, data=data, verify=False).text
	bot.reply_to(message,url)
	
print('اشتغل البوت 👀✨')
bot.infinity_polling()
