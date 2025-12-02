import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8248058395:AAEKtYl-98JZ76Fl42SQFCh5n-kdKzGEZYE"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

user_state = {}
STATE_WAIT_YES = "WAIT_YES"
STATE_WAIT_NEXT = "WAIT_NEXT"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_state[user_id] = STATE_WAIT_YES
    await update.message.reply_text("Hi 👋\nDo you want Canva Pro details? Reply yes to continue.", parse_mode="Markdown")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip().lower()
    state = user_state.get(user_id)

    if state == STATE_WAIT_YES:
        if text in ["yes","y","ok","sure"]:
            user_state[user_id] = STATE_WAIT_NEXT
            await update.message.reply_text("Canva Pro: ₹499, 1–2 years ✅\nSend Gmail ID + screenshot after payment.", parse_mode="Markdown")
        else:
            await update.message.reply_text("Reply yes if you want Canva Pro details 😊", parse_mode="Markdown")

    elif state == STATE_WAIT_NEXT:
        await update.message.reply_text("Thanks! 🙏 I’ll wait here.")
        user_state[user_id] = None
    else:
        await update.message.reply_text("Type /start to begin 🙂")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
