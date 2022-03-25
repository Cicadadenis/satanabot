from aiogram.utils import executor
import asyncio, os
import requests
from data import config
from loader import scheduler, dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify

token = config.TOKEN

async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    MethodGetMe = (f'''https://api.telegram.org/bot{token}/GetMe''')
    response = requests.post(MethodGetMe)
    tttm = response.json()
    tk = tttm['ok']
    if tk == True:
        id_us = (tttm['result']['id'])
        first_name = (tttm['result']['first_name'])
        username = (tttm['result']['username'])
  

        print(f"""
                    ---------------------------------
                    🆔 Bot id: {id_us}
                    ---------------------------------
                    👤 Имя Бота: {first_name}
                    ---------------------------------
                    🗣 username: {username}
                    ---------------------------------
                    🌐 https://t.me/{username}
                    ---------------------------------
                    ******* Suport: @Satanasat ******
        """)

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
