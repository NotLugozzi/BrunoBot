#pogging
import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "Everything is going to be okay, you'll be okay, just give it some time :)",
  "You're real and you deserve this",
  "I'm so proud of you",
]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
#message body
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bruno'):
        print('jumpin')
        await message.channel.send('Jump in the cadillac,, girl let\'s put some miles on it')
        print('sent')
    elif message.content.startswith('$tommy'):
        print('oi dickhead')
        await message.channel.send('Just killed a woman, feeling good')
        print('sent')
    elif message.content.startswith('$help'):
       print('it\'ll be okay')
       await message.channel.send(random.choice(starter_encouragements))
       print('sent')
client.run(os.getenv('TOKEN'))