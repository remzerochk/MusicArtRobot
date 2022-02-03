from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("5298446554:AAEED-6GXxC_WxRyNXgz6Hk_FdLs2XJ43V4")
API_ID = int(getenv("15496152", ""))
API_HASH = getenv("6fc8da58e058f700fe4e81b9d15f0617")
DURATION_LIMIT_MIN = int(getenv("60", "10"))
ASSISTANT_PREFIX = list(getenv("/", ".").split())
MONGO_DB_URI = getenv("mongodb+srv://Greninja:qwerty123@dabi.rjgbu.mongodb.net/Cluster0?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("2087717046 2108356386 1789859817", "").split()))
OWNER_ID = list(map(int, getenv("2125081807", "").split()))
LOG_GROUP_ID = int(getenv("-1001775910981", ""))
MUSIC_BOT_NAME = getenv("MusicArt")
HEROKU_API_KEY = getenv("4a7b14d7-54aa-4779-bc49-9f6f057ad0ea")
HEROKU_APP_NAME = getenv("MusicArt")

#UPSTREAM_REPO = getenv(https://github.com/NotReallyShikhar/YukkiMusicBot
#    "UPSTREAM_REPO", "https://github.com/NotReallyShikhar/YukkiMusicBot"
#)
#UPSTREAM_BRANCH = getenv("Master", "master")

if str(getenv("https://t.me/MarinXUpdates")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("https://t.me/MarinXUpdates"))
if str(getenv("https://t.me/MarinXSupport")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("https://t.me/MarinXSupport"))


if str(getenv("MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/ +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9 t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/ +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9 t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/ +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9 t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g 5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO 62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/ +aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9 t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs 5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB"))
