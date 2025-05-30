# ZeldrisRobot
# Copyright (C) 2017-2019, Paul Larsen
# Copyright (C) 2022, IDNCoderX Team, <https://github.com/IDN-C-X/ZeldrisRobot>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


if not __name__.endswith("config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = ""  # Take from @BotFather
    OWNER_ID = (
        "7742582171"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "bila_asarii"
    API_HASH = ""  # for purge stuffs
    API_ID = 29545467

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ""  # needed for any database modules
    MESSAGE_DUMP = "-1002230982823"  # needed to make sure 'save from' messages persist
    REDIS_URL = ""  # needed for afk module, get from redislab
    LOAD = ""
    NO_LOAD = "android"
    WEBHOOK = False
    URL = None
    MONGO_URI = ""
    MONGO_PORT = 27017  # leave it as it is
    MONGO_DB = "rubyhoshino"

    # OPTIONAL
    DEV_USERS = (
        [7842121452, 7967369452, 7133102095, 1454556602, 2005540797, 7858402613, 7436081160, 6565297804, 7213596810, 7608534850, 7013362810, 8193231031, 7010422153, 5987888780, 8020068489, 8148781195, 7722797664, 7763617262, 7742582171]
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        [7842121452, 7967369452, 7133102095, 1454556602, 2005540797, 7858402613, 7436081160, 6565297804, 7213596810, 7608534850, 7013362810, 8193231031, 7010422153, 5987888780, 8020068489, 8148781195, 7722797664, 7763617262, 7742582171]
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        [7842121452, 7967369452, 7133102095, 1454556602, 2005540797, 7858402613, 7436081160, 6565297804, 7213596810, 7608534850, 7013362810, 8193231031, 7010422153, 5987888780, 8020068489, 8148781195, 7722797664, 7763617262, 7742582171]
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = ""  # OpenWeather API
    SPAMWATCH_API = ""  # Your SpamWatch token
    WALL_API = ""
    SPAMMERS = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
