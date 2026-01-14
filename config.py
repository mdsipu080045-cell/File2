# 🗿  Visit & Support us - @newmoviesabbir
# ⚡️ Do Not Remove Credit - Made by @newmoviesabbir
# 💬 For Any Help Join Support Group: @all_anime_in_hindi_dub1
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import re
from os import environ


id_pattern = re.compile(r'^-?\d+$')


SESSION = environ.get("SESSION", "UHDFiletoLinksBot")

# আপনার দেওয়া তথ্যগুলো নিচে বসানো হয়েছে
API_ID = int(environ.get("API_ID", "29608422"))
API_HASH = environ.get("API_HASH", "3db2f8e109301f02f5d9c8f10dd79244")
BOT_TOKEN = environ.get("BOT_TOKEN", "8560160655:AAHzkz6R3aoKeAqu_XYoxUqTJ9pmUz0QrtI")


PORT = int(environ.get("PORT", "8080"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "") # এখানে আপনার Render বা Heroku অ্যাপের লিঙ্ক দিতে পারেন


LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003360104781"))
ADMINS = [
    int(admin) if id_pattern.match(admin) else admin
    for admin in environ.get("ADMINS", "8056243176").split()
]


DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://mdohidh20:emETBcodRUOnB69C@movienamerequest.smfx6uk.mongodb.net/?retryWrites=true&w=majority&appName=Movienamerequest")
DATABASE_NAME = environ.get("DATABASE_NAME", "Movienamerequest")
