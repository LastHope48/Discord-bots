import discord,random
from discord.ext import commands
from bot_mantık import secret_function,emoji
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def yazıtura(ctx,times=1):
    await ctx.send(secret_function(times))
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def emojispawn(ctx):
    await ctx.send(emoji(3))
@bot.command()
async def yardım(ctx):
    await ctx.send("""!merhaba: Bot size kendinizi tanıtır
!heh (sayı): sayı kısmına yazdığınız kadar 'he' der.
!yazıtura: Yazı veya tura der
!joined (@sunucudaki bir kişi): İstediğiniz kişinin sunucuya ne zaman katıldığını gösterir
!emojispawn: 3 adet emoji gönderir
!choose (seçeneklerin) choose'dan sonra yazdığğın şeylerden birini seçiyor""")
@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))
bot.run("MTQyNjI1MDI5Mzg3NTcwMzg2OA.GVd8PR.GGIADsax27TtyiLODCnrMRjRP17zxNnx665L4I")
