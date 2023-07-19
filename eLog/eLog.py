import requests
import json
from datetime import datetime
import pytz
import os
import argparse
from . import payloads, data

class eLog:
    
    def __init__(self, filename):
        self.token = data.get_token()
        self.db_id = data.getDBid()
        if not self.token: 
            print(f'[!] eLog.py | No Notion API key found. Please run configure.py.')
            return
        if not self.db_id: 
            print(f'[!] eLog.py | No Notion database ID found. Please run configure.py.')
            return
        self.filename = filename
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json"
        }

    def find_entry(self, error):
        entries = json.loads(requests.post(f'https://api.notion.com/v1/databases/{self.db_id}/query', headers=self.headers).content)['results']
        for entry in entries:
            if not entry['properties']['Error']['rich_text']: continue
            if entry['properties']['Error']['rich_text'][0]['text']['content'].strip() == error.strip() and \
                entry['properties']['File']['rich_text'][0]['text']['content'].strip() == self.filename.strip():
                return entry['id'], entry['properties']['Count']['number']
        return None

    def update_entry(self, entry_id, error, cnt):
        url = f"https://api.notion.com/v1/pages/{entry_id}"
        payload = payloads.updateEntryPayload(error, cnt)
        r = requests.patch(url, headers=self.headers, json=payload)
        return r.status_code

    def create_entry(self, error):
        payload = payloads.createEntryPayload(self.db_id, error, self.filename)
        r = requests.post("https://api.notion.com/v1/pages/", headers=self.headers, json=payload)
        return r.status_code

    def log(self, error):
        try: entry_id, cnt = self.find_entry(error)
        except: entry_id = False
        if entry_id: return self.update_entry(entry_id, error, cnt)
        else: return self.create_entry(error)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="The filename to be processed")
    parser.add_argument("error", help="The error message to be logged")
    args = parser.parse_args()
    print(args.filename)
    print(args.error)
    logger = eLog(args.filename)
    status_code = logger.log(args.error)
    if status_code == 200: print(f'Logged error in {args.filename}:\n    {args.error}')
    else: print(f'Could not log error in {filename}:\n    {error}')
    return True if status_code == 200 else status_code

if __name__ == "__main__":
    logged = main()
    
