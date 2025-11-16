# Str8TV Telegram Bot - Setup Guide

Complete step-by-step guide to configure your Telegram bot.

---

## Step 1: Create Your Telegram Bot

1. **Open Telegram** and search for `@BotFather`
2. **Start a chat** with BotFather and send: `/newbot`
3. **Choose a name** for your bot (e.g., "Str8TV Support Bot")
4. **Choose a username** (must end in "bot", e.g., "str8tv_support_bot")
5. **Copy the token** - BotFather will give you a token that looks like:
   ```
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz123456789
   ```
6. **Save this token** - you'll need it in Step 3

---

## Step 2: Get Your Admin Chat ID

This ID lets the bot forward live support requests to you.

### Method 1: Using @userinfobot (Easiest)

1. Search for `@userinfobot` in Telegram
2. Start a chat with it
3. It will instantly send you your Chat ID
4. Copy the number (e.g., `123456789`)

### Method 2: Using Your Bot

1. First, complete Step 3 below (insert your token)
2. Run your bot: `python3 str8tv_bot.py`
3. Send any message to your bot on Telegram
4. Check the terminal - it will show: `Chat ID: 123456789`
5. Copy your Chat ID

---

## Step 3: Configure Your Bot

1. **Open `str8tv_bot.py`** in your code editor
2. **Find these lines** at the top:
   ```python
   TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
   ADMIN_CHAT_ID = 123456789  # Replace with your Telegram user ID
   ```

3. **Replace the values**:
   ```python
   TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz123456789"
   ADMIN_CHAT_ID = 987654321  # Your actual chat ID
   ```

4. **Save the file**

---

## Step 4: Add Your Video Tutorials

1. **Upload your videos** to YouTube or any hosting platform
2. **Copy the video URLs**
3. **Open `str8tv_bot.py`** and find the `"videos"` section (around line 74-83)
4. **Replace the placeholder links**:
   ```python
   "videos": (
       "🎥 *Setup Video Tutorials*\n\n"
       "📺 *TiviMate Setup Guide*\n"
       "https://www.youtube.com/watch?v=YOUR_TIVIMATE_VIDEO\n\n"
       "📺 *IPTV Smarters Setup Guide*\n"
       "https://www.youtube.com/watch?v=YOUR_SMARTERS_VIDEO\n\n"
       "📺 *Firestick Installation Guide*\n"
       "https://www.youtube.com/watch?v=YOUR_FIRESTICK_VIDEO\n\n"
       "💡 Need more help? Contact support!"
   ),
   ```

5. **Save the file**

---

## Step 5: Verify Logo File

Make sure `SK-Logo-02-01.jpeg` is in the same folder as `str8tv_bot.py`

Check with:
```bash
ls -la *.jpeg
```

If missing, the bot will still work but won't show the logo on `/start`

---

## Step 6: Install Dependencies

Install the required Python packages:

```bash
pip install python-telegram-bot --upgrade
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

---

## Step 7: Test Your Bot Locally

1. **Run the bot**:
   ```bash
   python3 str8tv_bot.py
   ```

2. **You should see**:
   ```
   🤖 Str8TV Bot (Live Support Enabled) is running...
   ```

3. **Open Telegram** and search for your bot username
4. **Send `/start`** - you should see:
   - Your logo
   - Welcome message
   - Menu buttons

5. **Test all features**:
   - Click each menu button
   - Type keywords like "billing", "setup", "help"
   - Type "talk to someone" to test live agent forwarding
   - Check if you receive the admin notification

---

## Troubleshooting

### Bot doesn't respond
- Check TOKEN is correct (no extra spaces)
- Make sure bot is running (`python3 str8tv_bot.py`)
- Verify you started the bot (`/start` command)

### Logo doesn't appear
- Check `SK-Logo-02-01.jpeg` is in the same folder
- Verify file name matches exactly (case-sensitive)
- Bot will work without logo, just no image

### Live support requests not forwarding
- Verify ADMIN_CHAT_ID is YOUR user ID (not bot's)
- Start a chat with your bot first
- Check for typos in the ID

### Import errors
```bash
pip install python-telegram-bot --upgrade
```

---

## Next Steps

Once your bot works locally, proceed to **DEPLOYMENT.md** to run it 24/7.

Need help? Check **USER_GUIDE.md** for updating FAQs and managing the bot.
