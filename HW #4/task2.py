# В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»
spis_1 = set("«Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»".split())
spis_2 = set("«Сливочное», «Вафелька», «Сладкоежка»".split())

lIst = spis_1.difference(spis_2)
print(f"Закончилась {lIst}")