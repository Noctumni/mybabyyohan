import discord
from discord.ext import commands
import utils
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="owo ", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def owoify(ctx, *, text):
    await ctx.send(utils.owoify(text))

bot.run("MTM3MjkzMzQ0OTE1Mjg1NjIyNA.G6YhNR.qMHbJXCSCnnK9ZfMnOYP0lGG9isF13GjX9BKQY")