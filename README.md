# KHK Minecraft Bot

A simple Discord bot that allows you to manage the whitelist on the KHK
Minecraft server.

KHK Minecraft Bot runs on a Raspberry Pi connected to the same local area
network as the Minecraft server. The bot listens for commands in the KHK Discord
server and executes them over RCON to manage the server's whitelist.

## Initial Setup

It is highly recommended that you use a Python virtual environment for the
backend. To create one, run:

```
python3 -m venv venv &&
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Copy `sample-secrets.json` to `secrets.json` and edit your configuration:

  - `bot_token`: The secret token from the Discord developer portal
  - `rcon_password`: The RCON password as defined in the `server.properties`
    file

It is recommended that you change permissions on your `secrets.json` file to
prevent other users from reading it (ie. `chmod 600 secrets.json`).

Copy `sample-config.json` to `config.json` and edit your configuration:

  - `server_address`: The Minecraft server's IP address or hostname
  - `rcon_port`: The RCON port as defined in the `server.properties` file

Start your bot:

```
python3 bot.py
```

## Supported Commands

  - `/khkmc list`
  - `/khkmc whitelist add <username>`
  - `/khkmc whitelist remove <username>`
  - `/khkmc whitelist list`
