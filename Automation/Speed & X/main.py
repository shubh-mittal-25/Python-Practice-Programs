import os
from dotenv import load_dotenv

load_dotenv()
email = str(os.getenv("Y_EMAIL"))
password = str(os.getenv("Y_PASSWORD"))
UPLOAD_SPEED = 100
DOWNLOAD_SPEED = 100