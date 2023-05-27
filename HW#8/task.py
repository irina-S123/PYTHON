# Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.
import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=['ответ'])
def answer(message):
    print(message)
    data = open('requests_log.txt', mode='r', encoding='utf-8')
    log = data.readlines()
    print(log)
    choice = int(input('Выберите номер запроса: '))
    user_id = int(log[choice - 1].split(' -')[0])
    answer = input('Введите ответ на запрос: ')
    bot.send_message(user_id, answer)
bot.polling()