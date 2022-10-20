import requests
import os


def exchange_code(code, redirect_uri):
    data = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % os.getenv('API_ENDPOINT'), data=data, headers=headers)
    r.raise_for_status()
    return r.json()


def refresh_token(refresh_token):
    data = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('%s/oauth2/token' % os.getenv('API_ENDPOINT'), data=data, headers=headers)
    r.raise_for_status()
    return r.json()


def add_to_guild(access_token, userID, guildID):
    url = f"{os.getenv('API_ENDPOINT')}/guilds/{guildID}/members/{userID}"
    data = {
        "access_token": access_token,
    }
    headers = {
        "Authorization": f"Bot {os.getenv('TOKEN')}",
        'Content-Type': 'application/json'
    }
    response = requests.put(url=url, headers=headers, json=data)
    print(response.text)
