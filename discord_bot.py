import requests
import discord
import json
import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))
from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)

cluster = MongoClient("-")
db = cluster["yaku"]

collection_servers = db["servers"]
collection_users = db["users"]


@client.event
async def on_ready():
    print(f'The {client.user.name} BOT has started working.')

    for guild in client.guilds:
        s_roles = {}
        for role in guild._roles.values():
            if role.name != "@everyone":
                s_roles[role.id] = role.name
        for user in guild.members:
            u_roles = {}
            for role in user.roles:
                if role.name != "@everyone":
                    u_roles[role.id] = role.name
            collection_users.insert_one({"_id": user.id, "name": user.name, "roles": u_roles})
    collection_servers.insert_one({"_id": guild.id, "name": guild.name, "roles": s_roles})


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.channel.type)

    if message.channel.type.name == 'news':
        print(f'{message.author} said [{message.content}] in the news channel [{message.channel}].')


keep_alive()
client.run(os.getenv('TOKEN'))
