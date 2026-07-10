import os
from dotenv import load_dotenv

load_dotenv()
username = str(os.getenv("SAN_EMAIL"))
password = str(os.getenv("SAN_PASSWORD"))
SIMILAR_ACCOUNT = ("chefsteps")
URL = "https://app.100daysofpython.dev/services/share-a-naan"