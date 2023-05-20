# -*- coding: utf-8 -*-

from yandexpics import YandexImagesSearch
import time

# --------- SETTINGS --------------
PAGES = 10
PATH = 'Image'
QUERYLIST = 'data.txt'

file = open(QUERYLIST, mode='r', encoding='utf-8')
lines = file.readlines()
print(f'Считываю файл: {QUERYLIST}')
for line in lines:
    line = line[:-3]
    print(f'Выполняем поиск по запросу: {line}')
    load_pics = YandexImagesSearch(line, PAGES, PATH)
    load_pics.do_search()
    print('Включение задержки выполнения скрипта')
    time.sleep(120)
    print('Отключение задержки выполнения скрипта')




#files = os.listdir(f"{PATH}/{WORD}")
#for x in files:
#    if x.endswith(".jpg"):
#        print(x)





