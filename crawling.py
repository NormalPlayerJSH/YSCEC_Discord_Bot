import discord
from discord.ext import commands
import asyncio, datetime, sys, os
import pickle

async def check(ctx):
    id=ctx.author.id
    dm_channel=ctx.author.dm_channel
    await dm_channel.send(f'Now running for ID {ctx.author.id}')
    with open('data.dat','rb') as f:
        infoDict=pickle.load(f)
    await dm_channel.send(f"Hello, {infoDict[id]['ID']}")
