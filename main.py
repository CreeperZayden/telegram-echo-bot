from python-telegram-bot import Bot, Dispatcher, executor, types
import os
from keep_alive import keep_alive
keep_alive()

bot = Bot(token=os.environ.get('token'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f"Hello {username}!")

@dp.message_handler(commands=['help'])
async def show_commands(message: types.Message):
    commands = "/start - say hi with the telegram username\n"
    commands += "/list - show list of fruit types\n"
    commands += "/wiki - provide a link to the Blox Fruits wiki\n"
    commands += "/codes - show redeem codes for Blox Fruits"
    await message.reply(commands)

@dp.message_handler(commands=['list'])
async def show_fruit_list(message: types.Message):
    fruit_list = """Fruit Type
    Bomb 
    Barrier 
    Buddha 
    Chop 
    Control 
    Dark 
    Dough 
    Dragon 
    Flame 
    Gravity 
    Gum 
    Ice 
    Kilo 
    Light 
    Love 
    Magu 
    Magma 
    Phoenix 
    Quake 
    Rumble 
    Sand 
    Smoke 
    Snow 
    Spin 
    Spring 
    Venom 
    String 
    Human 
    Giraffe 
    Leopard 
    Wolf 
    Paw 
    Door 
    Spike 
    Rocket 
    Bird"""
    await message.reply(fruit_list)

@dp.message_handler(commands=['wiki'])
async def show_wiki(message: types.Message):
    wiki_link = "https://blox-fruits.fandom.com/wiki/Blox_Fruits"
    await message.reply(wiki_link)

@dp.message_handler(commands=['codes'])
async def show_codes(message: types.Message):
    codes_list = """NEWTROLL: Redeem for a 20 minutes of 2x EXP Boost

KITT_RESET: Redeem for a Stat Refund or Reset

Sub2CaptainMaui: Redeem for 20 minutes of 2x EXP Boost

SUB2GAMERROBOT_RESET1: Redeem for a free Stat Reset

kittgaming: Redeem for 20 minutes of 2x EXP Boost

Sub2Fer999: Redeem for 20 minutes of 2x EXP Boost

Enyu_is_Pro: Redeem for 20 minutes of 2x EXP Boost

Magicbus: Redeem for 20 minutes of 2x EXP Boost

JCWK: Redeem for 20 minutes of 2x EXP Boost

Starcodeheo: Redeem for 20 minutes of 2x EXP Boost

Bluxxy: Redeem for a Boost

fudd10_v2: Redeem code for 2 Beli

FUDD10: Redeem code for $1

BIGNEWS: Redeem code for an in-game title

THEGREATACE: Redeem code for 20 Minutes of 2x Experience

SUB2GAMERROBOT_EXP1: Redeem for 30 Minutes of 2x Experience

Sub2OfficialNoobie: Redeem code for 20 Minutes of 2x Experience

StrawHatMaine: Redeem for 20 minutes of 2x Experience

SUB2NOOBMASTER123: Redeem code for 15 Minutes of 2x Experience

Sub2UncleKizaru: Redeem code for a Stat Refund

Sub2Daigrock: Redeem code for 15 Minutes of 2x Experience

Axiore: Redeem code for 20 Minutes of 2x Experience

TantaiGaming: Redeem code for 15 Minutes of 2x Experience"""
    await message.reply(codes_list)

if __name__ == '__main__':
    executor.start_polling(dp)
