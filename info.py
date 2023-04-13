import re
import os
from os import environ
from Script import script 
from pyrogram import enums


import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class evamaria(Client):
    filterstore: Dict[str, Dict[str, str]] = defaultdict(dict)
    warndatastore: Dict[
        str, Dict[str, Union[str, int, List[str]]]
    ] = defaultdict(dict)
    warnsettingsstore: Dict[str, str] = defaultdict(dict)

    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir=TMP_DOWNLOAD_DIRECTORY,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            sleep_threshold=60
        )

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '16225550'))
API_HASH = environ.get('API_HASH', '160343c3d2eaf54b556ad5a7c72a3b83')
BOT_TOKEN = environ.get('BOT_TOKEN', "5312771340:AAFLFCgF0fEjP7ICx_dQjez2NNvCuN2feI0")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
# Welcome area
PICS = (environ.get('PICS', 'https://telegra.ph/file/3a1c31c86bb5c8c2dcfbf.jpg https://telegra.ph/file/573d2ac2615e0a11ecdd8.jpg https://telegra.ph/file/56c88fd799de1fdddcff5.jpg https://telegra.ph/file/64d8c4ccc44fea11c4953.jpg https://telegra.ph/file/273614c87ff4853c6c705.jpg https://telegra.ph/file/60b02b7b3b938ef38148a.jpg https://telegra.ph/file/6c58ccd1166e91d253de5.jpg https://telegra.ph/file/882d20b0a374b71de8534.jpg https://telegra.ph/file/11b5e79f90992c5f0f922.jpg https://telegra.ph/file/e0cec2ad83a635661b550.jpg https://telegra.ph/file/85a12855ceb53080553f6.jpg https://telegra.ph/file/f02f0f1e222fb2bb2b125.jpg https://telegra.ph/file/8d70dad72cd1fc4e345d8.jpg https://telegra.ph/file/8793f383b164e84c31f92.jpg https://telegra.ph/file/2d50b6fb671ca0170bc38.jpg https://telegra.ph/file/3089a5728b43d0373f1f0.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/225d02996e920bbf681ca.jpg")
MELCOW_PIC = environ.get("MELCOW_PIC", "https://telegra.ph/file/d31136c86dcc124e07272.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1345179077').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001827951140').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://pikachpatel:pikach432@pikachucluster.7cwyq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "pikachucluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
MONGO_URL = os.environ.get('MONGO_URL', "mongodb+srv://pikachpatel:pikach432@pikachucluster.7cwyq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '902284efd5e05828f51770d84f5ba26a6abf7751')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
S_GROUP = environ.get('S_GROUP',"")
RLU_LNK = environ.get('RLU_LNK', 'https://telegra.ph/GROUP-RULES-02-22')
GIT_LNK = environ.get('GIT_LNK', 'https://github.com/BLVCK-ANGEL')
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/mvie_max')
ANI_LNK = environ.get('ANI_LNK', 'https://t.me/mviemax_anime')
SER_LNK = environ.get('SER_LNK', 'https://t.me/mviemax_series')
CHNL_LNK = environ.get('CHNL_LNK', '')
MSG_ALRT = environ.get('MSG_ALRT', '⚠️ ᴘɪʀᴀᴄʏ ɪs ᴄʀɪᴍᴇ ⚠️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", 4)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
