import discord
import random
from kodland_utils import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def rps(ctx, *args):
    choices = ['rock', 'paper', 'scissors']
    user_choice = "".join(args).lower()
    bot_choice = random.choice(choices)

    if user_choice not in choices:
        await ctx.send("Please choose either rock, paper, or scissors.")
        return

    if user_choice == bot_choice:
        result = "It's a draw!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    await ctx.send(f"Your choice: {user_choice}\nBot's choice: {bot_choice}\n{result}")

@bot.command()
async def pass_gen(ctx, length):
    if length.isdigit():
        length = int(length)
        
        await ctx.send(gen_pass(length))
    else:
        await ctx.send("enter a number")

@bot.command()
async def flip(ctx):

    await ctx.send(flip())

@bot.command()
async def random_emoji(ctx):

    await ctx.send(random_emoji())

bot.run()
