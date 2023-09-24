# from playwright.async_api import async_playwright
# from webdriver_manager.chrome import ChromeDriverManager

print('Господи, помилуй.')
print('Слава Тебе, Бог наш, Слава Тебе.')
print()
from bs4 import BeautifulSoup as bs
import requests, csv, json, os, sys, time, schedule, random
# from crontab import CronTab
from datetime import datetime
# import pandas as pd
import time
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text, BaseFilter,CommandStart
from aiogram.types import Message, ContentType, BotCommand,CallbackQuery
# import os, dotenv
from environs import Env
from selenium import webdriver
from selenium.webdriver.common.by import By
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import Config, load_config
from playwright.async_api import Playwright, async_playwright
# from playwright_stealth import stealth_async

config1= load_config()
BOT_TOKEN: str = config1.tg_bot.token
# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
# API_TOKEN: str = '5959145787:AAHKfsD3UgNhcXuY78EoV0tqE8ZNAn7lK6w'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Стартовать'),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/support',
                   description='Поддержка'),
        BotCommand(command='/contacts',
                   description='Другие способы связи'),
        BotCommand(command='/payments',
                   description='Платежи')]

    await bot.set_my_commands(main_menu_commands)


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Новости')
button_2: KeyboardButton = KeyboardButton(text='Объявления bs4')
button_3: KeyboardButton = KeyboardButton(text='Объявления sel')
button_4: KeyboardButton = KeyboardButton(text='Долгота')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1,button_2,button_3,button_4]],resize_keyboard=True,
                                    one_time_keyboard=True)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
# @dp.message(Text(text=['k','K','л','Л']))
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Что хотите посмотреть?',
                         reply_markup=keyboard)



# Список с ID администраторов бота. !!!Замените на ваш!!!
# admin_ids: list[int] = [1942504567]


# Собственный фильтр, проверяющий юзера на админа
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         # В качестве параметра фильтр принимает список с целыми числами
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
#
#
# # Этот хэндлер будет срабатывать, если апдейт от админа
# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     print(message.from_user.id)
#     await message.answer(text='Вы админ')



# Этот хэндлер будет срабатывать, при нажатии кнопки Долгота
@dp.message(Text(text='Долгота'))
async def dolgota(message: Message):
    await message.answer(text='Долгота')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36', }
    with open('dolgota.csv', 'w', encoding='utf-8') as file:
        m = csv.writer(file)  # ,delimiter=';')
        m.writerow(['Город', 'Восход', 'Заход', 'Долгота', 'Изменение', 'Сайт', ''])
        d = ['Прокопьевск', 'Удачный    ', 'Норильск   ', 'Воркута    ', '', '', '', '', '', '', '', '', '', '', '', '',
             '',
             '']
        kl='https://voshod-solnca.ru/sun/прокопьевск'
        sait = ['прокопьевск',
                'мурманск',
                'оленегорск',
                'удачный',
                'норильск',
                'воркута',
                'москва',
                'сочи',
                'певек',
                'пхукет',
                'дровяной',
                'мирный_(республика_саха_(якутия))']
        b = []
        n = []
        veter = []
        data = []
        p = 0
        await message.answer(text='1')
        for y in sait:
            response = requests.get(url=f'https://voshod-solnca.ru/sun/{y}', headers=headers)
            response.encoding = 'utf=8'
            soup = bs(response.text, 'html.parser')
            # h=[i.text for i in soup.find('span', class_='unit unit_temperature_c').find_all('div', class_='maxt')]
            gorod = soup.find('div', id='map-content-search').find('option').text
            vochod = soup.find('div', {'data-name': 'sunrise'}).text
            zahod = soup.find('div', {'data-name': 'sunset'}).text
            dolgota = soup.find('div', {'data-name': 'daytime'}).find('span').text
            ismen = soup.find('div', class_='table-scroll').find_all('td')[5].text
            m.writerow([gorod, vochod, zahod, dolgota, ismen, sait[p]])
            p+=1
            hg=[vochod,zahod,dolgota,ismen,gorod]
            await message.answer(text='   '.join(hg))
        # читаем файл.csv и создаем таблицу
        # chat_id = message.chat.id
        #
        # df = pd.read_csv('dolgota.csv')
        # await message.answer(text=df)
        # # создаем сообщение с таблицей
        # table_message = ''
        # for row in df.itertuples():
        #     table_message += ' | '.join(str(val) for val in row[1:]) + '\n'
        # # отправляем сообщение с таблицей
        #     await message.answer(text=table_message)
        # await bot.send_message(chat_id, table_message)


