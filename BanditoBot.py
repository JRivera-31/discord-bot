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

# for events
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

# for commands
@client.command()
async def test(ctx):
    await ctx.send("This is a test")

client.run(BOT_TOKEN)