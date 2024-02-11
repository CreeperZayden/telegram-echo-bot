import os
from telegram.ext import Updater, CommandHandler
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Get your bot token from environment variables
token = os.environ.get('token')

# Initialize the bot
updater = Updater(token=token, use_context=True)

# Define command handlers
def start(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {user.first_name}!")

def help_command(update, context):
    available_commands = """
    Available commands:
    /start - Start the bot
    /help - Display available commands
    /hi - Say hi to the bot
    /halal - Greet with Assalamualaikum
    /codes - Get codes
    /wiki - Get Wiki link
    /list - Get list of fruits
    /sex - Remind to stay halal
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=available_commands)

def say_hi(update, context):
    user = update.message.from_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello, {user.first_name}!")

def greet_with_assalamualaikum(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Assalamualaikum, my brother/sister!")

def send_codes(update, context):
    codes_text = """
    NEWTROLL: Redeem for a 20 minutes of 2x EXP Boost
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
    context.bot.send_message(chat_id=update.effective_chat.id, text=codes_text)

def send_wiki_link(update, context):
    wiki_link = "https://blox-fruits.fandom.com/wiki/Blox_Fruits"
    context.bot.send_message(chat_id=update.effective_chat.id, text=wiki_link)

def send_fruit_list(update, context):
    fruits_list = """
    Fruit Type
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
    context.bot.send_message(chat_id=update.effective_chat.id, text=fruits_list)

def remind_halal(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Stay halal, brother!")

# Register command handlers
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("hi", say_hi))
updater.dispatcher.add_handler(CommandHandler("halal", greet_with_assalamualaikum))
updater.dispatcher.add_handler(CommandHandler("codes", send_codes))
updater.dispatcher.add_handler(CommandHandler("wiki", send_wiki_link))
updater.dispatcher.add_handler(CommandHandler("list", send_fruit_list))
updater.dispatcher.add_handler(CommandHandler("sex", remind_halal))

if __name__ == '__main__':
    try:
        # Start the bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the service fails
        updater.idle()
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)  # Log the full exception traceback
        updater.stop()
        updater.is_idle = False  # Ensure the updater loop exits
