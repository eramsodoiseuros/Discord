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
