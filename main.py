import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

from VkBot import VkBot
from work_with_sql import examination, take_all_users_id
from wtr import weather, peek_cities, forecast


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': get_random_id()})


token = "0c260bce9d17f0258eda9914371bcbdfc29fa56250defbd46807fc2239084f826e4e6c2654fbe6928cc18"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

autorization = False
print("Server started")
users_ids = take_all_users_id()
wanna_peek_weather = False
frcst = False
citis = []
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            user = VkBot(event.user_id)
            if event.user_id not in users_ids:
                write_msg(event.user_id, 'Что-то я вас не узнаю...')
                write_msg(event.user_id, 'Подождите пару секунд...')
                examination(event.user_id, user.take_nickname())
                write_msg(event.user_id, '🎉Авторизация прошла успешно!🎉')
                users_ids.append(event.user_id)
                write_msg(event.user_id, f'Рад тебя видеть! {user.take_name()}\n'
                                         f'Для того, что бы посмотреть список команд, напиши боту "!help"')
            elif event.text.lower() == '!help' or event.text.lower() == '!рудз':
                write_msg(event.user_id, f'Пока что я могу выполнять такие команды:\n'
                                         f'!help ——————— отображение доступных команд(если вы видите этот'
                                         f' текст, думаю вы это уже поняли)\n\n'
                                         f'!weather ————— посмотри погоду в своём городе'
                                         f' на сегодня, или на другие дни\n\n'
                                         f'!notebook ———— записная книжка внутри ВК, в ней'
                                         f' ты можешь записать задания, о которых ты боишься забыть'
                                         f', а я тебе о них вовремя напомню\n\n'
                                         f'!quiz ——————— я дам тебе вопрос, правильно ответив на который,'
                                         f' ты сможешь подняться в таблице лидеров, и похвастаться этим перед'
                                         f' друзьями')

            elif event.text.lower().split()[0] == '!weather':
                city = event.text.lower().split()[1]
                a = peek_cities(city)
                b = []
                if len(a) > 0:
                    for i in range(len(a)):
                        b.append(f'{a[i][0]}. {a[i][1]} ({a[i][2]})')
                    b = '\n'.join(b)
                    write_msg(event.user_id, f'Какой город вы имели ввиду?\n'
                                             f'{b}')
                    wanna_peek_weather = True
                    citis = a

            elif wanna_peek_weather:
                try:
                    number = int(event.text) - 1
                except ValueError:
                    write_msg(event.user_id, 'Кажется вы неправильно ввели запрос, повторите его снова')
                city = citis[number][-1]
                a = weather(city)
                if a == 'bad_query':
                    write_msg(event.user_id, 'Кажется вы неправильно ввели запрос, повторите его снова')
                else:
                    precipitation = ''

                    if a[4].lower() == 'clouds':
                        precipitation = "Облачно"

                    if a[4].lower() == 'rain':
                        precipitation = "Дождь"

                    if a[4].lower() == 'clear':
                        precipitation = "Чистое небо"

                    print(a[4].lower())

                    write_msg(event.user_id, f'Температура {a[0]}°C\n'
                                             f'Влажность: {a[1]}%\n'
                                             f'Скорость ветра: {a[2]}m/s\n'
                                             f'Давление: {a[3]}hPa\n'
                                             f'{precipitation}')
                    wanna_peek_weather = False

            elif event.text.lower().split()[0] == '!forecast':
                city = event.text.lower().split()[1]
                a = peek_cities(city)
                b = []
                if len(a) > 0:
                    for i in range(len(a)):
                        b.append(f'{a[i][0]}. {a[i][1]} ({a[i][2]})')
                    b = '\n'.join(b)
                    write_msg(event.user_id, f'Какой город вы имели ввиду?\n'
                                             f'{b}')
                    frcst = True
                    citis = a

            elif frcst:
                try:
                    number = int(event.text) - 1
                except ValueError:
                    write_msg(event.user_id, 'Кажется вы неправильно ввели запрос, повторите его снова')
                city_id = citis[number][-1]
                a = forecast(city_id)
                for i in range(len(a)):
                    a[i] = ' '.join(a[i])
                write_msg(event.user_id, '\n'.join(a))
                frcst = False


            elif wanna_peek_weather:
                try:
                    number = int(event.text)
                except ValueError:
                    write_msg(event.user_id, 'Кажется вы неправильно ввели запрос, повторите его снова')
                city = citis[number][-1]
                a = weather(city)
                if a == 'bad_query':
                    write_msg(event.user_id, 'Кажется вы неправильно ввели запрос, повторите его снова')
                else:
                    write_msg(event.user_id, f'Температура {a[0]}°C\n'
                                             f'Влажность: {a[1]}%\n'
                                             f'Скорость ветра: {a[2]}m/s\n'
                                             f'Давление: {a[3]}hPa')
                wanna_peek_weather = False

            elif event.text not in user.COMMANDS:
                write_msg(event.user_id, f'Упс, кажется я не понимаю, что вы говорите...😬\n'
                                         f'Но думаю, если вы введёте одну из команд, я смогу вам помочь🧐\n'
                                         f'("!help" что бы посмотреть список команд)')
