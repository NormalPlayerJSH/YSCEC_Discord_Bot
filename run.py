import discord
from discord.ext import commands
import asyncio, datetime, sys, os
from crawling import check

app=commands.Bot(command_prefix='.')

@app.event
async def on_ready():
    print('다음으로 로그인 합니다:',app.user.name)
    print('Connection Success')
    await app.change_presence(status=discord.Status.online,activity=None)

doLoop=False

@app.command()
async def 실행(ctx):
    print('started')
    print('Run by',ctx.author.id)
    global doLoop
    doLoop=True
    if ctx.author.dm_channel is None:
        await ctx.author.create_dm()
    while doLoop:
        await check(ctx)
        await asyncio.sleep(30)

@app.command()
async def 종료(ctx):
    global doLoop
    doLoop=False
    print('Terminating')

with open('secretData/token.txt', 'r') as f:
    token=f.readline()
app.run(token)
