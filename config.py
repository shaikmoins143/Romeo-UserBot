from os import getenv

API_ID = int(getenv("API_ID", "")) #optional
API_HASH = getenv("API_HASH", "") #optional

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_URL = getenv("MONGO_URL", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
LOG_GROUP = getenv("LOG_GROUP", "")
PM_LOGGER = getenv("PM_LOGGER", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5368154755").split()))
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Romeo-RJ/ROMEO-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a62b9c7d9848afde0569e.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "ʀᴏᴍᴇᴏʙᴏᴛ")
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
