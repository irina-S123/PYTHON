# Добавьте в telegram-бота игру «Угадай числа». 
# Бот загадывает число от 1 до 1000. Когда игрок угадывает его, 
# бот выводит количество сделанных ходов.
import telebot
import random

bot = telebot.TeleBot("")

count = 1
question = random.randint(1, 1000)

@bot.message_handler(commands=['game'])
def numbers_game(message):    
    bot.send_message(message.from_user.id, "Отгадайте число от 1 до 1000")    
    @bot.message_handler(content_types=['text'])
    def game(message):
        user_number = int(message.text)
        global count
        if question > user_number:
            bot.send_message(message.from_user.id, "Мало")
            count += 1
        elif question < user_number:
            bot.send_message(message.from_user.id, "Много")
            count += 1
        else:
            bot.reply_to(message, f"Победа за {count} попыток")

@bot.message_handler(commands=['restart'])
def game_restart(message):
    global question, count
    question = random.randint(1, 1000)
    count = 1
    bot.send_message(message.from_user.id, "Можно начать заново")

         

bot.polling()