from geopy import GoogleV3
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


google_geocoder = GoogleV3(api_key=os.getenv('GOOGLE_V3_API'), domain='maps.google.ru')
random_place = 'проспект Ленина, 18Б Центр район, Петрозаводск, 185035'
geocoded = google_geocoder.geocode('проспект Ленина, 18Б Центр район, Петрозаводск, 185035')
pprint(geocoded.raw)
