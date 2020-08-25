import discord
import os
from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    
    # Make sure bot is not responding to itself
    if message.author == client.user:
        return
        
    # check if a message was sent to memers channel
    if str(message.channel) == "😂-memers" and str(message.content) != "":
        await message.channel.purge(limit=1)

client.run(BOT_TOKEN)