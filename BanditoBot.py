import discord
import os

from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands

# Grab bot token from .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
BOT_TOKEN = os.environ.get("BOT_TOKEN")

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

async def on_message(message):
    message.content = message.content.lower()
    
    # Make sure bot is not responding to itself
    if message.author == client.user:
        return
        
    # check if a message with text was sent to memers channel
    if str(message.channel) == "😂-memers" and str(message.content) != "":
        # delete the message
        await message.channel.purge(limit=1)

@client.command()
async def ping(ctx):
    await ctx.send(f'Bot ping: {round(client.latency * 1000)}ms')

@client.command()
async def rules(ctx):
    await ctx.send("""```THE RULES
    1. Be respectful.
    2. No blatant racism please.
    3. Feel free to link your stream when you go 
       live in streamers only.
    4. Feel free to post your clips in the clips 
       channel. Anything that violates these rules will be 
       removed.
    5. Please use the appropriate text/voice channels!

    Thank you!
    ```""")

client.run(BOT_TOKEN)