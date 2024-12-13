import discord
from discord.ext import commands
from bot_logic import gen_pass, flip_coin, gen_emoji, current_date, current_time, addition, subtraction, moltiplication, division

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def come_stai(ctx):
    await ctx.send("Bene")

@bot.command()
async def password(ctx, count_password = 5):
    await ctx.send(gen_pass(count_password))

@bot.command()
async def moneta(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def data(ctx):
    await ctx.send(current_date())

@bot.command()
async def ora(ctx):
    await ctx.send(current_time())

@bot.command()
async def addizione(ctx, a, b):
    await ctx.send(addition(a, b))

@bot.command()
async def sottrazione(ctx, a, b):
    await ctx.send(subtraction(a, b))

@bot.command()
async def moltiplicazione(ctx, a, b):
    await ctx.send(moltiplication(a, b))

@bot.command()
async def divisione(ctx, a, b):
    await ctx.send(division(a, b))

bot.run("TOKEN")
