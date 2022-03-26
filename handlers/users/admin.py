import asyncio
import os
import random
from random import randint
from telethon import TelegramClient, Button, events 
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from telethon.tl.functions.messages import ImportChatInviteRequest
from aiogram.utils.exceptions import Unauthorized
from telethon.tl.functions.channels import JoinChannelRequest
import json
import os
from loguru import logger
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from convert_tdata import convert_tdata
import time
from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from telethon.errors.rpcerrorlist import FloodWaitError
from keyboards.inline.menu import back_admin, admin_menu, choose_menu
from loader import dp, bot
from states.states import BroadcastState, GiveTime, TakeTime
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu, ssttop
from utils.db_api.db_commands import select_all_users, del_user, update_date
from calendar import c
from email import message
import random
from telethon.sessions import StringSession
from telethon.tl.custom import Button
from datetime import datetime
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu, inv
import socks
from utils.db_api.db_commands import select_all_users, del_user, update_date
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from aiogram.dispatcher import FSMContext
from telethon.tl.functions.messages import AddChatUserRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import os, sys
import configparser
import csv
import time
import random

from lib2to3.pgen2 import token
import rarfile
import shutil
import re
import requests
from datetime import datetime
import time
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, types, executor
from aiogram.utils.markdown import hbold, hlink
import time
from threading import Timer
#from data.config import api_id, api_hash
#from loader import scheduler
import os
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime, timedelta


class akasil(StatesGroup):
    sms_text = State()

class sms5(StatesGroup):
    sms_text = State()

class sms4(StatesGroup):
    sms_text = State()

class sms3(StatesGroup):
    sms_text = State()

class sms2(StatesGroup):
    sms_text = State()

class post(StatesGroup):
    text = State()

class tima(StatesGroup):
    timeout = State()
@dp.callback_query_handler(text="paussa")
async def paus(call: CallbackQuery):
    await call.message.answer("⏱    <b>Введи значение для паузы между отправкой смс 'меньше 30 сек не рекоминдую спам'</b>")
    @dp.message_handler(content_types=['text'])
    async def paus(message: Message):
        pausse = message.text
        with open('time.txt', 'w') as f:
            f.write(pausse)
        await message.answer(f"⏱    <b>Тайминг Изменен на {pausse}</b>", reply_markup=back_to_main_menu)





@dp.callback_query_handler(text="rep")
async def rep(call: CallbackQuery):
    msms = await call.message.answer("<b>Запуск Reporter</b>")
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    tt = open('time.txt', 'r')
    ti = int(tt.read())
    tt.close()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    count = int(z)
    i = 1
    s = 0
    c = 0
    o = 0
    msm = 0
    a = 5
    while i <= xx:
       # try:
            if a == count:
                await client.disconnect()
                i = i + 1
                a = 0
            sto = open('stop.txt', 'r').read()
            if sto == 'stop':
                with open('stop.txt', 'w') as f:
                    f.write("start")
                await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            aka = acaunt.split(".")[0]
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            ss = open('ussers.txt', 'r').readlines()
            username = ss[a][:-1]
            message_id = "8" # as example
            rsn = types.InputReportReasonPornography()
            msg = "some messages"
            async def rep(username, message_id, rsn, msg):
                print("y") # this is working
                a = await client(functions.messages.ReportRequest(
                    peer='@'+username,
                    id=[int(message_id)],
                    reason=rsn,
                    message = msg
                ))
                print(a)
            #asyncio.run(rep(username, message_id, rsn, msg))
            #await client(functions.messages.ReportRequest(peer, id=[42], reason=types.InputReportReasonSpam(), message='Hello there!'))
            #aka = acaunt.split(".")[0]
            msm = msm + 1
            await msms.edit_text(
                f"<b>   Всего отправленно жалоб {msm}</b>\n\n"
                f"💬    <b>Жалоба С Акаунта: \n<code>{aka}</code> \nна</b> <code>{username}</code> Отправленна! +1 \n\n", reply_markup=ssttop)
            o = o + 1
            
            mm = mm + 1
            time.sleep(ti)
            a = a + 1
            await client.disconnect()

