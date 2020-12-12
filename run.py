import discord
from discord.ext import commands
import asyncio, datetime, sys, os

app=commands.Bot(command_prefix='.')

@app.event
async def on_ready():
    print('다음으로 로그인 합니다:',app.user.name)
    print('Connection Success')
    await app.change_presence(status=discord.Status.online,activity=None)

#app.run('Nzg3MDg4MzA1OTgzNDU1MjUy.X9P3Gw.feZhZ18EAhSqUwW_O6VyTrYWKTo')

doLoop=False

@app.command()
async def 실행(ctx):
    print('started')
    #await app.wait_until_ready()
    #channel=discord.Object(id='787087196414804000')
    counter=1
    await ctx.send("Hello, World")
    print('Run by',ctx.author.id)
    global doLoop
    doLoop=True
    if ctx.author.dm_channel is None:
        await ctx.author.create_dm()
    while doLoop:
        await ctx.author.dm_channel.send(str(counter)+str(doLoop))
        counter+=1
        await asyncio.sleep(5)

@app.command()
async def 종료(ctx):
    global doLoop
    doLoop=False
    print('Terminating')

app.run('Nzg3MDg4MzA1OTgzNDU1MjUy.X9P3Gw.feZhZ18EAhSqUwW_O6VyTrYWKTo')
