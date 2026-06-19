from pprint import pprint
from data_manager import DataManager
import requests_cache

requests_cache.install_cache("flight_cache", expire_after=3600)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)
