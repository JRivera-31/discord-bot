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
        
@client.event
async def on_member_join(member):
    print(member.name + " joined the server")
    try:
        await member.send("Welcome to The Hole " + member.name + "! Please see the rules in " +
        "announcements or type !rules in just-chatting")
    except:
        print("Couldn't send message")

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
       channel. Anything that violates rules 1 & 2 will be 
       removed.
    5. Please use the appropriate text/voice channels!

    Thank you!
    ```""")

client.run(BOT_TOKEN)