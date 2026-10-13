import discord
from discord.ext import commands
from colorama import Fore
import config
import random
from car import Car

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

sohbet_edilen = None


@bot.event
async def on_ready():
    print(f"{Fore.GREEN}Bot giriş yaptı: {Fore.YELLOW}{bot.user}")
    print(Fore.RESET)


@bot.event
async def on_message(message):
    global sohbet_edilen

    if message.author == bot.user:
        return

    if sohbet_edilen is not None and message.author == sohbet_edilen:
        if "nasılsın" in message.content.lower():
            await message.channel.send("İyiyim, sen nasılsın?")

    await bot.process_commands(message)


@bot.command(help="Sizi selamlar :D")
async def merhaba(ctx):
    global sohbet_edilen

    sohbet_edilen = ctx.author

    await ctx.send(f"Merhaba {ctx.author.mention}! 👋")


@bot.command(help="Komuttan sonra gelen sayıları toplar.")
async def add(ctx, *numbers: int):
    await ctx.send(
        f"Cevap: {sum(numbers)}"
    )


@bot.command(help="Komuttan sonra gelen metinlerden birini seçer.")
async def choose(ctx, *selections):
    choiced = random.choice(selections)

    await ctx.send(
        f"Seçilen: {choiced}"
    )


@bot.command(help="Araba yapar")
async def car(ctx, renk: str, marka: str):
    temp_car = Car(
        renk,
        marka
    )

    await ctx.send(temp_car)


@bot.command(help="Komutun bota gidene kadar geçen süreyi ölçer.")
async def ping(ctx):
    await ctx.send(
        f"Pong! 🏓 {(bot.latency * 1000):.2f} ms"
    )


bot.run(config.TOKEN)