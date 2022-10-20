import requests
import random
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
    print(f'The {client.user.name} BOT has started.')


@client.event
async def on_message(message):

<<<<<<< Updated upstream
  if message.channel.name == 'announcements':
    
@client.command()
async def hi(ctx):
    with open('users.txt','w') as f:
        async for member in ctx.guild.fetch_members(limit=None):
            print("{},{}".format(member,member.id), file=f,)
    print("done")
    
@client.command()
async def info(ctx, user: discord.Member):

    mention = []
    for role in user.roles:
        if role.name != "@everyone":
            mention.append(role.mention)

    b = ", ".join(mention)


    embed = discord.Embed(title="Info:", description=f"Info of: {user.mention}", color=discord.Color.orange())
    embed.add_field(name="Top role:", value=user.top_role)
    embed.add_field(name="Roles:", value=b)

    await ctx.send(embed=embed)
    
client.run(TOKEN)
=======
    if message.author == client.user:
        return

    msg = message.content
    print(msg)

    if message.channel.name == 'announcements':
        username = str(message.author).split('#')[0]
        await message.channel.send(f'{username} said {msg}.')

    if message.channel.name == 'general':
        username = str(message.author).split('#')[0]
        await message.channel.send(f'> {message.author} said something in {message.channel}'
                                   f'\n```{message}```'
                                   f'\n> {message.content}')


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


keep_alive()
client.run(os.getenv('TOKEN'))
>>>>>>> Stashed changes
