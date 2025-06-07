import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#---------------------------------------------------------------
#---------------------------------------------------------------         ,
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '9613996'))
API_HASH = environ.get('API_HASH', 'c02cb5be077027d44609486c0ac1fbc6')
BOT_TOKEN = environ.get('BOT_TOKEN', '5739123043:AAH9STFn52swMQEOisNf3PC42PbA1x4QJqE')
#---------------------------------------------------------------
#---------------------------------------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1729487047').split()]
USERNAME = environ.get('USERNAME', "https://t.me/letswatchrequest") # ADMIN USERNAME
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001717087987'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/letswatchnow01')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001750371143').split()]
#---------------------------------------------------------------
#---------------------------------------------------------------
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://case01f:zPi6Y2ZhtenyRwPf@watchit.ghjaoxy.mongodb.net/?retryWrites=true&w=majority&appName=Watchit")
DATABASE_NAME = environ.get('DATABASE_NAME', "Watchit")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
#---------------------------------------------------------------
#---------------------------------------------------------------
#----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '0'))  
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','0'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0'))
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '0'))
auth_channel = environ.get('AUTH_CHANNEL', '')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '0'))
request_channel = environ.get('REQUEST_CHANNEL', '0')
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '0'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/letswatchitnow') #Support group link ( make sure bot is admin )
#---------------------------------------------------------------
#---------------------------------------------------------------
IS_VERIFY = is_enabled('IS_VERIFY', True)
#---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bigsmall.in%2Fblogs%2Funique-gifts%2F20-shows-movies-to-binge-watch-over-the-weekend&psig=AOvVaw3ctKTx4Hn_brmA_Glui0Fb&ust=1749402747957000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIiJiaLn340DFQAAAAAdAAAAABAE")
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'omegalinks.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'omegalinks.in')
SHORTENER_API3 = environ.get("SHORTENER_API3", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'omegalinks.in')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))
#---------------------------------------------------------------
#---------------------------------------------------------------
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
#---------------------------------------------------------------
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
START_IMG = (environ.get('START_IMG', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bigsmall.in%2Fblogs%2Funique-gifts%2F20-shows-movies-to-binge-watch-over-the-weekend&psig=AOvVaw3ctKTx4Hn_brmA_Glui0Fb&ust=1749402747957000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIiJiaLn340DFQAAAAAdAAAAABAE')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bigsmall.in%2Fblogs%2Funique-gifts%2F20-shows-movies-to-binge-watch-over-the-weekend&psig=AOvVaw3ctKTx4Hn_brmA_Glui0Fb&ust=1749402747957000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIiJiaLn340DFQAAAAAdAAAAABAE')
REFER_PICS = (environ.get("REFER_PICS", "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bigsmall.in%2Fblogs%2Funique-gifts%2F20-shows-movies-to-binge-watch-over-the-weekend&psig=AOvVaw3ctKTx4Hn_brmA_Glui0Fb&ust=1749402747957000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIiJiaLn340DFQAAAAAdAAAAABAE")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bigsmall.in%2Fblogs%2Funique-gifts%2F20-shows-movies-to-binge-watch-over-the-weekend&psig=AOvVaw3ctKTx4Hn_brmA_Glui0Fb&ust=1749402747957000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIiJiaLn340DFQAAAAAdAAAAABAE')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bigsmall.in%2Fblogs%2Funique-gifts%2F20-shows-movies-to-binge-watch-over-the-weekend&psig=AOvVaw3ctKTx4Hn_brmA_Glui0Fb&ust=1749402747957000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIiJiaLn340DFQAAAAAdAAAAABAE'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
PORT = environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)

#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "")

#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
