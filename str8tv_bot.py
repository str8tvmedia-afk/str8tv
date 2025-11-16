
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
    # Send logo first
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
        # Fallback if logo file not found
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
        "general": (
            "📺 *General Info*\n\n"
            "💡 Str8TV Media offers IPTV streaming for live TV, sports, and movies.\n"
            "🖥️ Works on Firestick, Android boxes, Smart TVs, phones, and more.\n"
            "🔒 VPN recommended for privacy and performance."
        ),
        "billing": (
            "💳 *Subscriptions & Billing*\n\n"
            "Buy a plan at https://str8tvmedia.com\n"
            "⏱️ Activation: 1–3 hours after payment.\n"
            "🔁 Renew anytime.\n"
            "❌ No refunds after activation, but support can help with issues."
        ),
        "setup": (
            "🧩 *Setup Help*\n\n"
            "📱 Use TiviMate, IPTV Smarters, or XCIPTV.\n"
            "💡 Setup details are emailed after you subscribe.\n"
            "No extra downloads required."
        ),
        "videos": (
            "🎥 *Setup Video Tutorials*\n\n"
            "📺 *TiviMate Setup Guide*\n"
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ\n\n"
            "📺 *IPTV Smarters Setup Guide*\n"
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ\n\n"
            "📺 *Firestick Installation Guide*\n"
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ\n\n"
            "💡 *Pro tip:* Replace these with your actual tutorial videos!"
        ),
        "troubleshoot": (
            "⚙️ *Troubleshooting*\n\n"
            "⚠️ Channels not loading? Restart device/router and check internet (15 Mbps+).\n"
            "❗ Connection failed? Check login or subscription.\n"
            "⏸️ Buffering? Try a VPN or switch servers.\n"
            "🔑 Lost login? Contact support."
        ),
        "support": (
            "📞 *Contact Support*\n\n"
            "🕘 Available 7 days/week, 9 AM – 9 PM (EST)\n"
            "🌐 https://str8tvmedia.com/contact\n"
            "💬 You can also type 'talk to someone' for live help."
        )
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
        reply = (
            "💳 *Subscriptions & Billing*\n"
            "You can buy or renew plans at https://str8tvmedia.com.\n"
            "Activation usually takes 1–3 hours after payment."
        )
    elif any(word in message for word in ["setup", "install", "app", "device", "firestick", "tivimate", "video", "tutorial"]):
        reply = (
            "🧩 *Setup Help*\n"
            "Use IPTV Smarters, TiviMate, or XCIPTV.\n"
            "Setup details are emailed after you subscribe.\n\n"
            "🎥 Want video tutorials? Select '4️⃣ Setup Videos' from the menu!"
        )
    elif any(word in message for word in ["channel", "buffer", "freeze", "error", "connection", "not working"]):
        reply = (
            "⚙️ *Troubleshooting*\n"
            "Restart your device and router.\n"
            "Check internet speed (15 Mbps+).\n"
            "If still not working, contact support."
        )
    elif any(word in message for word in ["vpn", "privacy", "safe"]):
        reply = (
            "🔒 *VPN Info*\n"
            "A VPN isn't required but recommended for stable, private streaming."
        )
    elif any(word in message for word in ["talk", "live", "agent", "person", "help", "someone", "representative"]):
        reply = (
            "👨‍💻 I'm alerting a live support agent for you right now.\n"
            "Please wait a moment — someone will reach out here shortly."
        )
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=(
                f"🚨 *Live Chat Request!*\n"
                f"From: @{user.username or user.first_name}\n"
                f"User ID: {chat_id}\n"
                f"Message: {update.message.text}"
            ),
            parse_mode="Markdown"
        )
    else:
        reply = (
            "🤔 I didn't quite catch that.\n"
            "Please choose a category below 👇 or try asking again more clearly."
        )

    await update.message.reply_text(reply, parse_mode="Markdown", reply_markup=main_menu_keyboard())

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("🤖 Str8TV Bot (Live Support Enabled) is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
