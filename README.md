# KHK Minecraft Bot

A simple bot that allows you to manage the whitelist on the KHK Minecraft
server.

KHK Minecraft Bot runs on a Raspberry Pi connected to the same local area
network as the Minecraft server. The bot listens for commands in the KHK Discord
server and executes them over RCON to manage the server's whitelist.

## Initial Setup

Copy `sample-secrets.json` to `secrets.json` and paste your bot token from the
Discord developer portal inside.

Copy `sample-config.json` to `config.json` and edit your configuration:

  - `server_address`: The Minecraft server's IP address or hostname
  - `rcon_port`: The RCON port as defined in the `server.properties` file

## Supported Commands

  - `/khkmc whitelist add <username>`
  - `/khkmc whitelist remove <username>`
  - `/khkmc whitelist list`