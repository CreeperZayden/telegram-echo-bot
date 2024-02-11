import os
import asyncio
from telegram import Bot
from telegram.ext import Dispatcher, Updater, CommandHandler
from keep_alive import keep_alive

# Initialize the bot and dispatcher
bot = Bot(token=os.environ.get('token'))
dp = Dispatcher(bot)

# Define your command handlers
async def start(update, context):
    username = update.message.from_user.username
    await update.message.reply(f"Hello {username}!")

async def help(update, context):
    commands = "/start - say hi with the telegram username\n"
    commands += "/list - show list of fruit types\n"
    commands += "/wiki - provide a link to the Blox Fruits wiki\n"
    commands += "/codes - show redeem codes for Blox Fruits"
    await update.message.reply(commands)

async def list_fruits(update, context):
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
Bird
    """
    await update.message.reply(fruit_list)

async def wiki(update, context):
    wiki_link = "https://blox-fruits.fandom.com/wiki/Blox_Fruits"
    await update.message.reply(wiki_link)

async def codes(update, context):
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
    TantaiGaming: Redeem code for 15 Minutes of 2x Experience
    """
    await update.message.reply(codes_list)

# Register your command handlers with the dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("list", list_fruits))
dp.add_handler(CommandHandler("wiki", wiki))
dp.add_handler(CommandHandler("codes", codes))

# Start the bot
async def main():
    await bot.delete_webhook()
    await dp.start_polling()

if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())
