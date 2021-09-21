import requests
from bs4 import *

from work_with_sql import examination


class VkBot:
    def __init__(self, user_id):
        self._USER_ID = user_id
        self._NICKNAME = self.take_nickname()
        self._NAME = self.take_name()
        self._SURENAME = self.take_surename()
        self.COMMANDS = ['!help', '!weather', '!notebook', '!quiz']

    def take_nickname(self):
        request = requests.get('https://vk.com/id' + str(self._USER_ID))
        soup = BeautifulSoup(request.text, 'lxml')
        nick = soup.find('title').text

        return nick.replace(' | ВКонтакте', '')

    def take_name(self):
        nick = self.take_nickname()
        name = nick.split()[0]
        return name

    def take_surename(self):
        nick = self.take_nickname()
        surename = nick.split()[0]
        return surename

    @property
    def USER_ID(self):
        return self._USER_ID

    @property
    def NICKNAME(self):
        return self._NICKNAME
