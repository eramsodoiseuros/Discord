import discord
import os

from keep_alive import keep_alive
from dotenv import load_dotenv
from pymongo import MongoClient

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

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


collection_announcements = db["announcements"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.channel.type)

    if message.channel.type.name == 'news':
        collection_announcements.insert_one({"_id": message.id, "author": message.author, "server_id": message.guild.id,
                                           "server_name": message.guild.name, "channel": message.channel, "content": message.content})



keep_alive()
client.run(os.getenv('TOKEN'))
