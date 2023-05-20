from bs4 import BeautifulSoup
from fake_headers import Headers
import os, requests, json

class YandexImagesSearch:
    def __init__(self, search, num_pages, path):
        self.search = search
        self.num_pages = num_pages
        self.path = path
        self.pics_divs = []
        self.k = 0
        self.item = None
        self.clean = None

    def _print_ok(self):
        print(f'page {self.k} - {self.pics_divs.index(self.item)} OK')

    def _look_save_pics(self):
        try:
            pica = requests.get(self.clean, timeout=5)
        except Exception as e:
            print('----ERROR---', self.clean)
            return
        if pica.status_code == 200:
            pica = pica.content
            self.clean = self._clear_url(self.clean)
            with open(f'{self.path}/{self.search}/{self.clean[-22:]}', 'wb') as p:
                p.write(pica)
            self._print_ok()

    @staticmethod
    def _clear_url(uncleaned_url):
        bad_symbols = '/?:*"<>|\\'
        for sym in uncleaned_url:
            if sym in bad_symbols:
                uncleaned_url = uncleaned_url.replace(sym, '')
        return uncleaned_url

    def do_search(self):
        
        if os.path.isdir(f'{self.path}') == False:
            try:
                os.mkdir(f'{self.path}')
            except FileExistsError:
                pass

        if os.path.isdir(f'{self.path}/{self.search}') == False:
            try:
                os.mkdir(f'{self.path}/{self.search}')
            except FileExistsError:
                pass


        sess = requests.Session()
        sess.headers.update(Headers(os="win", browser="chrome", headers=True).generate())

        for self.k in range(self.num_pages):
            link = f'https://yandex.ru/images/search?from=tabbar&isize=large&text={self.search}&type=photo&p={self.k}'
            a = sess.get(link)
            soup = BeautifulSoup(a.text, 'html.parser')
            self.pics_divs = soup.find_all('div', class_='serp-item_type_search')

            for self.item in self.pics_divs:
                json_data = json.loads(self.item.get('data-bem'))
                try:
                    self.clean = json_data['serp-item']['preview'][0]['url']
                except KeyError:
                    continue
                if self.clean[-3:] in ['jpg', 'png', 'peg', 'gif', 'svg', 'ebp']:
                    self._look_save_pics()
                else:
                    try:
                        self.clean = json_data['serp-item']['preview'][0]['origin']['url']
                    except KeyError:
                        continue
                    if self.clean[-3:] in ['jpg', 'png', 'peg', 'gif', 'svg', 'ebp']:
                        self._look_save_pics()
                        
