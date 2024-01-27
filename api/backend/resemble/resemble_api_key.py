from resemble import Resemble
import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv('RESEMBLE_API_TOKEN')
Resemble.api_key(api_token)