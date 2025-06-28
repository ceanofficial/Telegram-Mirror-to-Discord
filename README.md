# 📬 Telegram to Discord Bridge Bot

This Python script connects a **Telegram bot** with a **Discord webhook**, acting as a message bridge. It listens for incoming messages on a Telegram bot and automatically forwards them to a specified Discord channel using a webhook.

## 🔧 Features

- Listens to any text messages sent to your Telegram bot
- Automatically forwards the message content and sender's name to a Discord channel
- Uses `python-telegram-bot` and `requests` libraries
- Simple and lightweight – no database required

## 🚀 How It Works

1. A message is sent to your Telegram bot.
2. The bot receives the message and extracts the sender's name and message content.
3. The message is forwarded to the Discord channel via a webhook.

## 📦 Requirements

- Python 3.6+
- `python-telegram-bot`
- `requests`

Install the dependencies using:

```bash
pip install python-telegram-bot requests
```

## 🔑 Setup

1. **Create a Telegram Bot**
   - Talk to [@BotFather](https://t.me/BotFather) on Telegram to create a new bot and get the bot token.

2. **Create a Discord Webhook**
   - In your Discord server, go to a channel → Edit Channel → Integrations → Webhooks → New Webhook
   - Copy the Webhook URL

3. **Update the Script**

Replace the placeholders in the script:

```python
telegram_token = 'TOKEN'               # Replace with your Telegram bot token
telegram_chat_id = '-ID'              # (Optional: Not used directly)
discord_webhook_url = 'WEBHOOK'       # Replace with your Discord webhook URL
```

## ▶️ Running the Bot

Run the script using:

```bash
python telegram_to_discord.py
```

The bot will start polling Telegram for new messages and forward them to Discord in real-time.

## 📄 Example Output

**Telegram:**
```
User: Hello from Telegram!
```

**Discord:**
```
Username: User
Message: Hello from Telegram!
```

## 🛠 Code

```python
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
```

## 📫 Contact

Feel free to open issues or submit PRs for improvements!
