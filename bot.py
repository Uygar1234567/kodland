import discord
import random
import os
from sifre_olusturucu import sifreolusturucu

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

async def sifre(ctx):
    yeni_sifre = sifreolusturucu(10)
    await ctx.send(f'Sifren bu: {yeni_sifre}!')

@bot.command()

async def heh(ctx, count_heh = 5):

    await ctx.send("he" * count_heh)

@bot.command()

async def mem(ctx):
    img_name=random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:

        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!

        images = discord.File(f)

   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!

    await ctx.send(file=images)
bot.run("MTI0Nzk2OTUxODk5NTg5ODQ1OQ.GDL6vW.mjwodcaxG-PJuDB6b_uHU0GlSYdKChbaJpNtJ0")




