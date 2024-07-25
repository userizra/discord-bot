import os
import discord
from discord.ext import commands 

#import Bot token
from apikeys import *

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = '!', intents = intents) #initalize instance of bot and command prefix which is !


#Event is for when the bot detects it is ready
@client.event #When it detects something it does something else ie
async def on_ready():
     print("Dazai is now ready for use!") #print statement for when it works
     print("---------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello Bungo Stray Dogs fan")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye from Dazai")

@client.event
async def on_member_join(member):
    channel = client.get_channel(1132961069141336105)
    await channel.send("Welcome to IB Hive")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(1132961069141336105) #This is the channel tag used when on developer mode ie Community
    await channel.send("Sucks you left the best server ever")

client.run(BOT_TOKEN)