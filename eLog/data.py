import os

def get_token():
    ENV_TOKEN=False
    try: ENV_TOKEN = os.getenv('NOTION_TOKEN') 
    if not ENV_TOKEN: print(f"[!] eLog | Token not found. Have you ran configure.py?")
    return ENV_TOKEN

def getDBid():
    ENV_ID=False
    try: ENV_ID = os.getenv('NOTION_DB_ID') 
    except: pass
    if not ENV_ID: print(f"[!] eLog | Notion page not found. Have you ran configure.py?")
    return ENV_ID
