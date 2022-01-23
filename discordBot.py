import discord
import random
import os

TOKEN = "ODEyMDgyNzM3MTg2OTk2Mjg1.YC7k_A.ldx_vnw47MDejWjT-a_ufn4K--U"

#Vi lister opp alle memes i et array.
MEMES = os.listdir("meme")

client = discord.Client()

@client.event
async def on_ready():
  #Vi lager en sjekk som bekrefter at vi får logget inn & status.
    print("Vi har logget inn som {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!hjelp for hjelp"))

@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  print(f"{username}: {user_message}")

  if message.author == client.user:
    return
    
  if user_message.lower() == 'hei kekbot':
    await message.channel.send(f'uwu hei {username}')
    return
  if user_message.lower() == '!meme':
    await message.channel.send("jeg elsker mems:3", file=discord.File(f"meme/{random.choice(MEMES)}"))
    return
  if username == 'ThorBear':
    await message.channel.send(f"hold kjeft Torbjørn")
  elif username == 'JenMol':
    await message.channel.send(f"hold kjeft Jens")

  if user_message.lower() == '!hjelp':
    await message.channel.send(' ```Foreløpig har jeg kunn !meme``` ')


client.run(TOKEN)
