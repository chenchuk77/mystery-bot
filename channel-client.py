from aiogram import Bot, types
import credentials

bot_token = credentials.token
channel_id = credentials.target_channel

bot2 = Bot(token=bot_token)


async def send_message():
    await bot2.send_message(channel_id, "Hello, World!")


# w
#def send(message):
#bot2.loop.run_until_complete(send_message())


