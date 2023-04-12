import logging
import os
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '6236836050:AAFFVcr5PtpPleWeiVpo_PaNxDdwvgU3fKo'


# Configure logging
logging.basicConfig(level=logging.INFO)

#storage keep the answer
storage = MemoryStorage()

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
