from resemble import Resemble
import os
from dotenv import load_dotenv


load_dotenv()
api_token = os.getenv('B2uOK6Cac0oo1r3frYJl7wtt')
api_token_key = Resemble.api_key(api_token)