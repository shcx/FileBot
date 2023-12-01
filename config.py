#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6712185386:AAENODSTMIsl9-4vaj0S3lzj2FrUi0EzL-k")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20608421"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dfd183bd459c45796aecc0f116cd17f5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002138656231"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1308798660"))

#Port
PORT = os.environ.get("PORT", "8451")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Harshu:Harshu@cluster0.idilqao.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "Harshu")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001418227130"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001421222864"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1048953852").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "✅𝙆𝙊𝙉𝙉𝙄𝘾𝙃𝙄𝙒𝘼 {first}\n\n• 𝙔𝙊𝙐 𝙉𝙀𝙀𝘿 𝙏𝙊 𝙅𝙊𝙄𝙉 4𝘾𝙃𝘼𝙉𝙉𝙀𝙇𝙎 1𝙎𝙏 [ 𝙅𝙊𝙄𝙉 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ] 𝙏𝙃𝙀𝙉\n\n• 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝘽𝙔 𝙏𝘼𝙋𝙋𝙄𝙉𝙂 𝙊𝙉 📥 𝙏𝙍𝙔 𝘼𝙂𝘼𝙄𝙉 📥\n\n• 𝙆𝙀𝙀𝙋 𝙎𝙐𝙋𝙋𝙊𝙍𝙏𝙄𝙉𝙂 ❤️</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "Files Bot From ACG ™️ [ @Anime_Chat_Group_ACG ]")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
