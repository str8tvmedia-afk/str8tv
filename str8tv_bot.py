from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

TOKEN = "8372128749:AAEH_CKhu6Tk3Pa-If8MrF-qQCj-pddIzvA"
ADMIN_CHAT_ID = 8147936951  # Replace with your Telegram user ID

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ General Info", callback_data="general")],
        [InlineKeyboardButton("2️⃣ Subscriptions & Billing", callback_data="billing")],
        [InlineKeyboardButton("3️⃣ Setup Help", callback_data="setup")],
        [InlineKeyboardButton("4️⃣ Setup Videos", callback_data="videos")],
        [InlineKeyboardButton("5️⃣ Troubleshooting", callback_data="troubleshoot")],
        [InlineKeyboardButton("6️⃣ Contact Support", callback_data="support")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_photo(
            photo=open('SK-Logo-02-01.jpeg', 'rb'),
            caption=(
                "👋 *Welcome to Str8TV Media Support!*\n"
                "I can help with setup, billing, or troubleshooting.\n\n"
                "Type your question or choose a category below 👇"
            ),
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )
    except FileNotFoundError:
        await update.message.reply_text(
            (
                "👋 *Welcome to Str8TV Media Support!*\n"
                "I can help with setup, billing, or troubleshooting.\n\n"
                "Type your question or choose a category below 👇"
            ),
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    responses = {
        "general": "📺 *General Info*\n\n💡 Str8TV Media offers IPTV streaming...",
        "billing": "💳 *Subscriptions & Billing*\n\nBuy a plan at https://str8tvmedia.com...",
        "setup": "🧩 *Setup Help*\n\n📱 Use TiviMate, IPTV Smarters, or XCIPTV...",
        "videos": "🎥 *Setup Video Tutorials*\n\n📺 Replace with your actual tutorial links...",
        "troubleshoot": "⚙️ *Troubleshooting*\n\n⚠️ Restart device/router, check internet...",
        "support": "📞 *Contact Support*\n\n🕘 Available 7 days/week, 9 AM – 9 PM (EST)..."
    }

    text = responses.get(data, "⚙️ Please select a valid option.")
    await query.edit_message_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard()
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    chat_id = update.message.chat_id
    user = update.message.from_user

    if any(word in message for word in ["price", "plan", "subscribe", "renew", "billing", "payment"]):
        reply = "💳 *Subscriptions & Billing*\nYou can buy or renew plans at https://str8tvmedia.com..."
    elif any(word in message for word in ["setup", "install", "app", "device", "firestick", "tivimate", "video", "tutorial"]):
        reply = "🧩 *Setup Help*\nUse IPTV Smarters, TiviMate, or XCIPTV..."
    elif any(word in message for word in ["channel", "buffer", "freeze", "error", "connection", "not working"]):
        reply = "⚙️ *Troubleshooting*\nRestart your device and router..."
    elif any(word in message for word in ["vpn", "privacy", "safe"]):
        reply = "🔒 *VPN Info*\nA VPN isn't required but recommended..."
    elif any(word in message for word in ["talk", "live", "agent", "person", "help", "someone", "representative"]):
        reply = "👨‍💻 I'm alerting a live support agent for you right now..."
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"🚨 *Live Chat Request!*\nFrom: {user.full_name} (ID: {chat_id})"
        )
    else:
        reply = "🤔 I didn’t quite get that. Please choose from the menu below."

    await update.message.reply_text(reply, parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    app.run_polling()

if __name__ == "__main__":
    main()