#                except:
#                    a = a + 1
#                    await call.message.answer(
#                        f"💬    <b>Жалоба С Акаунта: \n<code>{aka}</code> \nна</b> <code>{user}</code> Отправленна!\n\n")
#                    await client.disconnect()
#                    c = c + 1
#                    i = i + 1
#                    time.sleep(ti)
#
#        except:
#            
#           
#            break
#    await call.message.answer(
#                        f"💬     <b>Жалобы все отправленны</b> !!", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="add_silka", state="*")
async def add_silka(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(
        f"<b>Для загрузки акаунтов по ссылке</b>\n"
        f"<b>Нужны акаунты только с этого ресурса:</b>\n"
        f"<b>https://ydeda.pro/</b>")
    await akasil.sms_text.set()




@dp.message_handler(state=akasil.sms_text)
async def receive_com(message: Message, state: FSMContext):
    ww = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
    API_ID = 17463049
    sessions = []
    await message.answer("<b>Идет Обработка и подвязка акаунтов ожидайте...</b>")
    baza = []
    print("".join(map(str, ww)))
    url_pattern = r'https://[\S]+'
    u = re.findall(url_pattern, ww)
    s = len(u)
    
    await message.answer(f"<b>Подготавливаю {s} Акаунтов</b>")
    for x in u:
        
        os.system(f"curl -k -L --output temp_aka/telega.rar  {x}")
        time.sleep(4)
        rar_file = "temp_aka/telega.rar"
        dir_name = "tdatas"
        rarobj = rarfile.RarFile(rar_file)
        rarobj.extractall(dir_name)
        xx = os.listdir(dir_name)
        

        #os.system(f"powershell Remove-item data\{xx[0]} -recurse")

        for tdata in os.listdir("tdatas"):
            
            try:
                auth_key = convert_tdata(f"tdatas/{tdata}/tdata")[0]
            except Exception as err:
                logger.error(err)
            else:
                logger.success(f"{tdata} успешно конвертировано")

            sessions.append(StringSession(auth_key))

            logger.info("Проверка аккаунтов")
            j = 0
            for session in sessions:
                await message.edit_text(f"<b>Подключаю Акаунт № {xx[j]}</b>")
                j = j + 1
                client = TelegramClient(
                    session,
                    api_hash=API_HASH,
                    api_id=API_ID
                )

                

                await client.connect()
                auth_key = client.session.save()
                with open(f"sessions/{tdata}.session", "w") as file:
                    file.write(auth_key)
                    await client.disconnect()
                    logger.success(f"{tdata} — сохранён.")
                    
        zzz = os.listdir("tdatas")
        nn = len(zzz)
        os.system(f"rm -r tdatas/* ")

    await message.answer(f"<b>Готово ! Акаунты добавленны +{s} шт !</b>", reply_markup=back_to_main_menu)
 
    await state.finish()
    sessions.clear()

@dp.callback_query_handler(text="sms", state="*")
async def sms(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("💬    <b>Введи текст для рассылки</b>",
                                 reply_markup=back_to_main_menu)
    await sms2.sms_text.set()
    #await call.message.answer('💬     <b>Текст успешно сохранен</b> !',
     #                     reply_markup=back_to_main_menu)
#
    @dp.message_handler(state=sms2.sms_text)
    async def sms_spam(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open('sms.txt', 'w') as f:
            f.write(sms)
        await message.answer('💬     <b>Текст успешно сохранен</b> !',
                            reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="give_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await GiveTime.GT1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=GiveTime.GT1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await GiveTime.next()
    await state.update_data(user_id=user_id)
    await msg_to_edit.edit_text("<b>⏰  Введите время в часах которое выдать человеку:</b>", reply_markup=back_admin)


@dp.message_handler(state=GiveTime.GT2)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, user_id = data.get("msg_to_edit"), data.get("user_id")
    try:
        hours = int(message.text)
        await message.delete()
        date_when_expires = datetime.now() + timedelta(hours=hours)
        date_to_db = str(date_when_expires).split(".")[0].replace("-", " ").split(":")
        date_to_db = " ".join(date_to_db[:-1])
        await update_date(user_id, date_to_db)
        await state.finish()
        await msg_to_edit.edit_text("<b>Доступ выдан.</b>", reply_markup=back_admin)
    except ValueError:
        await msg_to_edit.edit_text("<b>    ⏰Не верный формат, попробуйте еще раз.</b>")


@dp.callback_query_handler(text="take_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await TakeTime.T1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=TakeTime.T1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await update_date(user_id, None)
    await state.finish()
    await msg_to_edit.edit_text("<b>У юзера больше нет доступа.</b>", reply_markup=back_admin)


# ========================BROADCAST========================
# ASK FOR PHOTO AND TEXT
@dp.callback_query_handler(text="broadcast")
async def broadcast2(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("🏞    <b>Отправь фото  которое будут рассылаться по юзерам</b>", reply_markup=back_to_main_menu)
    await BroadcastState.BS1.set()


# RECEIVE PHOTO OR TEXT
@dp.message_handler(content_types=['photo'], state=BroadcastState.BS1)
async def broadcast4(message: Message, state: FSMContext):
    await message.delete()
    easy_chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    name = 'cicada'
    photo_name = name + ".jpg"
    await message.photo[-1].download(f"pics/broadcast/{photo_name}")
    await state.update_data(photo=photo_name, text=message.caption)
    with open("foto.txt", "w") as f:
        f.write("+++")
    await asyncio.sleep(2)
    await message.answer("🏞    <b>Фото успешно загруженно</b>", reply_markup=back_to_main_menu)



@dp.callback_query_handler(text="fdel")
async def fdel(call: CallbackQuery):
    try:
        with open("foto.txt", "w") as f:
            f.write("---")
        await call.message.answer("<b>Фото Удаленно</b>", reply_markup=back_to_main_menu)
    except:
        await call.message.answer("<b>Фото Удаленно</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="hahah")
async def broadcast_text_post(call: CallbackQuery):
    try:
        kart = os.listdir("pics/broadcast")
        if kart[0] == 'cicada.jpg':
            path = f'pics/broadcast/cicada.jpg'
            with open(path, 'rb') as f:
                photo = f.read()
            ssm = open('sms.txt', 'r').read()
            zz = ssm.split('|')
            sms = random.choice(zz)
            await call.message.answer_photo(photo=photo, caption=f"{ssm}\n\n"
                                                            f"<b>Все правильно? Отправляем?</b>",
                                    reply_markup=choose_menu)
    except:
        ssm = open('sms.txt', 'r').read()
        zz = ssm.split('|')
        sms = random.choice(zz)
        await call.message.answer(ssm + "\n\n<b>Все правильно? Отправляем?</b>", reply_markup=choose_menu)

from telethon import TelegramClient, sync

@dp.callback_query_handler(text="invait")
async def gru(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Выбери куда добавлять пользователей</b>", reply_markup=inv)



@dp.callback_query_handler(text="invait_can", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms4.sms_text.set()


@dp.message_handler(state=sms4.sms_text)
async def cann(message: Message, state: FSMContext):
    channel = message.text
    msms = await message.answer("<b>Запуск Инвайта</b>")
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    if z <= 1:
        await message.answer("Добать получателей список пуст !")
        
    count = int(z)
    i = 0
    d = 0
    s = 0
    c = 0
    o = 0
    msm = 0
    a = 0
    v = 0
    while i <= xx:
        try:
            if v == z:
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            akk = acaunt.split(".")[0]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            result = await client(functions.users.GetFullUserRequest(id="me"))
            nam = result.user.first_name
            lnam = result.user.last_name
            if mm <= 20:
                
                try:
                    await client(JoinChannelRequest(channel))
                    o = o + 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Добавлен пользователь {akk} в группу ✅</b>")
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti)
                    msm = msm + 1
                    mm = mm + 1
                    v = v + 1
                    
                   
                    d = d + 1
                except:
                    
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Не Добавлен {akk} в группу ❌</b>")
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti/2)
                    d = d + 1
                    v = v + 1
        except:
            i = i + 1
    await message.answer("<b>Инвайт завершил работу</b>", reply_markup=back_to_main_menu)
    await state.finish()


@dp.callback_query_handler(text="parser", state="*")
async def gru(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms5.sms_text.set()



@dp.message_handler(state=sms3.sms_text)
async def gruuu(message: Message, state: FSMContext):
    channel = message.text
    msms = await message.answer("<b>Начинаю Инвайт Группы</b>")
    await message.delete()
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    if z <= 1:
        await message.answer("Добать получателей список пуст !")
        
    count = int(z)
    i = 1
    d = 0

    c = 0
    o = 0
    msm = 0
    a = 0
    v = 0
    while i <= xx:
        try:
            if d == 15:
                i = i + 1
            if v == z:
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            await client(JoinChannelRequest(channel))

            if mm <= 20:
                ss = open('ussers.txt', 'r').readlines()
                user = ss[a][:-1]
                akk = acaunt.split(".")[0]
                #await client(functions.channels.InviteToChannelRequest(channel=channel, users = [user]))
                try:
                    await client(InviteToChannelRequest(channel=channel, users = [user]))
                    o = o + 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Добавлен пользователь {user} в группу ✅</b>")
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti)
                    mm = mm + 1
                    v = v + 1
                    a = a + 1
                    d = d + 1
                except:
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Не Добавлен {user} в группу ❌</b>")
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti/2)
               #     except:
               #     time.sleep(ti/2)
               #     await message.answer(f"<b>Не вышло добавить пользователь {user} в группу ❌</b>")
               #     d = d + 1
                    a = a + 1
               #     v = v + 1
        except:
          ##  print("ne policilos")
            i = i + 1
            
    await message.answer("<b>Инвайт завершил работу</b>", reply_markup=back_to_main_menu)
    await state.finish()

@dp.callback_query_handler(text="invait_grup", state="*")
async def gru(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms3.sms_text.set()


@dp.message_handler(state=sms5.sms_text)
async def gruuu(message: Message, state: FSMContext):
    channel = message.text
    await message.answer("<b>Начинаю парсинг.....</b>")
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    file_list = os.listdir('sessions')
    sht = len(file_list)
    xaka = random.randint(0, sht)
    acaunt = file_list[xaka]
    cli = open(f"sessions/{acaunt}").read()
    client = TelegramClient(StringSession(cli), api_id, api_hash)
    await client.connect()
    try:
        await client(JoinChannelRequest(channel))
    except:pass
    offset_user = 0    # номер участника, с которого начинается считывание
    limit_user = 100  # максимальное число записей, передаваемых за один раз

    all_participants = []   # список всех участников канала
    filter_user = ChannelParticipantsSearch('')
    while True:
        participants = await client(GetParticipantsRequest(channel,
            filter_user, offset_user, limit_user, hash=0))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset_user += len(participants.users) # len(participants.users)
    await message.answer("<b>Идет сохранения списка.....</b>")
    all_users_details = []   # список словарей с интересующими параметрами участников канала
    for participant in all_participants:
        if participant.username not in all_users_details: 
                all_users_details.append(participant.username)
    for x in all_users_details:
        if x == None:
            continue
        if x[-3:] == 'bot':
            continue
        if x[-3:] == 'Bot':
            continue
        else:        
            with open("ussers.txt", "a") as f:
                f.write(str(f"{x}\n"))

    zx = open('ussers.txt', 'r').readlines()
        
    await message.answer(
        f"<b>Список сохранен</b>\n"
        f"<b>Получено {len(zx)} пользователей</b>", reply_markup=back_to_main_menu)

        

@dp.callback_query_handler(text="STOP")
async def st(call: CallbackQuery):
    with open("status.txt", "w") as f:
        f.write("1")

# START BROADCAST
@dp.callback_query_handler(text="go_start")
async def broadcast_text_post(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    ded = await call.message.answer("<b>Спам Рассылка Запущенна !</b>")
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"  
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    mom = len(ss)
    i = 0
    p = 0
    t = 0
    c = 0
    o = 0
    propusk = 0
    while xx >= i:
        acaunt = file_list[i]
        akk = acaunt.split(".")[0]
        ti = int(open('time.txt', 'r').read())
        sto = open('stop.txt', 'r').read()
        if sto == 'stop':
            with open('stop.txt', 'w') as f:
                f.write("start")
            await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
            
        try:
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
        except:
            client = TelegramClient(f"sessions/{acaunt}", api_id, api_hash)
            await client.connect()

        fff = open("pics/broadcast/cicada.jpg", 'rb').read() 
        ssm = open('sms.txt', 'r', encoding="UTF-8").read()
        zz = ssm.split('|')
        sms = random.choice(zz)
        try:
          file_list2 = open('ussers.txt', 'r').readlines()
        except:
          await call.message.answer("Рассылка завершена", reply_markup=back_to_main_menu)
            
        
        if propusk == 10:
            #await client.disconnect()
            i = i + 1
            t = t - 9
            propusk = 0
        if mom == 0:
            break
        if p >= 40:
            await client.disconnect()
            i = i + 1
            p = p - 40
        if len(file_list2) >= p:
            try:
                ft = open("foto.txt", "r").read()
                if ft == "+++":
                    with open("ussers.txt", "r") as z:
                        lines = z.readlines()
                        far = lines[0][:-1]
                    await client.send_file(far, file=fff, caption=ssm)
                    with open("ussers.txt", "w") as f:
                        f.writelines(lines[1:])
                if ft == "---":
                    with open("ussers.txt", "r") as z:
                        lines = z.readlines()
                        far = lines[0][:-1]
                    await client.send_message(far, ssm)
                p = p + 1
                propusk = 0
                t = t + 1
                o = o + 1
                result = await client(functions.users.GetFullUserRequest(id="me"))
                nam = result.user.first_name
                lnam = result.user.last_name
                await client.disconnect()
                try:
                    xxx = file_list2[t][:-1]
                except:
                    pass
                await ded.edit_text(
                            f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                            f"<b>На пользователя 🗣 {xxx} ✅</b>\n\n"
                            f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {o}</b>\n\n"
                            f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                mom = mom - 1
                time.sleep(ti)
            except:
                t = t + 1
                c = c + 1
                result = await client(functions.users.GetFullUserRequest(id="me"))
                nam = result.user.first_name
                lnam = result.user.last_name
                try:
                    xxx = file_list2[t][:-1]
                except:
                    pass
                await ded.edit_text(
                            f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                            f"<b>На пользователя 🗣 {xxx} ❌</b>\n\n"
                            f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {o}</b>\n\n"
                            f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                time.sleep(ti/2)
                propusk = propusk + 1
                mom = mom - 1
                await client.disconnect()
        else:
            await client.disconnect()
            i = i + 1
            mom = mom - 1
    await call.message.answer("✅ <b>Рассылка Завершена</b> ✅", reply_markup=back_to_main_menu)    

        

        
              

        
@dp.callback_query_handler(text="ceker")
async def broadcast_text_post(call: CallbackQuery, state: FSMContext):
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581" 
    file_list = os.listdir('sessions')
    xx = len(file_list)   
    i = 0
    s = 0
    a = 0
    tit = 0 
    r = 0
    while i <= xx:
        try:
            mm = 0         
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            try:
                cli = open(f"sessions/{acaunt}").read()
                client = TelegramClient(StringSession(cli), api_id, api_hash)
                await client.connect()
            except:
                client = TelegramClient(f"sessions/{acaunt}", api_id, api_hash)
                await client.connect()
            try:
                await client.connect()
                result = await client(functions.users.GetFullUserRequest(id="me"))
                nam = result.user.first_name
                lnam = result.user.last_name
                akk = acaunt.split(".")[0]
                vremya = result.user.status.was_online

                time.sleep(1)
                i = i + 1
                r = r + 1
                await call.message.edit_text(
                    f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                    f"❌    <b>В Спаме:  {tit}</b>\n"
                    f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                    f"<b>Акаунт {akk} \n💠 {nam} {lnam}</b> ✅\n"
                    f"<b>Последняя активность \n{vremya}</b>")
                await client.disconnect()   
            except:         
                akk = acaunt.split(".")[0]
                #await call.message.answer(f"<b>Акаунт {akk}</b> ❌")
                path = (f"sessions/{acaunt}")
                os.remove(path)
                tit = tit + 1
                await call.message.edit_text(
                    f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                    f"❌    <b>В Спаме:  {tit}</b>\n"
                    f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
                    f"<b>Акаунт {akk} \n💠 {nam} {lnam}</b> ❌\n"
                    f"<b>Последняя активность \n{vremya}</b>")
                time.sleep(1)
                i = i + 1  
            
  

        except:
            i = i + 1 
            
    await call.message.answer(
                            f"🔍    <b>Проверка Завершена</b> !\n\n"
                            f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
                            f"❌    <b>В Спаме:  {tit}</b>\n", reply_markup=back_to_main_menu) 


@dp.callback_query_handler(text="xxx")
async def exitt(call: CallbackQuery):
    await call.message.edit_text("<b>меню</b>", reply_markup=back_to_main_menu)
