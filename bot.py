import discord
from discord.ext import commands
from discord.flags import SystemChannelFlags
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='[', intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online2<<")

@bot.event      #join
async def on_member_join(member):
    #print(f'{member} join!')
    channel = bot.get_channel(844991915135860758)
    await channel.send(f'{member} join!')

@bot.event      #leave
async def on_member_remove(member):
    #print(f'{member} leave!')
    channel = bot.get_channel(844991915135860758)
    await channel.send(f'{member} leave!')

bot.run('ODQ0NjI3OTY2MDgzMzM0MjE0.YKVLFw.X2vwl1QbAbmVHZnHmlyxsmiVq6Q')