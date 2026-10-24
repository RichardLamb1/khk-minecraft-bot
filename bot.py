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

import aiomcrcon
import discord
from discord.ext import commands
import json

# Load secrets
with open('secrets.json') as f:
    secrets = json.load(f)

# Load config
with open('config.json') as f:
    config = json.load(f)

# Register intents
intents = discord.Intents.default()
intents.message_content = True

# Register bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Connect to RCON
rcon = aiomcrcon.Client(
    host=config['server_address'],
    port=config['rcon_port'],
    password=secrets['rcon_password']
)

# Function to connect to RCON and execute a command
async def execute_rcon_command(command: str):
    # Try to connect to the RCON server
    try:
        await rcon.connect()
    except aiomcrcon.RCONConnectionError:
        print("An error occurred while connecting to the server.")
        return
    except aiomcrcon.IncorrectPasswordError:
        print("The provided RCON password was incorrect. Please check your secrets.json file.")
        return

    # Try to execute the RCON command
    try:
        out = await rcon.send_cmd(command)
        await rcon.close()
        return out[0]
    except Exception as e:
        await rcon.close()
        return out[0]

# Register command /khkmc
@bot.tree.command(name='khkmc')
async def _khkmc(interaction: discord.Interaction, arguments: str):
    # Split the string of arguments into a list of individual arguments
    args = arguments.split()
    action = args[0] if len(args) > 0 else None

    # Whitelist action
    if action == 'whitelist':
        subaction = args[1] if len(args) > 1 else None
        username = args[2] if len(args) > 2 else None
        if subaction == 'add' and username:
            out = await execute_rcon_command(f'whitelist add {username}')
            await interaction.response.send_message(f'```{out}```')
        elif subaction == 'remove' and username:
            out = await execute_rcon_command(f'whitelist remove {username}')
            await interaction.response.send_message(f'```{out}```')
        elif subaction == 'list':
            out = await execute_rcon_command('whitelist list')
            await interaction.response.send_message(f'```{out}```')
        else:
            await interaction.response.send_message('Invalid subcommand for whitelist.')

    # Command not found
    else:
        await interaction.response.send_message('Command not found or supported.')

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
