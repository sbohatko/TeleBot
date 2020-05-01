import telebot
import wikipedia

bot = telebot.TeleBot("token")
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
    user_markup.row('💵 Donate', '🔎 Search')
    answer = 'Hi, i`m a Bot with searching API, you can find all information what you want 😉' \
             '\n\nSome commands:' \
             '\n/start' \
             '\n/search' \
             '\n/donate' \
             '\n/stop'
    log(message, answer)
    bot.send_message(message.chat.id, answer, reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    answer = "Ok,bye. 😔"
    bot.send_message(message.chat.id, answer, reply_markup=hide_markup)


@bot.message_handler(commands=['donate'])
def handle_text(message):
    answer = 'Here is my card for payments "5168 3212 3942 1239"'
    bot.send_message(message.chat.id, answer)
    bot.send_photo(message.chat.id, photo=open('cat.jpg', 'rb'), caption='thanks <3')


@bot.message_handler(commands=['search'])
def handle_search(message):
    message_text_list = message.text.lower().split()
    search_query = str(message_text_list[1])
    try:
        wikipedia.set_lang('ru')
        bot.reply_to(message.chat.id, wikipedia.summary(search_query))
    except wikipedia.HTTPTimeoutError:
        bot.reply_to(message.chat.id, "I cant find, {} 🤯".format(search_query))


bot.polling(none_stop=True)
