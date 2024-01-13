import discord
from discord.ext import commands 

app = commands.Bot(command_prefix='!!',intents=discord.Intents.all())

@app.event
async def on_ready():
   print(f"[라디오봇] LOGIN SUCCESSED")
   activity = discord.Activity(type=discord.ActivityType.listening,name='라디오')
   await app.change_presence(status=discord.Status.online,activity=activity)

app.load_extension("Cogs.radio")

app.run('token')