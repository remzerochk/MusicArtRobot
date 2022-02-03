from pyrogram import Client as Bot 
from config import API_ID, API_HASH, BOT_TOKEN

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

bot.start()
run()
