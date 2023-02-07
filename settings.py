import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_V3_API = os.getenv('GOOGLE_V3_API')
YANDEX_API = os.getenv('YANDEX_API')
PATH_TO_FILE = os.getenv('PATH_TO_FILE')
MAP_GEOCODER = os.getenv('MAP_GEOCODER')