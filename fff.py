import logging
from telethon import TelegramClient,sync, utils, errors
from telethon.tl.types import PeerUser, PeerChat
from telethon import functions, types
import time
import re
import asyncio, os
from contextlib import suppress
import traceback
from telethon.sessions import StringSession
import random



log = logging.getLogger(__name__)
format = '%(asctime)s %(levelname)s:%(message)s'
logging.basicConfig(format=format, level=logging.INFO)

api_id = ""
api_hash = ""

filename_excel = "project_for_export_no_formulas_31_10_18.xlsx"
filename_numbers = "number.txt"

queue_entity = asyncio.Queue()
numbers = []
count_thread = 8






async def create_client():
    file_list = os.listdir('sessions')
    sht = len(file_list)
    xaka = random.randint(0, sht)
    acaunt = file_list[xaka]
    cli = open(f"sessions/{acaunt}").read()
    client = TelegramClient(StringSession(cli), api_id, api_hash)
    await client.connect()


async def parse_entity(client):
    result = None
    try:
        
        result = client(functions.channels.GetFullChannelRequest(
                channel="https://t.me/s_a_t_a_n_a_6_6"
            ))
        print("Успешно")
    except TypeError:
        try:
            result = client(functions.users.GetFullUserRequest(
                id="https://t.me/s_a_t_a_n_a_6_6"
            ))
        except TypeError:
            result = client(functions.messages.GetFullChatRequest(
                chat_id="https://t.me/s_a_t_a_n_a_6_6"
            ))
    except errors.UsernameInvalidError:
        print("Не найден пользователь, канал или чат")
    except errors.InviteHashExpiredError:
        print("Чата больше нет")
    except errors.InviteHashInvalidError:
        print("Ссылка приглашения не валидна")
    except ValueError:
        print("Невозможно получить entity. Для начала нужно вступить в группу или чат")
    except errors.FloodWaitError:
        print("Ожидание суток")
    return result


async def crawl(future):
    futures = []
   
    for f in asyncio.as_completed([asyncio.ensure_future(create_client())]):
        client = await f
        while queue_entity.qsize() > 0:
            futures.append(asyncio.ensure_future(parse_entity(queue_entity.get_nowait(), client)))
    if futures:
        await asyncio.wait(futures)
    print(futures)
async def start_main(root):
    loop = asyncio.get_event_loop()
    initial_future = loop.create_future()
    initial_future.set_result(root)
    await crawl(initial_future)

if __name__ == '__main__':
    start = time.time()

    log.info("Time work: %s", time.time() - start)