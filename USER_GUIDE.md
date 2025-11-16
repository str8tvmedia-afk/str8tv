# Str8TV Telegram Bot - User Guide

Complete guide for managing and updating your bot after deployment.

---

## Table of Contents
1. [Updating FAQs & Responses](#updating-faqs--responses)
2. [Adding/Changing Video Tutorials](#addingchanging-video-tutorials)
3. [Customizing Auto-Reply Keywords](#customizing-auto-reply-keywords)
4. [Managing Live Support Requests](#managing-live-support-requests)
5. [Adding New Menu Options](#adding-new-menu-options)
6. [Changing Bot Appearance](#changing-bot-appearance)
7. [Checking Bot Status](#checking-bot-status)
8. [Common Issues & Solutions](#common-issues--solutions)

---

## Updating FAQs & Responses

### Location: Menu Button Responses

**File:** `str8tv_bot.py` (lines 54-97)

### How to Update

1. **Open `str8tv_bot.py`**
2. **Find the `responses` dictionary**
3. **Edit the text for any category:**

```python
responses = {
    "general": (
        "📺 *General Info*\n\n"
        "💡 Your updated text here.\n"
        "🖥️ Add more lines as needed."
    ),
    "billing": (
        "💳 *Subscriptions & Billing*\n\n"
        "Update your billing info here."
    ),
    # ... more categories
}
```

### Example: Change Billing Response

**Before:**
```python
"billing": (
    "💳 *Subscriptions & Billing*\n\n"
    "Buy a plan at https://str8tvmedia.com\n"
    "⏱️ Activation: 1–3 hours after payment."
),
```

**After:**
```python
"billing": (
    "💳 *Subscriptions & Billing*\n\n"
    "🎉 Special Offer: 20% off annual plans!\n"
    "Buy now at https://str8tvmedia.com\n"
    "⏱️ Instant activation for new customers."
),
```

### Formatting Tips

- Use `\n` for new line
- Use `\n\n` for blank line
- Use `*text*` for **bold** text
- Use `_text_` for _italic_ text
- Keep URLs as plain text

### Apply Changes

**Railway:**
1. Commit changes to GitHub
2. Railway auto-deploys

**DigitalOcean:**
```bash
systemctl stop str8tv-bot
nano str8tv_bot.py  # Make changes
systemctl start str8tv-bot
```

---

## Adding/Changing Video Tutorials

### Location: Videos Menu Response

**File:** `str8tv_bot.py` (lines 74-83)

### How to Update Videos

```python
"videos": (
    "🎥 *Setup Video Tutorials*\n\n"
    "📺 *TiviMate Setup Guide*\n"
    "https://youtube.com/YOUR_VIDEO_1\n\n"
    "📺 *IPTV Smarters Setup Guide*\n"
    "https://youtube.com/YOUR_VIDEO_2\n\n"
    "📺 *Firestick Installation Guide*\n"
    "https://youtube.com/YOUR_VIDEO_3\n\n"
    "💡 *Pro tip:* Check our channel for more tutorials!"
),
```

### Adding More Videos

```python
"videos": (
    "🎥 *Setup Video Tutorials*\n\n"
    "📺 *TiviMate Setup*\n"
    "https://youtube.com/watch?v=video1\n\n"
    "📺 *IPTV Smarters Setup*\n"
    "https://youtube.com/watch?v=video2\n\n"
    "📺 *Firestick Install*\n"
    "https://youtube.com/watch?v=video3\n\n"
    "📺 *Smart TV Setup*\n"        # NEW VIDEO
    "https://youtube.com/watch?v=video4\n\n"
    "📺 *Android Box Setup*\n"    # NEW VIDEO
    "https://youtube.com/watch?v=video5"
),
```

---

## Customizing Auto-Reply Keywords

### Location: Auto-Reply Function

**File:** `str8tv_bot.py` (lines 111-155)

### How Keywords Work

When a user types a message, the bot scans for keywords and sends a relevant response.

### Adding Keywords

**Example: Add "cost" and "pricing" to billing keywords**

**Before:**
```python
if any(word in message for word in ["price", "plan", "subscribe", "renew", "billing", "payment"]):
```

**After:**
```python
if any(word in message for word in ["price", "plan", "subscribe", "renew", "billing", "payment", "cost", "pricing"]):
```

### Adding New Keyword Category

**Example: Add refund policy responses**

Add this after line 116:

```python
elif any(word in message for word in ["refund", "cancel", "money back"]):
    reply = (
        "💰 *Refund Policy*\n"
        "Refunds available within 7 days if service not activated.\n"
        "Contact support@str8tvmedia.com for refund requests."
    )
```

---

## Managing Live Support Requests

### How It Works

When users type keywords like "talk to someone" or "help", the bot:
1. Sends them a confirmation message
2. Forwards their message to YOU (admin) via Telegram

### Receiving Requests

You'll get a notification like:
```
🚨 Live Chat Request!
From: @username
User ID: 123456789
Message: I need help with my subscription
```

### Responding to Users

**Option 1: Direct Reply (Recommended)**
1. Copy the User ID from the notification
2. Open your bot chat
3. Use this command format:
   ```
   /reply 123456789 Your message here
   ```

**Option 2: Manual Response**
1. Search for the user in Telegram (if they have a username)
2. Send them a direct message

### Adding /reply Command (Optional Enhancement)

Add this function to `str8tv_bot.py`:

```python
async def reply_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if admin
    if update.message.from_user.id != ADMIN_CHAT_ID:
        await update.message.reply_text("⛔ Admin only command")
        return

    # Get user ID and message
    try:
        args = update.message.text.split(' ', 2)
        user_id = int(args[1])
        message = args[2]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"📞 *Support Response:*\n\n{message}",
            parse_mode="Markdown"
        )
        await update.message.reply_text("✅ Message sent!")
    except:
        await update.message.reply_text("Usage: /reply USER_ID Your message")

# In main() function, add:
app.add_handler(CommandHandler("reply", reply_to_user))
```

---

## Adding New Menu Options

### Step 1: Add Button to Menu

**File:** `str8tv_bot.py` (lines 14-22)

```python
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("1️⃣ General Info", callback_data="general")],
        [InlineKeyboardButton("2️⃣ Subscriptions & Billing", callback_data="billing")],
        [InlineKeyboardButton("3️⃣ Setup Help", callback_data="setup")],
        [InlineKeyboardButton("4️⃣ Setup Videos", callback_data="videos")],
        [InlineKeyboardButton("5️⃣ Troubleshooting", callback_data="troubleshoot")],
        [InlineKeyboardButton("6️⃣ Contact Support", callback_data="support")],
        [InlineKeyboardButton("7️⃣ Referral Program", callback_data="referral")]  # NEW
    ])
```

### Step 2: Add Response

**File:** `str8tv_bot.py` (lines 54-97)

```python
responses = {
    # ... existing responses ...
    "referral": (
        "🎁 *Referral Program*\n\n"
        "Earn rewards for referring friends!\n"
        "🔗 Your referral link: https://str8tvmedia.com/ref/yourcode\n"
        "💰 Get 1 month free for every 3 referrals!"
    )
}
```

---

## Changing Bot Appearance

### Update Logo

1. Replace `SK-Logo-02-01.jpeg` with your new image
2. Keep the same filename OR update line 28 in `str8tv_bot.py`:
   ```python
   photo=open('YOUR_NEW_IMAGE.jpeg', 'rb')
   ```

### Update Welcome Message

**File:** `str8tv_bot.py` (lines 30-32)

```python
caption=(
    "👋 *Welcome to Str8TV Media Support!*\n"
    "Your updated welcome message here.\n\n"
    "Type your question or choose a category below 👇"
),
```

### Change Menu Emoji/Text

Edit line 16-21 to customize button appearance:
```python
[InlineKeyboardButton("🔥 Hot Deals", callback_data="billing")],
```

---

## Checking Bot Status

### Quick Check: Send Message to Bot
1. Open bot in Telegram
2. Send `/start`
3. Instant response = bot is online

### Railway Dashboard
1. Go to https://railway.app
2. Open your project
3. Check "Logs" tab
4. Look for: `🤖 Str8TV Bot (Live Support Enabled) is running...`

### DigitalOcean Server
```bash
ssh root@your_droplet_ip
systemctl status str8tv-bot
```

**Output:**
- ✅ `Active: active (running)` = Bot is online
- ❌ `Active: inactive (dead)` = Bot is offline

### View Live Logs (DigitalOcean)
```bash
journalctl -u str8tv-bot -f
```

Press `Ctrl+C` to exit

---

## Common Issues & Solutions

### Issue: Bot Not Responding

**Possible Causes:**
1. Bot is offline
2. Wrong TOKEN
3. User didn't start the bot

**Solution:**
```bash
# Check if running
systemctl status str8tv-bot

# Restart
systemctl restart str8tv-bot

# Check logs for errors
journalctl -u str8tv-bot -n 50
```

### Issue: Changes Not Showing

**Railway:**
- Make sure you committed and pushed to GitHub
- Check deployment logs

**DigitalOcean:**
```bash
systemctl restart str8tv-bot
```

### Issue: Live Support Not Working

**Check:**
1. ADMIN_CHAT_ID is YOUR user ID (not bot's)
2. You started a chat with the bot
3. Keywords match (e.g., "help", "talk to someone")

**Test:**
```python
# Add this temporarily to see your ID
print(f"User ID: {update.message.from_user.id}")
```

### Issue: Syntax Errors After Editing

**Check:**
- All strings use quotes (`"` or `'`)
- Parentheses are closed
- Commas between dictionary items

**Test locally:**
```bash
python3 -m py_compile str8tv_bot.py
```

No output = syntax is valid

### Issue: Bot Crashes Randomly

**View crash logs:**
```bash
journalctl -u str8tv-bot -n 100
```

**Common causes:**
- Network timeout (auto-restarts handle this)
- Image file missing
- Invalid TOKEN

---

## Best Practices

### 1. Test Changes Locally First
```bash
python3 str8tv_bot.py
# Test in Telegram
# Ctrl+C to stop
```

### 2. Backup Before Major Changes
```bash
cp str8tv_bot.py str8tv_bot.py.backup
```

### 3. Keep Responses Short
- Mobile users prefer concise info
- Use bullets for multiple points
- Add "Contact support for more info"

### 4. Update Video Links Regularly
- Test links monthly
- Remove outdated videos
- Add new content

### 5. Monitor User Requests
- Check what keywords users type
- Add new auto-replies for common questions
- Update FAQs based on real questions

---

## Getting Help

### Bot Issues
1. Check logs first
2. Test locally
3. Verify configuration

### Code Questions
- Check this guide
- Review `str8tv_bot.py` comments
- Test changes locally before deploying

### Telegram API Issues
- Official docs: https://core.telegram.org/bots/api
- Python library: https://python-telegram-bot.org

---

## Quick Reference Commands

### Railway
- Deploy: Push to GitHub
- Logs: Dashboard → Logs tab
- Restart: Dashboard → Restart button

### DigitalOcean
```bash
# Status
systemctl status str8tv-bot

# Start
systemctl start str8tv-bot

# Stop
systemctl stop str8tv-bot

# Restart
systemctl restart str8tv-bot

# Logs
journalctl -u str8tv-bot -f

# Edit code
nano str8tv_bot.py
```

---

**Need more help?** Review SETUP.md and DEPLOYMENT.md for detailed configuration and deployment instructions.
