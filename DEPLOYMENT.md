# Str8TV Telegram Bot - Deployment Guide

Deploy your bot to run 24/7 using Railway or DigitalOcean.

---

## Option 1: Railway (Easiest - Free Tier Available)

Railway is the simplest way to deploy Python bots with minimal setup.

### Step 1: Prepare Your Files

1. Make sure you have these files:
   - `str8tv_bot.py` (configured with TOKEN and ADMIN_CHAT_ID)
   - `requirements.txt`
   - `SK-Logo-02-01.jpeg`

2. Create a `Procfile` (tells Railway how to run your bot):
   ```bash
   echo "worker: python3 str8tv_bot.py" > Procfile
   ```

### Step 2: Create Railway Account

1. Go to https://railway.app
2. Sign up with GitHub (free account)
3. Verify your email

### Step 3: Deploy Bot

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Connect your GitHub account
4. Create a new repository with your bot files
5. Select the repository in Railway

### Step 4: Configure Environment (Optional)

If you want to use environment variables instead of hardcoding:

1. In Railway dashboard, go to **Variables**
2. Add:
   ```
   TELEGRAM_TOKEN = your_bot_token_here
   ADMIN_CHAT_ID = your_admin_id_here
   ```

3. Update `str8tv_bot.py`:
   ```python
   import os
   TOKEN = os.getenv('TELEGRAM_TOKEN', 'YOUR_TELEGRAM_BOT_TOKEN_HERE')
   ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID', '123456789'))
   ```

### Step 5: Deploy & Monitor

1. Railway will automatically deploy
2. Check **Logs** tab to see if bot is running
3. Look for: `🤖 Str8TV Bot (Live Support Enabled) is running...`

### Step 6: Keep Bot Running

Railway automatically restarts your bot if it crashes. Nothing extra needed!

### Railway Free Tier Limits
- 500 hours/month (enough for 24/7)
- $5 free credit monthly
- Perfect for Telegram bots

---

## Option 2: DigitalOcean Droplet (More Control)

DigitalOcean gives you a full Linux server - more powerful but requires setup.

### Step 1: Create Droplet

1. Go to https://www.digitalocean.com
2. Sign up (get $200 credit with GitHub Student Pack)
3. Click **"Create Droplet"**
4. Choose:
   - **Ubuntu 22.04 LTS**
   - **Basic Plan** - $6/month
   - **Regular CPU**
   - Any datacenter region

5. Add SSH key (or use password)
6. Click **"Create Droplet"**

### Step 2: Connect to Your Server

```bash
ssh root@your_droplet_ip
```

### Step 3: Install Python & Dependencies

```bash
# Update system
apt update && apt upgrade -y

# Install Python
apt install python3 python3-pip -y

# Install python-telegram-bot
pip3 install python-telegram-bot
```

### Step 4: Upload Your Bot Files

**Method 1: Using SCP (from your local machine)**
```bash
scp str8tv_bot.py root@your_droplet_ip:/root/
scp SK-Logo-02-01.jpeg root@your_droplet_ip:/root/
```

**Method 2: Using Git**
```bash
# On your droplet
git clone https://github.com/yourusername/your-bot-repo.git
cd your-bot-repo
```

**Method 3: Manual Copy-Paste**
```bash
# On your droplet
nano str8tv_bot.py
# Paste your code, save with Ctrl+X, Y, Enter
```

### Step 5: Test Bot

```bash
python3 str8tv_bot.py
```

You should see: `🤖 Str8TV Bot (Live Support Enabled) is running...`

Press `Ctrl+C` to stop.

### Step 6: Keep Bot Running 24/7 with systemd

Create a service file:

```bash
nano /etc/systemd/system/str8tv-bot.service
```

Paste this configuration:
```ini
[Unit]
Description=Str8TV Telegram Support Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart=/usr/bin/python3 /root/str8tv_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Save and exit (`Ctrl+X`, `Y`, `Enter`)

### Step 7: Start & Enable Service

```bash
# Reload systemd
systemctl daemon-reload

# Start the bot
systemctl start str8tv-bot

# Enable on boot
systemctl enable str8tv-bot

# Check status
systemctl status str8tv-bot
```

### Step 8: Manage Your Bot

**Check if bot is running:**
```bash
systemctl status str8tv-bot
```

**View logs:**
```bash
journalctl -u str8tv-bot -f
```

**Restart bot:**
```bash
systemctl restart str8tv-bot
```

**Stop bot:**
```bash
systemctl stop str8tv-bot
```

**Update bot code:**
```bash
# Stop bot
systemctl stop str8tv-bot

# Edit code
nano str8tv_bot.py

# Restart bot
systemctl restart str8tv-bot
```

---

## Option 3: Screen (Simple Alternative for DigitalOcean)

If you don't want to use systemd, you can use `screen`:

```bash
# Install screen
apt install screen -y

# Start screen session
screen -S str8tv-bot

# Run bot
python3 str8tv_bot.py

# Detach: Press Ctrl+A then D

# Reattach later
screen -r str8tv-bot

# Kill session
screen -X -S str8tv-bot quit
```

---

## Checking If Your Bot Is Online

### Method 1: Telegram
Send `/start` to your bot - instant response = online

### Method 2: BotFather
1. Open @BotFather on Telegram
2. Send `/mybots`
3. Select your bot
4. Check "Bot Info" - shows last activity

### Method 3: Server Logs (DigitalOcean)
```bash
systemctl status str8tv-bot
# or
journalctl -u str8tv-bot -f
```

### Method 4: Railway Dashboard
Check the **Logs** tab in your Railway project

---

## Troubleshooting Deployment

### Railway Issues

**Bot not starting:**
- Check Logs tab for errors
- Verify `Procfile` exists and is correct
- Ensure `requirements.txt` has `python-telegram-bot`

**Environment variables not working:**
- Make sure variables are set in Railway dashboard
- Restart deployment after adding variables

### DigitalOcean Issues

**Bot crashes immediately:**
```bash
# Check logs
journalctl -u str8tv-bot -n 50
```

**Permission denied:**
```bash
chmod +x str8tv_bot.py
```

**Module not found:**
```bash
pip3 install python-telegram-bot --upgrade
```

**Service won't start:**
```bash
# Check syntax
systemctl status str8tv-bot

# Test manually first
python3 str8tv_bot.py
```

---

## Pricing Comparison

| Platform | Cost | Ease | Best For |
|----------|------|------|----------|
| Railway | $5/month (free tier) | Easiest | Beginners |
| DigitalOcean | $6/month | Medium | Full control |
| Heroku | Deprecated | - | Don't use |

---

## Security Best Practices

1. **Never commit TOKEN to GitHub:**
   ```bash
   # Add to .gitignore
   echo "*.env" >> .gitignore
   ```

2. **Use environment variables for production**

3. **Keep server updated (DigitalOcean):**
   ```bash
   apt update && apt upgrade -y
   ```

4. **Enable firewall:**
   ```bash
   ufw allow 22/tcp
   ufw enable
   ```

---

## Next Steps

Bot deployed? Check **USER_GUIDE.md** to learn how to update FAQs, add videos, and manage your bot.
