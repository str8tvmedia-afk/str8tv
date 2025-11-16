# Str8TV Media - Telegram Customer Support Bot

Professional Telegram bot for handling customer support, FAQs, and live agent forwarding for Str8TV Media IPTV service.

---

## Features

✅ **Automated Q&A System**
- General information about IPTV service
- Billing and subscription details
- Technical support responses
- VPN recommendations

✅ **Setup Video Tutorials**
- TiviMate setup guides
- IPTV Smarters instructions
- Firestick installation videos
- Easy video link management

✅ **Live Agent Forwarding**
- Keyword-triggered support requests
- Direct admin notifications
- User info included (username, ID, message)

✅ **Smart Keyword Detection**
- Auto-replies based on user questions
- Multiple keyword triggers per category
- Natural language support

✅ **Professional Branding**
- Custom logo on welcome message
- Branded responses with emojis
- Interactive menu system

---

## Quick Start

### 1. Setup (5 minutes)
Follow **[SETUP.md](SETUP.md)** to:
- Create your bot with BotFather
- Get your admin chat ID
- Configure TOKEN and ADMIN_CHAT_ID
- Add your video tutorial links

### 2. Deploy (10 minutes)
Follow **[DEPLOYMENT.md](DEPLOYMENT.md)** to:
- Deploy to Railway (easiest) OR DigitalOcean
- Run bot 24/7
- Monitor with logs

### 3. Manage (ongoing)
Follow **[USER_GUIDE.md](USER_GUIDE.md)** to:
- Update FAQs and responses
- Add/change video tutorials
- Customize keywords
- Handle live support requests

---

## File Structure

```
iptv-hosting-service/
├── str8tv_bot.py          # Main bot code
├── SK-Logo-02-01.jpeg     # Your logo
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment config
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── SETUP.md              # Setup instructions
├── DEPLOYMENT.md         # Deployment guide
└── USER_GUIDE.md         # Management guide
```

---

## Requirements

- Python 3.8+
- python-telegram-bot 20.8
- Telegram Bot Token (from @BotFather)
- Your Telegram User ID

---

## Installation

### Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Configure bot
# Edit str8tv_bot.py and add:
# - TOKEN
# - ADMIN_CHAT_ID
# - Video links

# Run bot
python3 str8tv_bot.py
```

### Production Deployment

**Option 1: Railway (Recommended)**
- Push to GitHub
- Connect to Railway
- Automatic deployment

**Option 2: DigitalOcean**
- Create Ubuntu droplet
- Setup systemd service
- 24/7 operation

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for detailed instructions.

---

## Bot Commands

### User Commands
- `/start` - Show welcome message and menu

### Menu Options
1. **General Info** - Service overview
2. **Subscriptions & Billing** - Plans and payment
3. **Setup Help** - Installation instructions
4. **Setup Videos** - Video tutorials
5. **Troubleshooting** - Common issues
6. **Contact Support** - Live agent request

### Keyword Auto-Replies
The bot automatically responds to messages containing keywords:

| Keywords | Response |
|----------|----------|
| price, billing, payment | Billing info |
| setup, install, tivimate | Setup instructions + videos |
| buffer, freeze, error | Troubleshooting steps |
| vpn, privacy | VPN recommendations |
| help, talk to someone | Live agent forwarding |

---

## Customization

### Change Welcome Message
Edit lines 30-32 in `str8tv_bot.py`

### Update FAQ Responses
Edit the `responses` dictionary (lines 54-97)

### Add Video Tutorials
Edit the `videos` response (lines 74-83)

### Add Keywords
Edit the `auto_reply` function (lines 111-155)

### Change Logo
Replace `SK-Logo-02-01.jpeg` with your image

Full customization guide: **[USER_GUIDE.md](USER_GUIDE.md)**

---

## Testing

### Syntax Check
```bash
python3 -m py_compile str8tv_bot.py
```

### Local Testing
```bash
python3 str8tv_bot.py
# Open Telegram and search for your bot
# Send /start and test all features
```

### Production Testing
1. Send `/start` - verify welcome + logo
2. Click each menu button
3. Type keywords (e.g., "billing", "help")
4. Test live support forwarding

---

## Monitoring

### Check Bot Status

**Telegram:**
Send `/start` to your bot

**Railway:**
Dashboard → Logs tab

**DigitalOcean:**
```bash
systemctl status str8tv-bot
journalctl -u str8tv-bot -f
```

### Common Issues

| Issue | Solution |
|-------|----------|
| Bot not responding | Check TOKEN, restart bot |
| Logo not showing | Verify file path and name |
| Live support not working | Check ADMIN_CHAT_ID |
| Changes not showing | Restart bot after edits |

Full troubleshooting: **[USER_GUIDE.md](USER_GUIDE.md)**

---

## Security Notes

⚠️ **Never commit your TOKEN to GitHub**
- Use environment variables for production
- Add sensitive files to `.gitignore`
- Keep TOKEN secret

✅ **Best Practices:**
- Use environment variables on Railway
- Restrict SSH access on DigitalOcean
- Keep dependencies updated
- Monitor logs regularly

---

## Support & Documentation

📖 **Documentation:**
- [SETUP.md](SETUP.md) - Initial configuration
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deploy to cloud
- [USER_GUIDE.md](USER_GUIDE.md) - Day-to-day management

🔗 **Resources:**
- Telegram Bot API: https://core.telegram.org/bots/api
- python-telegram-bot: https://python-telegram-bot.org
- Railway: https://railway.app
- DigitalOcean: https://www.digitalocean.com

---

## Project Details

**Created for:** Str8TV Media IPTV Service
**Purpose:** Automated customer support
**Language:** Python 3.8+
**Framework:** python-telegram-bot
**Deployment:** Railway / DigitalOcean

---

## License

This bot was custom-developed for Str8TV Media. For questions or modifications, contact the developer.

---

## Changelog

### Version 1.0 (Initial Release)
- ✅ Automated Q&A system
- ✅ Menu-based navigation
- ✅ Video tutorial integration
- ✅ Keyword auto-replies
- ✅ Live agent forwarding
- ✅ Logo integration
- ✅ Complete documentation

---

**Ready to get started?** Follow [SETUP.md](SETUP.md) for configuration instructions!
