#!/usr/bin/env python3

import sys
from discord.ext import commands
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description="Gets Minecraft server info")
async def server(address: str):
    response = info(address)
    await bot.say(response)

def info(address: str):
    minecraft_server = MinecraftServer.lookup(address)
    try:
        status = minecraft_server.status()
        response = "{} has {} players online and replied in {} ms"\
        .format(address, status.players.online, status.latency)
        if status.players.online != 0:
            query = minecraft_server.query()
            response += "\nThe server has the following players online: \n {}"\
            .format("\n ".join(query.players.names))
    except IOError:
        response = "{} is off, has queries disabled or it doesn't exist".format(address)
    finally:
        return response

try:
    with open("token.txt", "r") as f:
        token = f.readline()
except IOError:
    print("Token file not found.")
    sys.exit(1)

bot.run(token)
