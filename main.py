# -*- coding: cp1251 -*-
from yandexpics import YandexImagesSearch
import os

# --------- SETTINGS --------------
WORD = 'Ваз 2101'
PAGES = 10
PATH = 'Image'

load_pics = YandexImagesSearch(WORD, PAGES, PATH)
load_pics.do_search()

files = os.listdir(f"{PATH}/{WORD}")
for x in files:
    if x.endswith(".jpg"):
        print(x)



