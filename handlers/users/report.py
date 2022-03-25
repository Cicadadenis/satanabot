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
import pandas as pd
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
i = 5
s = 0
c = 0
o = 0
msm = 0
a = 0
while i <= xx:
    #try:
        if a == count:
            client.disconnect()
            i = i + 1
            a = 0
        mm = 0
        file_list = os.listdir('sessions')
        acaunt = file_list[i]
        cli = open(f"sessions/{acaunt}").read()
        aka = acaunt.split(".")[0]
        client = TelegramClient(StringSession(cli), api_id, api_hash)
        client.connect()
        print("ok")
        ss = open('ussers.txt', 'r').readlines()
        username = ss[a][:-1]

        entity = client.get_entity("satanasat")
        print(entity)
        input()
            #messages = [mes.id for mes in client.iter_messages(entity, min_id=2)]
            #report = client(functions.messages.ReportRequest(
             #                   entity,
              #                  messages,
               #                 types.InputReportReasonSpam(),
                #                'spam message'
                 #           ))
            #rsn = types.InputReportReasonPornography()
            #msg = "some messages"
            #print("podgotovka")
            #client(functions.messages.ReportRequest(
            #        peer='@'+username,
            #        id=[int(message_id)],
            #        reason=rsn,
            #        message = msg
            #    ))
            #print("DDAA")
            #o = o + 1
            #msm = msm + 1
            #mm = mm + 1
            #time.sleep(ti)
            #a = a + 1
  #  asyncio.run(rep(username, message_id, rsn, msg))
#asyncio.get_event_loop().run_forever()

