import telebot
import wikipedia


print(bot.get_me())

def log(message, answer):
    print('\n ==========')
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/start', '/stop')
    user_markup.row('Поиск картинки', 'Поиск информации')
    answer = 'Привет мой сладенький синнабон,что тебя волнует?'
    log(message,answer)
    bot.send_message(message.chat.id, answer, reply_markup=user_markup)
@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Ну да, пошёл я нахер(", reply_markup=hide_markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Поиск информации':
        bot.send_message(message.chat.id, 'Введите что бы вы хотели узнать')
    else:
        try:
            wikipedia.set_lang('ru')
            bot.reply_to(message, wikipedia.summary(message.text.lower()))
        except:
            bot.reply_to(message, "Кто этот ваш", message.text.lower() ,'нахуй')

bot.polling(none_stop=True)