r=[]

@dp.message(Text(text=['з', 'З', 'p','P']))
async def zakrep(message: Message):
    await message.answer(text=r)

# Этот хэндлер будет срабатывать, при нажатии кнопки bs4
@dp.message(Text(text='Объявления bs4'))
async def vk_bs4(message: Message):
    await message.answer(text='Объявления')
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'Accept': '*/*'

    }

    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    await message.answer(text=k)
    response = requests.get(url='https://m.vk.com/jobprk', headers=headers)
    response.encoding = 'utf-8'
    soup = bs(response.text, 'html.parser')
    # print(soup.find('div',id="posts_container"))
    # print(soup.find_all('div', class_="pi_text"))
    # d = [i.text for i in soup.find_all('div', class_="pi_text")]
    d = []
    r=[]
    for u in soup.find_all('div', class_="wall_item"):
        o9=u.find('div', class_="wi_body").text
        o=len(u.find('div', class_="wi_body").text)
        o8=u.find('div', class_="pi_text")
        if u.find('span', class_="explain") != None:
            d.append('объявление закреплено')
            if u.find('div', class_="pi_text") == None:
                if u.find('img', class_='MediaGrid__imageSingle') != None:
                    print('картинка')
                    r.append(u.find('img', class_='MediaGrid__imageSingle')['src'])
                    continue
                print('фото')
                r.append(u.find('a', class_="MediaGrid__interactive")['href'])
                continue
            r.append(u.find('div', class_="pi_text").text)
            continue
        if u.find('div', class_="pi_text") == None:
            if u.find('img',class_='MediaGrid__imageSingle') !=None:
                print('картинка')
                d.append(u.find('img',class_='MediaGrid__imageSingle')['src'])
                continue
            print('фото')
            d.append(u.find('a', class_="MediaGrid__interactive")['href'])
            continue
        d.append(u.find('div', class_="pi_text").text)
    if len(d) == 0:
        await message.answer(text='Вас заблокировали')
    for j in d:
        if 'Показать ещё' in j:
            j = j.replace('Показать ещё', ' ')
        await message.answer(text=j)



# Этот хэндлер будет срабатывать, если апдейт придет кнопки  'Объявления sel' для парсера вк на селениуме

@dp.message(Text(text='Объявления sel'))
async def vk_selenium(message: Message):
    await message.answer(text='Объявления')
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
        'Accept': '*/*'

    }

    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    await message.answer(text=k)
    await message.answer(text='1')
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    g = random.randrange(100)
    options_chrome = webdriver.ChromeOptions()
    # options_chrome.add_extension('coordinates.crx')
    # zzz=options=options_chrome

    options_chrome.add_argument('--headless=chrome')
    await message.answer(text='2')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://m.vk.com/jobprk')
        d = []
        await message.answer(text='3')
        for g in browser.find_elements(By.CLASS_NAME, 'wall_item'):
            # await message.answer(text=g)
            # h = g.find_element(By.CLASS_NAME, 'pi_text')
            if g.find_elements(By.CLASS_NAME, 'pi_text'):
                d.append(g.find_element(By.CLASS_NAME, 'pi_text').text)
                continue
            else:
                if g.find_elements(By.CLASS_NAME, 'poster__text'):
                    d.append(g.find_element(By.CLASS_NAME, 'poster__text').text)
                    continue
                else:
                    d.append(g.find_element(By.CLASS_NAME, 'MediaGrid__interactive').get_attribute('href'))
                    continue

    await message.answer(text='5')
    for j in d:
        if 'Показать ещё' in j:
            j = j.replace('Показать ещё', '')
        await message.answer(text=j)

# Этот хэндлер будет срабатывать, если апдейт не от админа
v=[]   #  список ссылок новостей

