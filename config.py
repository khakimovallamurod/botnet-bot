from dotenv import load_dotenv
import os

load_dotenv()
def get_token():
    TOKEN = os.getenv("TOKEN")
    return TOKEN
def get_chatID():
    chat_id = os.getenv("chat_id")
    return chat_id
