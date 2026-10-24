'''
KHK Minecraft Bot - A simple bot that allows you to manage the whitelist on the
KHK Minecraft server.

KHK Minecraft Bot runs on a Raspberry Pi connected to the same local area
network as the Minecraft server. The bot listens for commands in the KHK Discord
server and executes them over RCON to manage the server's whitelist.

Supported Commands:
  - /khkmc whitelist add <username>
  - /khkmc whitelist remove <username>
  - /khkmc whitelist list

@author Richard Lamb <rllamb@wisc.edu>
'''

import discord
from discord.ext import commands
import json

# Load secrets
with open('secrets.json') as f:
    secrets = json.load(f)

# Load config
with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(secrets['bot_token'])