# cookies = {
#             'KIykI': '1',
#             'tmr_lvid': '8577b70851cc9276af8a0e173298cf19',
#             'tmr_lvidTS': '1664015288689',
#             'Zen-User-Data': '{%22zen-theme%22:%22light%22}',
#             'tmr_detect': '1%7C1689937622793',
#             '_yasc': 'kH3Hhv5nYpZx6H6NAe5qVg0A6b0DWIk/cszl9je0h1uqMlsMN2DZpEst85haLg==',
#             '_ym_isad': '1',
#             'Session_id': 'noauth:1689937589',
#             'mda2_beacon': '1689937589064',
#             'sessar': '1.827.CiC3RAAWhaaTyc_yUbfXQV5F7qpHbrkNketqpeTYBCrInA.JoqApHx6z-VnogFDyxBqZR0JXzQRB6nlGAP_AMUGdAc',
#             'sso_status': 'sso.passport.yandex.ru:synchronized',
#             'yandex_login': '',
#             'yandexuid': '3150064901655672013',
#             'ys': 'c_chck.3683064152',
#             'zen_sso_checked': '1',
#             '_ym_d': '1687116993',
#             '_ym_uid': '1666960296819424637',
#             'addruid': 'C16j8a1P7O2ts4G8U3J5o1r30X',
#             'sso_checked': '1',
#             'zen_gid': '11291',
#         }

# cookies = {
#     "KIykI": "1",
#     "tmr_lvid": "8577b70851cc9276af8a0e173298cf19",
#     "tmr_lvidTS": "1664015288689",
#     "Zen-User-Data": '{"zen-theme":"light"}',
#     "tmr_detect": "1%7C1689937622793",
#     "_yasc": "kH3Hhv5nYpZx6H6NAe5qVg0A6b0DWIk/cszl9je0h1uqMlsMN2DZpEst85haLg==",
#     "_ym_isad": "1",
#     "Session_id": "noauth:1689937589",
#     "mda2_beacon": "1689937589064",
#     "sessar": "1.827.CiC3RAAWhaaTyc_yUbfXQV5F7qpHbrkNketqpeTYBCrInA.JoqApHx6z-VnogFDyxBqZR0JXzQRB6nlGAP_AMUGdAc",
#     "sso_status": "sso.passport.yandex.ru:synchronized",
#     "yandex_login": "",
#     "yandexuid": "3150064901655672013",
#     "ys": "c_chck.3683064152",
#     "zen_sso_checked": "1",
#     "_ym_d": "1687116993",
#     "_ym_uid": "1666960296819424637",
#     "addruid": "C16j8a1P7O2ts4G8U3J5o1r30X",
#     "sso_checked": "1",
#     "zen_gid": "11291"
# }


v=[]
@dp.message(Text(text='1'))
async def novost_1(message: Message):
    await message.answer(text=v[0])

@dp.message(Text(text='2'))
async def novost_2(message: Message):
    await message.answer(text=v[1])

@dp.message(Text(text='3'))
async def novost_3(message: Message):
    await message.answer(text=v[2])

@dp.message(Text(text='4'))
async def novost_4(message: Message):
    await message.answer(text=v[3])

@dp.message(Text(text='5'))
async def novost_5(message: Message):
    await message.answer(text=v[4])

@dp.message(Text(text='6'))
async def novost_1(message: Message):
    await message.answer(text=v[5])

@dp.message(Text(text='7'))
async def novost_2(message: Message):
    await message.answer(text=v[6])

@dp.message(Text(text='8'))
async def novost_3(message: Message):
    await message.answer(text=v[7])

@dp.message(Text(text='9'))
async def novost_4(message: Message):
    await message.answer(text=v[8])

@dp.message(Text(text='10'))
async def novost_5(message: Message):
    await message.answer(text=v[9])


