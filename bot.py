from asyncio.tasks import wait
import discord
import json
from discord.ext import commands
from discord.flags import SystemChannelFlags
intents = discord.Intents.default()
intents.members = True

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='[', intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event      #join
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(844991915135860758)
    await channel.send(f'{member} join!')

@bot.event      #leave
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(844991915135860758)
    await channel.send(f'{member} leave!')


@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}(ms)')

@bot.command()
async def pig(ctx):
    await ctx.send('你才豬，你全家都是豬')

bot.run(jdata['TOKEN'])