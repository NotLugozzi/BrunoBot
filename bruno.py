#pogging
import os
import discord
from dotenv import load_dotenv
import random
from discord import voice_client

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "Everything is going to be okay, you'll be okay, just give it some time :)",
  "you're amazing",
  "i believe in you",
  "I'm so proud of you",
  "All our dreams can come true, if we have the courage to pursue them.",
  "Everything you can imagine is real.",
  "Whatever you are, be a good one.",
  "Do what you feel in your heart to be right – for you’ll be criticized anyway.",
  "You’ve gotta dance like there’s nobody watching, love like you’ll never be hurt, sing like there’s nobody listening, and live like it’s heaven on earth.",
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
        await message.channel.send('Jump in the cadillac,, girl let\'s put some miles on it')
        print('sent')
    elif message.content.startswith('$tommy'):
        await message.channel.send('Just killed a woman, feeling good')
        print('sent')
    elif message.content.startswith('$inspire me'):
       await message.channel.send(random.choice(starter_encouragements))
       print('sent')
    elif message.content.startswith('$puttane'):
       await message.channel.send("buongiorno zoccole sono Bruno")
       print('sent')
    elif message.content.startswith('$ash'):
       await message.channel.send("Ash is a fucking simp for ellie")
       print('sent')
    elif message.content.startswith('$ellie'):
       await message.channel.send("Ellie is my cute little baby:pleading_face:")
       print('sent')
    elif message.content.startswith('$greg'):
       await message.channel.send("Greg supersimp per vivi like smh sparati /j")
       print('sent')
    elif message.content.startswith('$simp'):
       await message.channel.send("https://cdn.discordapp.com/attachments/519271314373083204/820437716617265212/baby.jpg")
       print('sent')
client.run(os.getenv('TOKEN'))