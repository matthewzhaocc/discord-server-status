#a discord bot for playing with CICD
#system dependencies
import os

#3rd party dependencies
import discord

TOKEN = os.environ.get("DISCORD_API_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)