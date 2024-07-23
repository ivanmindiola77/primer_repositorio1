
import discord
from discord.ext import commands
import os, random 
intents = discord.Intents.default()

intents.message_content = True

token = 'MTI2MDAxNzU4NDY4Njc2MDA2OQ.GvwZXQ.cdO4wnBpVDjNv119UYwACqwFk-U56nNMy8LWnI'

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('El bot se ha iniciado')

@bot.command()
async def hola(ctx):
    await ctx.send('Hola, como te llamas')
     
@bot.command()
async def meme(ctx):
    files = os.listdir("img")
    meme_random = random.choice(files)
    meme_path  = os.path.join("img",meme_random)
    await ctx.send(file=discord.File(meme_path))
    
@bot.command()
async def suma(ctx,num1:int,num2:int):
    total=num1+num2
    await ctx.send(total)
@bot.command()
async def resta(ctx,num1:int,num2:int):
    total=num1-num2
    await ctx.send(total)    
@bot.command()
async def div(ctx,num1:int,num2:int):   
    if num1 != 0 and num2 != 0:
        total = num1/num2
        await ctx.send(total) 
    else:
        error = "Error no se puede dividir entre 0 "   
        await ctx.send(error)        
         
@bot.command()
async def multi(ctx,num1:int,num2:int):
    total=num1*num2
    await ctx.send(total)
bot.run(token)
