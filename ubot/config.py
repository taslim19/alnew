import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    1889281820, #al27
    1054295664, #ommkeenan
    1087819304, #ezaa
]

KYNAN = list(map(int, os.getenv("KYNAN", "816526222 1054295664 5013987239 5357942628 1898065191 482945686").split()))

API_ID = int(os.environ.get("API_ID", "23855532"))

API_HASH = os.environ.get("API_HASH", "3cc6eac0a9fbfe0b2b1da77f043cc9c9")

LOG_SELLER = int(os.getenv("LOG_SELLER", "-1001964273937"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001608847572 -1001538826310 -1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001861414061").split()))

USER_ID = list(map(int, os.getenv("USER_ID", "1054295664 482945686 816526222").split()))

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "",
).split()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6472140315:AAGfnrPpvTadDhwT0dM8_MQMON2-GIQrklk")

OWNER_ID = int(os.environ.get("OWNER_ID", "1889281820"))

MAX_BOT = int(os.environ.get("MAX_BOT", "30"))

SKY = int(os.environ.get("SKY", "-1001967160939"))

MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb+srv://kingex:hx7vMVs1iM9EmaKy@kingex.x4ighmk.mongodb.net/?retryWrites=true&w=majority",
)
