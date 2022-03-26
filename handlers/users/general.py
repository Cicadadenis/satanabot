from datetime import datetime
from email import message
import os
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from proxy_checking import ProxyChecker
from telethon import TelegramClient
from aiogram.dispatcher.filters.state import State, StatesGroup
from data.config import ADMINS, api_id, api_hash
from filters import IsNotSubscribed
from keyboards.inline.menu import admin_menu, main_menu, back_to_main_menu, goo
from loader import dp, bot
from utils.db_api.db_commands import *
from utils.other_utils import get_user_date, send_message_to_chat
class test(StatesGroup):
    tt = State()

@dp.callback_query_handler(IsNotSubscribed())
async def answer_call(call: CallbackQuery):
    await call.answer("❗️У вас нету подписки, чтобы пользоваться ботом")


# ========================DELETE BROADCAST MESSAGE========================
# WITH STATE
@dp.callback_query_handler(text="delete_this_message", state="*")
async def del_broadcast_msg(call: CallbackQuery):
    await call.message.delete()
    await bot_start(call.message)


# ========================SHOW MAIN MENU========================
# /start WITHOUT STATE


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    if not await select_user(message.from_user.id):
        await add_user(message.from_user.id)
    stat, user = await select_statistic(), await select_user(message.from_user.id)
    result_date = await get_user_date(message.from_user.id)
    proxy = await select_user_proxy(message.from_user.id)
    if not await select_user(message.from_user.id):
        await add_user(message.from_user.id)
    stat, user = await select_statistic(), await select_user(message.from_user.id)
    result_date = await get_user_date(message.from_user.id)
    proxy = await select_user_proxy(message.from_user.id)
    await message.answer(
        "<b>👋 Привет, данный бот создан для удобного авто~постинга во все чаты телеграмма!\n\n"
        "♻️ Отправлять любому юзеру своё сообщение от добавленного аккаунта!\n"
        "♻️ Добавлять хоть 100 чатов (и настраивать их одновременно)\n"
        "♻️Включать / отключать рассылки.\n"
        "♻️Менять все параметры, задержки / текст / фото / и другие!\n\n"
        "🚀Удачного использования!</b>",
        reply_markup=goo)
    
@dp.callback_query_handler(text="back_to_main_menu", state="*")
async def support(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await state.finish()
    sms = open('sms.txt', 'r').read()
    tt = open('time.txt', 'r')
    ti = int(tt.read())
    tt.close()
    file_list = os.listdir('sessions')
    sms = open('sms.txt', 'r').read()
    x = len(file_list)   
    file_list = os.listdir('sessions')
    sms = open('sms.txt', 'r').read()
    x = len(file_list)
    uss = open('ussers.txt', 'r')
    ff = uss.readlines()
    z = len(ff)
    user = await select_user(call.from_user.id)
    stat, proxy = await select_statistic(), await select_user_proxy(call.from_user.id)
    result_date = await get_user_date(call.from_user.id)

    pp = await call.message.answer(
            f"👤    <b>Акаунтов для спама:</b>   {x}\n"
            f"🕔    <b>Тайминг Установлен на</b> {ti} <b>сек.</b>\n\n"
            f"👩‍👩‍👧‍👧    <b>Участников для спама:</b> {z}", reply_markup=await main_menu(call.message.from_user.id))


@dp.callback_query_handler(text="posst")
async def posst(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #await call.message.delete(pp.message_id)
    sms = open('sms.txt', 'r').read()
    ft = open("foto.txt", "r").read()
    if ft == "+++":
        path = f'pics/broadcast/cicada.jpg'
        with open(path, 'rb') as f:
            photo = f.read()
        await call.message.answer_photo(photo=photo, caption=f"{sms}", reply_markup=back_to_main_menu)
    if ft == "---":
        await call.message.answer(sms, reply_markup=back_to_main_menu)
# BACK FROM ANY HANDLER TO MAIN MENU WITH STATE
@dp.callback_query_handler(text="admin", state="*")
async def support(call: CallbackQuery, state: FSMContext):
    

    await state.finish()
    if str(call.from_user.id) in ADMINS:
        await call.message.edit_text("Админ-меню", reply_markup=admin_menu)


# ========================INFO BUTTON========================
@dp.callback_query_handler(text="inf")
async def support(call: CallbackQuery):
    await call.message.edit_text(
        "<b>👋 Привет, данный бот создан для удобного авто~постинга во все чаты телеграмма!\n\n"
        "♻️ Отправлять любому юзеру своё сообщение от добавленного аккаунта!\n"
        "♻️ Добавлять хоть 100 чатов (и настраивать их одновременно)\n"
        "♻️Включать / отключать рассылки.\n"
        "♻️Менять все параметры, задержки / текст / фото / и другие!\n\n"
        "🚀Удачного использования!</b>",
        reply_markup=back_to_main_menu)
