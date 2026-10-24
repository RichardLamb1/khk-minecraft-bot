# KHK Minecraft Bot

A simple Discord bot that allows you to manage the whitelist on the KHK
Minecraft server.

KHK Minecraft Bot runs on a Raspberry Pi connected to the same local area
network as the Minecraft server. The bot listens for commands in the KHK Discord
server and executes them over RCON to manage the server's whitelist.

## Initial Setup

Copy `sample-secrets.json` to `secrets.json` and edit your configuration:

  - `bot_token`: The secret token from the Discord developer portal
  - `rcon_password`: The RCON password as defined in the `server.properties`
    file

It is recommended that you change permissions on your `secrets.json` file to
prevent other users from reading it (ie. `chmod 600 secrets.json`).

Copy `sample-config.json` to `config.json` and edit your configuration:

  - `server_address`: The Minecraft server's IP address or hostname
  - `rcon_port`: The RCON port as defined in the `server.properties` file

## Supported Commands

  - `/khkmc whitelist add <username>`
  - `/khkmc whitelist remove <username>`
  - `/khkmc whitelist list`