@dp.message(Text(text='Новости1'))
async def novosti_playwright(message: Message):
    await message.answer(text='Новости')
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    # print(message.from_user.id)
    await message.answer(text=k)
    # proxy_server = 'http://195.216.135.182:8000'

    # print(message.from_user.id)
    # try:
    # proxy_host = '195.216.135.182'
    # proxy_port = '8000'
    # username = 'XvQx6z'
    # password = '8k8KKM'

    proxy_host = '168.81.59.128'
    proxy_port = '8000'
    username = 'RLdrq9'
    password = 'haRzKV'


    # proxy_server = {
    #     'server': f"http://{proxy_host}:{proxy_port}",
    #     'username': username,
    #     'password': password,
    # }
    async with async_playwright() as pw:
        rt=0
        y=cookies
        # context = await browser.new_context(cookies=cookie, proxy=proxy_server)

        # proxy_server = { "server": f"http://{username}:{password}@{proxy_host}:{proxy_port}" }

        proxy_server = {'server': f"http://{proxy_host}:{proxy_port}", 'username': username, 'password': password}
        await message.answer(text='выполняет строку browser = await pw.chromium.launch(headless=True)')
        # browser = await pw.chromium.launch(headless=False,proxy=proxy_server)
        browser = await pw.chromium.launch(headless=True)
        await message.answer(text='выполняет строку context = await browser.new_context()')
        context = await browser.new_context(proxy=proxy_server)
        await message.answer(text='выполняет строку page = await context.new_page()')
        page = await context.new_page()
        await context.add_cookies(y)


        # await stealth_async(page)
        await message.answer(text='заходит на страницу сайта')
        # await message.answer(text='начался time.sleep')
        # time.sleep(100)
        # await message.answer(text='закончился time.sleep')
        # response = await page.goto("https://dzen.ru/?clid=1946579&win=90&yredirect=true&utm_referer=sso.dzen.ru")
        # response = await page.goto("https://dzen.ru/?yredirect=true")
        # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot.png')
        response = await page.goto("http://dzen.ru")
        # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot1.png')
        # response = await page.goto("https://stepik.org/lesson/716118/step/4?unit=716910")
        # response = await page.goto("https://google.com")
        if response.status == 200:
            await message.answer(text='200')
            # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot2.png')

        else:
            await message.answer(text='не 200')
        await message.answer(text="выполняет строку checkbox = page.locator('.card-news__stories-Bu')")
        checkbox = page.locator('.card-news__stories-Bu')
        await message.answer(text='выполняет строку checkbox_texts = await checkbox.all_inner_texts()')
        checkbox_texts = await checkbox.all_inner_texts()
        # checkbox_texts = [await kl.get_attribute('aria-label') for kl in (await checkbox.locator('span').all())]
        if checkbox_texts:
            await message.answer(text='выполняет строку await message.answer(text=checkbox_texts[0])')
            await message.answer(text=checkbox_texts[0])
        else:
            await message.answer(text='checkbox_texts пустой')
        v.clear()  # делает список пустым
        print()
        # await message.answer(text=checkbox_texts[0])
        n = [await k.get_attribute('href') for k in (await checkbox.locator('a').all())]

        await message.answer(text="выполняет строку d=checkbox_texts[0].split('\n')")
        d=checkbox_texts[0].split('\n')
        await message.answer(text='выполняет цикл ')
        for i,y in zip(d,n):
            await message.answer(text=i)
            v.append(y)

            # v.clear()   #  делает список пустым
            # g = [i.strip() for i in checkbox.text.split('\n')]   #  список заголовков новостей
            # n = [k.get_attribute('href') for k in checkbox.find_elements(By.TAG_NAME, 'a')]   #  список ссылок новостей
            # for y, u in zip(g, n):
            #     # print(y, u)
            #     v.append(u)   #  добавляет ссылки в список
            #     # await message.answer(text=u)
            #     await message.answer(text=y)
    # except:
    #     await message.answer(text='Что то пошло не так')
    #     print('Что то пошло не так')

