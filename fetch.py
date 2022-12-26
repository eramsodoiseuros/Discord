import requests
import json
import os
from dotenv import load_dotenv
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import pymongo
import ssl

load_dotenv()
API_ENDPOINT = os.getenv('API_ENDPOINT')

# STEP 1 - Logging in with Discord to get ACCOUNT_TOKEN
acc = os.getenv("ACCOUNT_TOKEN")
print(os.getenv('ACCOUNT_TOKEN'))

# STEP 2 - Generate a random key
password = b"password"
salt = b"salt"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000
)
key = base64.urlsafe_b64encode(kdf.derive(password))

# STEP 3 - Encrypt ACCOUNT_TOKEN
fernet = Fernet(key)
message = acc
encrypted_message = fernet.encrypt(message.encode('utf-8'))

# STEP 4 - Store encrypted token as a Cookie on the user's browser

# STEP 5 - Decrypt the message
decrypted_acc_token = fernet.decrypt(encrypted_message).decode('utf-8')

# STEP 6 - Connect it to the Database
client = pymongo.MongoClient("YOUR_DOCUMENTDB_URI",
                             ssl=True,
                             ssl_cert_reqs=ssl.CERT_NONE,
                             authSource="admin",
                             authMechanism='SCRAM-SHA-1',
                             username='YOUR_DOCUMENTDB_USERNAME',
                             password='YOUR_DOCUMENTDB_KEY')

db = client["YOUR_DATABASE"]
servers_collection = db["servers"]
channels_collection = db["channels"]
messages_collection = db["messages"]


def retrieve_servers():
    """Returns a list of all user's servers"""
    headers = {
        "authorization": f"{decrypted_acc_token}",
        "User-Agent": "Yaku/0.1"
    }
    response = requests.get("https://discord.com/api/users/@me/guilds", headers=headers)

    if response.status_code == 200:
        servers = response.json()
        servers_collection.insert_many(servers)
        return servers
    else:
        print(response.json())


def retrieve_announcement_channels(server):
    """Returns a list of all announcement channels in server"""
    url = f"{API_ENDPOINT}/guilds/{server['id']}/channels"
    headers = {
        "authorization": f"{decrypted_acc_token}",
        "User-Agent": "Yaku/0.1"
    }
    response = requests.get(url, headers=headers)

    announcement_channels = []
    if response.status_code != 200:
        print(f"Failed to get list of channels from {server['name']}")
    else:
        for channel in response.json():
            # Filter the results to only include announcement channels (type 5)
            if channel["type"] == 5:
                announcement_channels.append(channel)
                channels_collection.insert_one(channel)
    return announcement_channels


def retrieve_messages(channel_id):
    """Returns a list of all messages in channel_id"""
    headers = {
        'authorization': f'{decrypted_acc_token}',
        "User-Agent": "Yaku/0.1"
    }

    response = requests.get(f"{API_ENDPOINT}/channels/{channel_id}/messages", headers=headers)
    messages = response.json()
    messages_collection.insert_many(messages)
    return messages


""" TESTING """
yaku = {
    "id": "889791853094912000",
    "name": "YAKU",
    "icon": "a94d8d1e2cd05613bf86a024a264369e",
    "owner": False,
    "permissions": 67488833,
    "features": [
        "ROLE_ICONS",
        "PREVIEW_ENABLED",
        "AUTO_MODERATION",
        "COMMUNITY",
        "APPLICATION_COMMAND_PERMISSIONS_V2",
        "ENABLED_DISCOVERABLE_BEFORE",
        "ANIMATED_ICON",
        "COMMUNITY_EXP_LARGE_GATED",
        "VANITY_URL",
        "NEWS",
        "MEMBER_VERIFICATION_GATE_ENABLED",
        "THREE_DAY_THREAD_ARCHIVE",
        "SEVEN_DAY_THREAD_ARCHIVE",
        "ANIMATED_BANNER",
        "MEMBER_PROFILES",
        "BANNER",
        "DISCOVERABLE",
        "PRIVATE_THREADS",
        "WELCOME_SCREEN_ENABLED",
        "INVITE_SPLASH"
    ],
    "permissions_new": "448891571265"
}

# servers_ = retrieve_servers()
# print(json.dumps(servers_, indent=4))

# announcement_channels_ = retrieve_announcement_channels(yaku)
# print(json.dumps(announcement_channels_, indent=4))

# messages = retrieve_messages("901866925724930059")  # dao-announcements
# print(json.dumps(messages, indent=4))