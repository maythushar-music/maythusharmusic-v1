from maythushar.core.bot import Aviax
from maythushar.core.dir import dirr
from maythushar.core.git import git
from maythushar.core.userbot import Userbot
from maythushar.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
