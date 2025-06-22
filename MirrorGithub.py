import telegram
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Telegram bot token
telegram_token = 'TOKEN'

# Telegram chat ID
telegram_chat_id = '-ID'

# Discord webhook URL
discord_webhook_url = 'WEBHOOK'

# Create Telegram bot object
bot = telegram.Bot(token=telegram_token)

# Define function to handle incoming Telegram messages
def handle_telegram_message(update, context):
    # Extract message text and sender name
    message_text = update.message.text
    sender_name = update.message.chat.first_name

    # Send message to Discord
    discord_message = {
        'username': sender_name,
        'content': message_text
    }
    requests.post(discord_webhook_url, json=discord_message)

# Start Telegram bot polling for new messages
bot_updater = Updater(token=telegram_token, use_context=True)
bot_dispatcher = bot_updater.dispatcher
bot_dispatcher.add_handler(MessageHandler(Filters.text, handle_telegram_message))
bot_updater.start_polling()

# Keep the program running
bot_updater.idle()
