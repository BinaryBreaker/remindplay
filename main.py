import os
import json

import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

users = {"test":[] }

print("Loading Steam Games from JSON")

games_s = []

f = open('steam_games.json')
games = json.load(f)

for x in range(1, 95810):
    games_s.append(games["applist"]["apps"][x]["name"])
    users[games["applist"]["apps"][x]["name"]]  = []

print (len(games_s))

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix="*")

@client.event
async def on_ready():
    print ("bot is ready")

@client.command()
async def dm(ctx):
    await ctx.author.send("owo")

@client.command()
async def ping(ctx):
    await ctx.send("pong (I was too lazy to add a time stamp)")

@client.command()
async def search_steam(ctx, *args):
    str_message_full = ''
    message_parm = args
    print (message_parm)
    for x in range(0, (len(message_parm))):
        if x != 0:
            str_message_full = str_message_full + " " + message_parm[x]
        else:
            str_message_full = message_parm[0]
    print(str_message_full)
    if str_message_full in games_s:
        await ctx.send("Game Exists")
    else:
        await ctx.send('Game Does Not Exist. Please enter the EXACT name (*search_steam Half-Life 2)')

@client.command()
async def add_game(ctx, *args):
    str_message_full = ''
    message_parm = args
    print(message_parm)
    for x in range(0, (len(message_parm))):
        if x != 0:
            str_message_full = str_message_full + " " + message_parm[x]
        else:
            str_message_full = message_parm[0]
    print(str_message_full)
    if str_message_full in games_s:
        await ctx.send("Game Exists")
        users.get(str_message_full).append(ctx.author)
        await ctx.send("Zuccsess")
    else:
        await ctx.send('Game Does Not Exist. Please enter the EXACT name (*search_steam Half-Life 2)')

@client.command()
async def notify(ctx, *args):
    str_message_full = ''
    message_parm = args
    print(message_parm)
    for x in range(0, (len(message_parm))):
        if x != 0:
            str_message_full = str_message_full + " " + message_parm[x]
        else:
            str_message_full = message_parm[0]
    print(str_message_full)
    if str_message_full in games_s:
        await ctx.send("Game Exists")
        for x in users.get(str_message_full):
            await x.send("{} wants to play {}".format(ctx.author, str_message_full))
    else:
        await ctx.send('Game Does Not Exist. Please enter the EXACT name (*search_steam Half-Life 2)')

@client.command()
async def commands(ctx):
    await ctx.send("*help : displays help")
    await ctx.send("*ping : displays a ping")
    await ctx.send("*search_steam [steam game] : displays if steam game exists")
    await ctx.send("*add_game [steam game] : adds yourself to the list of users for that game")
    await ctx.send("*notify [steam game] : notifies all users of that steam game that you want to play")

client.run(TOKEN)