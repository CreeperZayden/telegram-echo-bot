import os
from telegram.ext import Updater, CommandHandler

# Initialize the bot
updater = Updater(token=os.environ.get('YOUR_BOT_TOKEN'), use_context=True)

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
    ...
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=codes_text)

def send_wiki_link(update, context):
    wiki_link = "https://blox-fruits.fandom.com/wiki/Blox_Fruits"
    context.bot.send_message(chat_id=update.effective_chat.id, text=wiki_link)

def send_fruit_list(update, context):
    fruits_list = """
    Fruit    Type
    Bomb    
    Barrier    
    ...
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

# Start the bot
updater.start_polling()

# Run the bot until you press Ctrl-C
updater.idle()