@dp.message(Text(text='Новости'))
async def novosti_requests(message: Message):
    await message.answer(text='Новости')
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    # print(message.from_user.id)
    await message.answer(text=k)
    # proxy_server = 'http://195.216.135.182:8000'

    # print(message.from_user.id)
    # try:
    # proxy_host = '195.216.135.182'
    # proxy_port = '8000'
    # username = 'XvQx6z'
    # password = '8k8KKM'

    proxy_host = '168.81.59.128'
    proxy_port = '8000'
    username = 'RLdrq9'
    password = 'haRzKV'


    # proxy_server = {
    #     'server': f"http://{proxy_host}:{proxy_port}",
    #     'username': username,
    #     'password': password,
    # }

    rt=0
    # y=cookies
    # context = await browser.new_context(cookies=cookie, proxy=proxy_server)

    # proxy_server = { "server": f"http://{username}:{password}@{proxy_host}:{proxy_port}" }

    proxy_server = {'server': f"http://{proxy_host}:{proxy_port}", 'username': username, 'password': password}
    cookies = {
        'yandex_login': '',
        'yandexuid': '7986167821683047642',
        '_ym_uid': '1686945243823701731',
        '_ym_d': '1686945243',
        'tmr_lvid': '6dfaf88cc5fc7a63da810b3638975cea',
        'tmr_lvidTS': '1686945243391',
        'vid': '873af10575d61ad3',
        'zen_gid': '11291',
        'KIykI': '1',
        'addruid': 'n16R9TX4T96GB46RQ73l0Gk8r0',
        'crookie': 'vg6vCy2sSLN3IguJi3hebBUryljWqn3XikbJgbKXylrP2zjdkjWZabI07McqbDa6pDmKVcxGxpvfpteJnjH/gW7Jg/4=',
        'cmtchd': 'MTY5NTA1Mzc5ODU3OQ==',
        'zen_sso_checked': '1',
        'Session_id': 'noauth:1695491008',
        'sessar': '1.1182.CiCTtdFAQ4KxcrqqRuU5OfTxPEx2NxOTPS0JmyNRfcUDHw.m6l8ornGoaYDXpT0QK4hRDMmGFMHEjuGMq-Io0ayrM8',
        'ys': 'c_chck.1308660127',
        'mda2_beacon': '1695491008335',
        '_ym_isad': '1',
        'Zen-User-Data': '{%22zen-theme%22:%22light%22}',
        'ask_city': '+',
        'tmr_detect': '1%7C1695496006520',
        '_yasc': '0UuriHacVByJsdceSZ4O1Y++vvsW7Vmfv+MBQs80sAa1WxFv8oiPTbmOXzFbXBxdKiZkYQ==',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'yandex_login=; yandexuid=7986167821683047642; _ym_uid=1686945243823701731; _ym_d=1686945243; tmr_lvid=6dfaf88cc5fc7a63da810b3638975cea; tmr_lvidTS=1686945243391; vid=873af10575d61ad3; zen_gid=11291; KIykI=1; addruid=n16R9TX4T96GB46RQ73l0Gk8r0; crookie=vg6vCy2sSLN3IguJi3hebBUryljWqn3XikbJgbKXylrP2zjdkjWZabI07McqbDa6pDmKVcxGxpvfpteJnjH/gW7Jg/4=; cmtchd=MTY5NTA1Mzc5ODU3OQ==; zen_sso_checked=1; Session_id=noauth:1695491008; sessar=1.1182.CiCTtdFAQ4KxcrqqRuU5OfTxPEx2NxOTPS0JmyNRfcUDHw.m6l8ornGoaYDXpT0QK4hRDMmGFMHEjuGMq-Io0ayrM8; ys=c_chck.1308660127; mda2_beacon=1695491008335; _ym_isad=1; Zen-User-Data={%22zen-theme%22:%22light%22}; ask_city=+; tmr_detect=1%7C1695496006520; _yasc=0UuriHacVByJsdceSZ4O1Y++vvsW7Vmfv+MBQs80sAa1WxFv8oiPTbmOXzFbXBxdKiZkYQ==',
        'Referer': 'https://m.dzen.ru/news/story/RIA_Novosti_razvedchiki_unichtozhili_tank_Leopard_sehkipazhem_armii_FRG--a161111dcc1f1326047292a0c367568d?lang=ru&from=main_portal&fan=1&stid=STEwBuJff9DUvftYhaMr&t=1695493665&persistent_id=4666199950789852023&tst=1695494051&story=37ca3162-a963-5720-91c2-510fa300c030&issue_tld=ru&contour=exp0&utm_referrer=m.dzen.ru',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }
    # e=[<ul class="card-news__stories-Bu"><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Uchyonye_ishhut_sposob_vskryt_grobnicu_khozyaina_Terrakotovoj_armii--5ef93b379aa0a821108feea31132f175?lang=ru&amp;from=main_portal&amp;fan=1&amp;stid=pr0UXHCBOmnLrxfU_Lr0&amp;t=1695544607&amp;persistent_id=4666199950789887976&amp;tst=1695545006&amp;story=2041990d-9958-5828-a16a-9c601b4baa72&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/28627/254083361-1516267195536-square/logo-square)" title="RT на русском"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Учёные ищут способ вскрыть гробницу хозяина Терракотовой армии</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Gubernator_Starovojt_Bespilotnik_atakoval_zdanie_vcentre_Kurska--97c9f6c9bf36c53942633bbcfcee137e?lang=ru&amp;from=main_portal&amp;fan=1&amp;stid=D9wvSOaXBSlwQkqG8Q-t&amp;t=1695544607&amp;persistent_id=4666199950789889571&amp;tst=1695545006&amp;story=6a10adb2-e989-5816-b065-0bdeb4d1906a&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/26056/1116-1478692904205-square/logo-square)" title="Российская газета"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Губернатор Старовойт: Беспилотник атаковал здание в центре Курска</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/RIA_Novosti_razvedchiki_unichtozhili_tank_Leopard_sehkipazhem_armii_FRG--a161111dcc1f1326047292a0c367568d?lang=ru&amp;from=main_portal&amp;fan=1&amp;stid=BuJfSTEwZ9s3vftYhaMr&amp;t=1695544607&amp;persistent_id=4666199950789852023&amp;tst=1695545006&amp;story=37ca3162-a963-5720-91c2-510fa300c030&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/56838/8352-1665080113000-square/logo-square)" title="BFM.ru"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">РИА Новости: разведчики уничтожили танк Leopard с экипажем армии ФРГ</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Putin_zayavil_chto_izbiratelnaya_sistema_Rossii_schitaetsya_odnoj_izluchshikh_vmire--56f4d4c257e1c13547979b26c887f3ff?lang=ru&amp;from=main_portal&amp;fan=1&amp;stid=7KgjidlnJ7iW_nxRtwCt&amp;t=1695544607&amp;persistent_id=4666199950789883772&amp;tst=1695545006&amp;story=e6064c8c-8a11-5abf-bf12-c25ac87d7534&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/41096/1040-1640775230584-square/logo-square)" title="Газета.Ru"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Путин заявил, что избирательная система России считается одной из лучших в мире</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Politico_ukrainskim_gospitalyam_vZaporozhe_ne_khvataet_medikamentov--9697b284c62b6216391f15c4a491eecb?lang=ru&amp;from=main_portal&amp;fan=1&amp;stid=9U0kJ_5_GxOKO0E0oKPR&amp;t=1695544607&amp;persistent_id=4666199950789889325&amp;tst=1695545006&amp;story=e81bfcf8-3581-5402-9c9d-78376145485c&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/135513/1002-1544074003449-square/logo-square)" title="РИА Новости"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Politico: украинским госпиталям в Запорожье не хватает медикаментов</span></div></a></li></ul>, <ul class="card-news__stories-Bu"><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Gubernator_Sergej_Civilev_pozdravil_zhitelej_Kuzbassa_sDnem_mashinostroitelya--4251180bff66ab9b82a8137b12f31a11?lang=ru&amp;from=reg_portal&amp;fan=1&amp;stid=NPRU&amp;t=1695544607&amp;persistent_id=4666199950789814021&amp;tst=1695545006&amp;story=396b60ae-fbcb-50f5-8250-6840f9e7fc31&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/41096/254133784-1612858469.771003-square/logo-square)" title="Царьград"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Губернатор Сергей Цивилев поздравил жителей Кузбасса с Днем машиностроителя</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Kemerovchane_predlozhili_uvelichit_chislo_dorozhnykh_polos_navezde_vgorod--b35205e1bd44c6d70a90c2cf59b8be3f?lang=ru&amp;from=reg_portal&amp;fan=1&amp;stid=d8gq&amp;t=1695544607&amp;persistent_id=4666199950789880308&amp;tst=1695545006&amp;story=cd0ddc1e-86b4-5a1b-98f3-af09eb394604&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/135513/254157551-1670985624012-square/logo-square)" title="ProKuzbass.ru"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Кемеровчане предложили увеличить число дорожных полос на въезде в город</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Naobnovlennoj_ulice_SHornikova_sokhranyat_derevya_i_klumby--74d3468bddfda3b38c15d7edf2779ec2?lang=ru&amp;from=reg_portal&amp;fan=1&amp;stid=oW5K8ro2U6ApSGmA&amp;t=1695544607&amp;persistent_id=4666199950789870287&amp;tst=1695545006&amp;story=db671fdb-5725-58e8-bf8e-195c059916fc&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/41096/254133784-1612858469.771003-square/logo-square)" title="Царьград"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">На обновленной улице Шорникова сохранят деревья и клумбы</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Ceny_nabenzin_i_dizel_vKuzbasse_upadut--990e594ea80fedd976c456d54e91c4ea?lang=ru&amp;from=reg_portal&amp;fan=1&amp;stid=lBRYyI_beFg8ykICfSSE&amp;t=1695544607&amp;persistent_id=4666199950789338962&amp;tst=1695545006&amp;story=c54bb205-014a-531c-b972-080c6f1cb6ec&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/33291/14614-1590398026134-square/logo-square)" title="Ngs42.ru"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Цены на бензин и дизель в Кузбассе упадут</span></div></a></li><li class="card-news-story__story-6T card-news-story__mobile-TS" data-testid="news-item"><a aria-label="Открыть новости по теме" class="card-news-story__link-3I" href="https://m.dzen.ru/news/story/Kaluzhskaya_oblast_poluchit_61_million_namodulnye_oteli--ac523be7ecaed41ac5e4b2aef4fa6d13?lang=ru&amp;from=reg_portal&amp;fan=1&amp;stid=4iTp34DgtYg5MlGvRS8b&amp;t=1695544607&amp;persistent_id=4666199950789806507&amp;tst=1695545006&amp;story=b882fce8-e225-57ac-be91-acd4d0987e69&amp;issue_tld=ru&amp;contour=exp0&amp;utm_referrer=m.dzen.ru" rel="noopener nofollow" target="_blank"><div class="card-news-story__agencyLogo-wB card-news-story__mobile-TS" style="background-image:url(//avatars.dzeninfra.ru/get-ynews-logo/117671/2427-1576231723161-square/logo-square)" title="ТРК Ника"></div><div class="card-news-story__textContainer-18 card-news-story__isWhiteDzen-3k card-news-story__mobile-TS"><span aria-label="Заголовок" class="card-news-story__text-3F card-news-story__mobile-TS">Калужская область получит 61 миллион на модульные отели</span></div></a></li></ul>]

    response = requests.get('https://m.dzen.ru/', cookies=cookies, headers=headers)
    # response = requests.get(url="https://dzen.ru", headers=headers,cookies=y)
    # print(response.text)
    if response.status_code == 200:
        await message.answer(text='200')
        response.encoding = 'utf-8'
        soup = bs(response.text, 'html.parser')
        g=soup.find_all('ul', class_="card-news__stories-Bu")
        t=soup.find('ul', class_="card-news__stories-Bu")
        v.clear()
        # print(g)
        # print(t)

        for i in g:
            # v.append([k['href'] for k in i.find_all('a')])
            for n in i.find_all('li'):
                v.append(n.find('a')['href'])
                await message.answer(text=n.text)
        print()
        print()

        # await page.screenshot(path='/root/tike/botserver/screenshots/screenshot2.png')

    else:
        await message.answer(text='не 200')

