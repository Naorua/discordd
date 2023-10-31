import discord
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
async def apa_yang_dapat_dilakukan_untuk_mengurangi_atau_mendaur_ulang_sampah(ctx):
    await ctx.send(f'''
- Mendaur ulang sampah organik
- Menggunakan tas saat berbelanja
- Menggunakan Misting saat jajan
- Hindari makanan / minuman yang memiliki bungkus plastik
- Lakukan Reduce, Reuse, Recycle (3R)
                    ''')
    
@bot.command()
async def cara_untuk_memisahkan_dan_mendaur_ulang_sampah(ctx):
    await ctx.send(f'''
Berikut adalah cara untuk mendaur ulang dan memisahkan sampah:
-Memisahkan dan memilah sampah
-Kesadaran untuk mendaur ulang
-Menggunakan kontainer daur ulang
-Mendaur ulang di pusat daur ulang
-Menggunakan produk yang mudah di daur ulang
                   ''')
    
@bot.command()
async def apa_yang_dapat_kita_jadikan_dari_sampah_organik(ctx):
    await ctx.send(f'Sampah organik dapat dijadikan berbagai macam saat di daur ulang. contoh yang sering dilakukan adalah membuat pupuk dari sampah sampah oraganik. Contoh dari pupuk tersebut adalah pupuk Kompos, biogas, dan bahan aktif lainnya')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

@bot.command()
async def mem(ctx):
    with open('KOMT/model3.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)
