import importlib
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, chat_invite_link  # for reply keyboard (sends message)
from aiogram.dispatcher.webhook import SendMessage
import credentials
import logging
import sys
import random
import effects
import asyncio


calculator = importlib.import_module("bounty-calculator")
channel_client = importlib.import_module("channel-client")
recorder = importlib.import_module("ffmpeg-selenium-recorder")

# effects = importlib.import_module("chat-effects")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

bot = Bot(token=credentials.token)
chat_id = credentials.target_channel

dp = Dispatcher(bot)

# bot.send_message(chat_id='@bot-channel-test998877', text='test from bot')
# channel =

# context variables
# game = {'name': '', 'itm_players': 0, 'prizepool': 0, 'is_running': False, 'prizes': []}
game = {
    'name': 'aaa',
    'itm_players': 30,
    'prizepool': 30000,
    'is_running': False,
    'prizes': [],
    '1st': 0,
    '2nd': 0,
    '3rd': 0,
    # image[0] is for low bounties, image[1] for 1st ... image[2] for 2nd ...
    'images': ['images/tilt.webp',
               'images/omg.webp',
               'images/running_hot.webp',
               'images/running_hot_elki.webp']
}

final_prizes = []


# used to check the function to handle arbitrary text (default text)
last_function = ''

# keyboards
setup1 = KeyboardButton('Set tournament name 📜📜📜')
setup2 = KeyboardButton('Set ITM players 💪💪💪')
setup3 = KeyboardButton('Set prizepool 💰💰💰')
setup_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(setup1).add(setup2).add(setup3)

start1 = KeyboardButton('☸️☸️☸️ Start game ☸️☸️☸️')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(setup1).add(setup2).add(setup3).add(start1)

win1 = KeyboardButton('🤞🏻🤞🏻🤞🏻 start the wheel 🤞🏻🤞🏻🤞🏻')
win2 = KeyboardButton('show remaining bounties')
winner_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(win1).add(win2)


async def advertise_winner(winner, prize):
    nice_prize = effects.to_nice_numbers(prize)
    await bot.send_message(chat_id, effects.announce_winner(winner, prize, game))

    # setting image to send
    imagefile = ''
    if prize == game['1st']:
        imagefile = game['images'][1]
    elif prize == game['2nd']:
        imagefile = game['images'][2]
    elif prize == game['3rd']:
        imagefile = game['images'][3]
    else:
        imagefile = game['images'][0]

    with open(imagefile, 'rb') as image_file:
        await bot.send_animation(chat_id, image_file)


async def sleep(s):
    time.sleep(s)

async def send_gif(winner):
    with open("wheel-{}.gif".format(winner), 'rb') as gif_file:
        await bot.send_animation(chat_id, gif_file)

async def send_video(filename):
    with open(filename, 'rb') as mp4_file:
        await bot.send_video(chat_id, mp4_file)

        # await bot.send_animation(chat_id, mp4_file)



@dp.message_handler(commands=['x'])
async def x(message: types.Message):
    global last_function
    logger.info("x() called ...")
    last_function = 'start'
    await bot.send_message(chat_id, "congrats {} 💪💪💪\nyou won {} 💰💰💰\n".format('asaf', effects.to_nice_numbers(2500)))
    #await message.answer('Im the mystery-bounty-bot ...\npress the menu button to setup a new game ...', reply_markup=setup_kb)




@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global last_function
    logger.info("start() called ...")
    last_function = 'start'

    # normal mode
    #await message.answer('Im the mystery-bounty-bot ...\npress the menu button to setup a new game ...', reply_markup=setup_kb)

    # debug mode

    #output_file=""
    #await bot.send_photo(message.chat.id, output_file)


    await message.answer('Im the mystery-bounty-bot ...\npress the menu button to setup a new game ...', reply_markup=start_kb)


@dp.message_handler(regexp='Set tournament name 📜📜📜')
async def set_name(message: types.Message):
    global last_function
    logger.info("set_name() called ...")
    last_function = 'set_name'
    await message.answer('What is the tournament name ?')
    # game['name'] = message.text

@dp.message_handler(regexp='Set ITM players 💪💪💪')
async def set_itm_players(message: types.Message):
    global last_function
    logger.info("set_itm_players() called ...")
    last_function = 'set_itm_players'
    await message.answer('How many players are ITM ?')
    # game['itm_players'] = int(message.text)

@dp.message_handler(regexp='Set prizepool 💰💰💰')
async def set_prizepool(message: types.Message):
    global last_function
    logger.info("set_prizepool() called ...")
    last_function = 'set_prizepool'
    await message.answer('What is the bounty prizepool ?')
    # game['itm_players'] = int(message.text)

