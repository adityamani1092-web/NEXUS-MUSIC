from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_URI, MONGO_DB_NAME

_client = AsyncIOMotorClient(MONGO_URI)
db = _client[MONGO_DB_NAME]

# Collections used across the bot's storage modules
sudo_col = db["sudo_users"]
gban_col = db["gban_users"]
settings_col = db["chat_settings"]
warnings_col = db["warnings"]
playlist_col = db["playlists"]

auth_col = db["authorized_music_users"]
autoplay_col = db["chat_autoplay"]
