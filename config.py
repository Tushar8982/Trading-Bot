from binance.client import Client
from dotenv import load_dotenv
import os

def create_client():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    
    if not api_key or not api_secret:
        raise Exception("API_KEY or API_SECRET not found. Check your .env file.")
    
    return Client(api_key, api_secret, testnet=True)