@dp.message(Text(text='Новости sel'))
async def novosti_selenium(message: Message):
    await message.answer(text='Новости')
    k = datetime.now().strftime('%d.%m.%y  %H:%M:%S')
    print(k)
    print(message.from_user.id)
    await message.answer(text=k)
    print(message.from_user.id)
    # try:
    options_chrome = webdriver.ChromeOptions()
    # options_chrome.add_extension('coordinates.crx')
    # zzz=options=options_chrome

    options_chrome.add_argument('--headless=chrome')
    with webdriver.Chrome(options=options_chrome) as browser:
        await message.answer(text='1')
        browser.get('https://dzen.ru/?clid=1946579&win=90&yredirect=true&utm_referer=sso.dzen.ru')
        await message.answer(text='2')
        checkbox = browser.find_element(By.CLASS_NAME, 'card-news__stories-Bu')   #

        v.clear()   #  делает список пустым
        g = [i.strip() for i in checkbox.text.split('\n')]   #  список заголовков новостей
        n = [k.get_attribute('href') for k in checkbox.find_elements(By.TAG_NAME, 'a')]   #  список ссылок новостей
        for y, u in zip(g, n):
            # print(y, u)
            v.append(u)   #  добавляет ссылки в список
            # await message.answer(text=u)
            await message.answer(text=y)
    # except:
    #     await message.answer(text='Что то пошло не так')
    #     print('Что то пошло не так')





if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)