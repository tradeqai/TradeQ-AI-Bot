import os
import json
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load Configuration
with open("config.json", "r") as f:
    config = json.load(f)

TELEGRAM_BOT_TOKEN = config["TELEGRAM_BOT_TOKEN"]

async def start(update: Update, context: CallbackContext) -> None:
    """Handle /start command"""
    keyboard = [
        [InlineKeyboardButton("📊 Scan Market", callback_data="scan_market")],
        [InlineKeyboardButton("🔍 Get Stock Info", callback_data="stock_info")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to TradeQ AI Bot! 🚀 Choose an option:", reply_markup=reply_markup)

async def scan_market(update: Update, context: CallbackContext) -> None:
    """Scan market for opportunities"""
    await update.message.reply_text("🔍 Scanning market... Fetching trade signals...")

def main():
    """Start the bot"""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan_market))
    logger.info("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
