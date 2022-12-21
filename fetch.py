import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
# after Loggin in with Dicord -> store ACCOUNT_TOKEN as an encripted Cookie on the user's browser
acc = os.getenv("ACCOUNT_TOKEN")
print(os.getenv('ACCOUNT_TOKEN'))


def retrieve_messages(channel_id):
    headers = {
        'Authorization': f'{acc}'
    }
    r = requests.get(f"{os.getenv('API_ENDPOINT')}/channels/{channel_id}/messages", headers=headers)
    json_obj = json.loads(r.text)
    print(json_obj)


# test
retrieve_messages('901866925724930059')
