import discord,random,os,requests
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
@bot.command()
async def mem(ctx):
    files=os.listdir("images")
    m=random.choice(files)
    with open(f'images/{m}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_dog_image_url():
    url='https://dog.ceo/api/breeds/image/random'
    res=requests.get(url)
    data=res.json()
    return data['message']
def get_cat_image_url():
    url="https://api.thecatapi.com/v1/images/search"
    res=requests.get(url)
    data=res.json()
    return data[0]['url']
@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command('dog')
async def dog(ctx):
    image_url=get_dog_image_url()
    await ctx.send(image_url)
@bot.command("cat")
async def cat(ctx):
    image_url=get_cat_image_url()
    await ctx.send(image_url)
bot.run("token pls")
