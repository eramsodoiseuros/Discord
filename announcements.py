import discord
import random

TOKEN = 'MTAzMTU2MTk0NzEwMTAwNzkwMg.GaOuAy.GW47kR0wDf9OBUMgjxC1fgePGx77SpknmOdjH0'

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]

  if message.channel.name == 'announcements':
    
client.run(TOKEN)