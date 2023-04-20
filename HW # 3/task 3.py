#  Создайте скрипт бота, который находит ответы
# на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза
# ему неизвестна, он выводит соответствующую фразу.

data = open("text.txt", encoding='utf-8')
text = data.readlines()
print(text)
data.close()

phrase = text[0].split(' : ')
bot = {}
bot[phrase[0]] = phrase[1]
print(bot)
q = input()
print(bot[q])