
from dotenv import load_dotenv
import os

load_dotenv()

def get_credentials():
    return os.getenv("EMAIL"), os.getenv("SENHA")
