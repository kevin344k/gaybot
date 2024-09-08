import telebot 
from telebot import types

TOKEN= '6409249656:AAEJM_E-6kgT6ZW0turdfOpx0KnBMjiIZZM'
bot=telebot.TeleBot(TOKEN)


#Creaciónb de comandos simples
@bot.message_handler(commands=['start'])
def send_welcome(message):
   # bot.reply_to(message,'Hola! Soy tu primer bot creado con Telebot')
  img_url='https://png.pngtree.com/thumb_back/fh260/background/20221003/pngtree-sausage-nobody-grilled-fried-photo-image_9571358.jpg'
  bot.send_photo(chat_id=message.chat.id,photo=img_url,caption='$CHORIZOCOIN')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Puedes interactuar conmigo usando comandos. Por ahora, solo respondo a /start y /help')


#@bot.message_handler(func=lambda m:True)
#defecho_all(message):
#    bot.reply_to(message,message.text)



@bot.message_handler(commands=['pizza'])
def send_options(message):
        markup=types.InlineKeyboardMarkup(row_width=2)


        #creando botones para el bot

        btn_si=types.InlineKeyboardButton('Si',callback_data='pizza_si')
        btn_no=types.InlineKeyboardButton('No',callback_data='pizza_no')

        #agrega los botones
        markup.add(btn_si, btn_no)

        #Enviar mensaje con los botones
        bot.send_message(message.chat.id,"¿Te gusta la pizza?",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    if call.data == 'pizza_si':
         bot.answer_callback_query(call.id,'!A mi tambien!')
    elif call.data == 'pizza_no':
         bot.answer_callback_query(call.id,'!Bueno, vcada uno tiene sus gustos!')     


@bot.message_handler(commands=['foto'])
def send_image(message):
     img_url='https://s3-us-west-2.amazonaws.com/devcodepro/media/blog/por-que-aprender-python.png'
     bot.send_photo(chat_id=message.chat.id,photo=img_url,caption='Aqui tienes tu imagen')


if __name__ == "__main__":
    bot.polling(none_stop=True)


