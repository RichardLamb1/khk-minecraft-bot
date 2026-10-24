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

bot = commands.Bot(command_prefix='!', intents=intents)

# Register command /khkmc
@bot.tree.command(name='khkmc')
async def _khkmc(interaction: discord.Interaction, arguments: str):
    args = arguments.split()
    action = args[0] if len(args) > 0 else None
    if action == 'whitelist':
        subaction = args[1] if len(args) > 1 else None
        username = args[2] if len(args) > 2 else None
        if subaction == 'add' and username:
            await interaction.response.send_message(f'Adding {username} to the whitelist...')
            # Add RCON logic here
        elif subaction == 'remove' and username:
            await interaction.response.send_message(f'Removing {username} from the whitelist...')
            # Add RCON logic here
        elif subaction == 'list':
            await interaction.response.send_message('Listing whitelist...')
            # Add RCON logic here
        else:
            await interaction.response.send_message('Invalid subcommand for whitelist.')
    else:
        await interaction.response.send_message('Invalid command.')

# Attempt to log in to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        await bot.tree.sync()
        print('Command tree synced successfully.')
    except Exception as e:
        print(f'Failed to sync command tree: {e}')

# Run the bot
bot.run(secrets['bot_token'])