@dp.message_handler(regexp='☸️☸️☸️ Start game ☸️☸️☸️')
async def start_game(message: types.Message):
    global last_function
    logger.info("start_game() called ...")
    last_function = 'start_game'
    if game['name'] != '' and game['itm_players'] > 0 and game['prizepool'] > 0:
        #await message.answer('What is the bounty prizepool ?')
        logger.info("game: {} started ...".format(game['name']))
        game['is_running'] = True

        # calculate winning prizes and get max_prize
        prizes = calculator.generate_winning_pattern(int(game['itm_players']), int(game['prizepool']))
        # finding the 3 biggest values (using a shallow copy) - can do better ...

        prizes_temp = prizes.copy()
        game['1st'] = max(prizes_temp)
        prizes_temp.remove(game['1st'])
        game['2nd'] = max(prizes_temp)
        prizes_temp.remove(game['2nd'])
        game['3rd'] = max(prizes_temp)
        prizes_temp.remove(game['3rd'])

        logger.info("generated prizes: {}".format(str(prizes)))
        logger.info("biggest prizes: {}".format(str(game['1st']), str(game['2nd']), str(game['3rd'])))

        logger.info("shuffling prizes ...")
        #random.shuffle(prizes)
        game['prizes'] = prizes

        await message.answer('Current tournament config:\nname: {}\nITM players: {}\nPrizepool: {}\nprizes: {}\nmax_prize: {}'.
                             format(game['name'], str(game['itm_players']), str(game['prizepool']), str(game['prizes']), str(game['1st'])), reply_markup=winner_kb)

    else:
        logger.warning("game setup incomplete, ignoring")


@dp.message_handler(regexp='🤞🏻🤞🏻🤞🏻 start the wheel 🤞🏻🤞🏻🤞🏻')
async def start_wheel(message: types.Message):
    global last_function
    last_function = 'start_wheel'
    logger.info("start_wheel() called ...")
    await message.answer('Who wins the KO ?\n')




# generic default handler for all ( must be declared LAST ! )
@dp.message_handler()
async def default(message: types.Message):
    global last_function
    if last_function == '':
        logger.warning("default() called but not by us ... ignoring ...")
        return
    logger.info("default() called (last_function={})...".format(last_function))
    await message.answer(message.text)
    if last_function == 'set_name':
        game['name'] = message.text
    if last_function == 'set_itm_players':
        game['itm_players'] = int(message.text)
    if last_function == 'set_prizepool':
        game['prizepool'] = int(message.text)

    if game['is_running']:
        if last_function == 'start_wheel':
            winner = message.text
            logger.info("spinning for: {} ...".format(winner))
            logger.info("remaining prizes before: {} ...".format(str(len(game['prizes']))))

            # record video
            prize, output_file = recorder.spin_and_record(game['prizes'], game['prizepool'])

            # send video
            await send_video(output_file)
            logger.info("{} won {} .".format(winner, prize))

            # remove the prize from remaining prizes


            # print('prizes: {}\nstr(prize): {}'.format(game['prizes'], str(prize)))

            game['prizes'].remove(prize)
            logger.info("remaining prizes after: {} ...".format(str(len(game['prizes']))))

            try:
                await bot.send_photo(message.chat.id, output_file)
            except Exception as e:
                logger.error(e)

            # await bot.send_animation(message.chat.id, output_file)
            # winner = message.text
            # logger.info("spinning for: {} ...".format(winner))
            # logger.info("remaining prizes before: {} ...".format(str(len(game['prizes']))))
            # prize = calculator.spin_wheel(game['prizes'], winner)
            # logger.info("{} won {} .".format(winner, prize))
            # game['prizes'] = game['prizes'][1:]
            # logger.info("remaining prizes after: {} ...".format(str(len(game['prizes']))))
            await sleep(7)
            await advertise_winner(winner, prize)
            # await send_gif(winner)

            await message.answer('Open menu for next KO...',reply_markup=winner_kb)



        else:
            logger.warning("we shouldnt be here ... ")

        print('dd')
    else:
        if game['name'] != '' and game['itm_players'] > 0 and game['prizepool'] > 0:
            print('setup complete, adding start_game button')
            logger.info("setup complete, adding start_game button'")
            await message.answer('Current tournament config:\nname: {}\nITM players: {}\nPrizepool: {}\n'.format(game['name'], str(game['itm_players']), str(game['prizepool'])), reply_markup=start_kb)
        else:
            logger.info("setup incomplete, removing start_game button'")
            await message.answer('Current tournament config:\nname: {}\nITM players: {}\nPrizepool: {}\n'.format(game['name'], str(game['itm_players']), str(game['prizepool'])), reply_markup=setup_kb)

    last_function = 'default'

# this is the last line
executor.start_polling(dp)