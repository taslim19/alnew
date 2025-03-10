import asyncio
import re
import os
import sys
import time
import logging

from pyrogram import *
from pyrogram.handlers import *
from pyrogram.types import *
from aiohttp import ClientSession
from .config import *
from pyromod import listen

async def create_session():
    return ClientSession()

# Get the event loop safely
try:
    event_loop = asyncio.get_running_loop()
except RuntimeError:
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

aiosession = event_loop.run_until_complete(create_session())

class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSError", "socket"]:
            if X in record.getMessage():
                os.system(f"kill -9 {os.getpid()} && python3 -m ubot")

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()
logger.addHandler(stream_handler)
logger.addHandler(connection_handler)

class Ubot(Client):
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="alcan-Ubot")
        
    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func
        return decorator
        
    def set_prefix(self, user_id, prefix):
        self._prefix[self.me.id] = prefix

    async def start(self):
        await super().start()
        handler = await get_prefix(self.me.id)
        self._prefix[self.me.id] = handler if handler else ["."]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = {"negara": "id"}
        print(f"Starting Userbot ({self.me.id}|{self.me.first_name})")

    async def stop(self):
        await super().stop()

ubot = Ubot(name="ubot")

async def get_prefix(user_id):
    return ubot._prefix.get(user_id, ".")

def anjay(cmd):
    command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")
    
    async def func(_, client, message):
        if message.text and message.from_user:
            text = message.text.strip()
            username = client.me.username or ""
            prefixes = await get_prefix(client.me.id)
            if not text:
                return False
            for prefix in prefixes:
                if not text.startswith(prefix):
                    continue
                without_prefix = text[len(prefix):]
                for command in cmd.split("|"):
                    if not re.match(rf"^(?:{command}(?:@?{username})?)(?:\\s|$)", without_prefix, flags=re.IGNORECASE):
                        continue
                    without_command = re.sub(rf"{command}(?:@?{username})?\\s?", "", without_prefix, count=1, flags=re.IGNORECASE)
                    message.command = [command] + [
                        re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                        for m in command_re.finditer(without_command)
                    ]
                    return True
        return False
    return filters.create(func)

class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs,
                         name="bot",
                         api_id=API_ID,
                         api_hash=API_HASH,
                         bot_token=BOT_TOKEN,
                         device_model="alcanUbot")
    
    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func
        return decorator
    
    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func
        return decorator
    
    async def start(self):
        await super().start()

bot = Bot()

# Import necessary modules after definitions
from ubot.core.helpers import *
from ubot.utils.dbfunctions import *
