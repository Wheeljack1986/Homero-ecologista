import discord
import random
import os
from botlogic2 import *
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"⚠️ La contaminación también es causada por: {conta()}")

@bot.command()
async def reciclables(ctx):
    await ctx.send(recicla)

@bot.command()
async def no_reciclables(ctx):
    await ctx.send(no_reci)

@bot.command()
async def descomposicion(ctx):
    await ctx.send(desco)

@bot.command()
async def manualidades(ctx):
    liste = os.listdir("manualidades")
    img_nome = random.choice(liste)
    with open(f'manualidades/{img_nome}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)    

@bot.command()
async def formas_de_no_contaminar(ctx):
    await ctx.send(f"Las formas de no contaminar son: {no_conta()}")
    
@bot.command()
async def help_(ctx):
    await ctx.send(help_message)
    
bot.run("tu token")
