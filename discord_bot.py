import requests
import discord
import json
import os
from dotenv import load_dotenv

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))
from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'The {client.user.name} BOT has started working.')
    roles = {}
    members = {}
    for guild in client.guilds:
        for role in guild._roles.values():
            if role.name != "@everyone":
                roles[role.id] = (guild.name, guild.id, role.name)
        for user in guild.members:
            members[user.id] = (guild.name, guild.id, user.name)

    print(members)
    print(roles)

# we can listen to any channel
channels_to_read = ['announcements']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name in channels_to_read:
        print(f'{message.author} said [{message.content}] in [{message.channel}].')


keep_alive()
client.run(os.getenv('TOKEN'))

