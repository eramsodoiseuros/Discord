import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def retrieve_messages(channel_id):
    headers = {
        'Authorization': f'{os.getenv("ACCOUNT_TOKEN")}'
    }
    r = requests.get(f"{os.getenv('API_ENDPOINT')}/channels/{channel_id}/messages", headers=headers)
    json_obj = json.loads(r.text)
    print(os.getenv('ACCOUNT_TOKEN'))
    print(json_obj)


# test
retrieve_messages('901866925724930059')
