
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
from telethon.sessions import StringSession
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
a = 5
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
        ss = open('ussers.txt', 'r').readlines()
        username = ss[a][:-1]
        message_id = "8" # as example
        rsn = types.InputReportReasonPornography()
        msg = "some messages"
        
        client(functions.messages.ReportRequest(
                peer='@'+username,
                id=[int(message_id)],
                reason=rsn,
                message = msg
            ))
        o = o + 1
        msm = msm + 1
        mm = mm + 1
        time.sleep(ti)
        a = a + 1