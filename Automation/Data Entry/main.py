import os
from dotenv import load_dotenv

load_dotenv()
form_url = str(os.getenv("FORM_URL"))
zillow_url = str(os.getenv("ZILLOW_URL"))
