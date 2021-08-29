import discord
import random
from discord.ext import commands
#criar o boot sem interferança de caracter
client = commands.Bot(command_prefix = ">", case_insensitve = True)

@client.event
async def on_ready():
  print("Entramos como {0.user}" .format(client))

@client.command()
async def ola(ctx):
  await ctx.send(f'Olá, {ctx.author}')

@client.command()
async def stop(ctx):
  await ctx.send(f'Nada pode me parar, {ctx.author} fui criado para viver')

@client.command()
async def gado(ctx):
  await ctx.send(f'olha quem fala, {ctx.author} quem pensa que você e, seu coco')


  
@client.command()
async def regradado(ctx):
  await ctx.send(f'A regra e simples, você usa o prefixo ">" para me invocar junto da palavra dado e de um espaço, logo em seguida você insera a quantidade de lado que deseja o seu dado, vou te retornar um numero aleatorio de 1 ate a quantidade que você me informou')

@client.command()
async def enviarembed(ctx):
  embed = discord.Embed(
    title = "Trio Shogum",
    description = "descrição",
    colour = discord.Colour.blue()
  )

  embed.set_author(name='Autor', icon_url='https://static.wikia.nocookie.net/ursossemcurso/images/e/e3/The_Bears.png/revision/latest/scale-to-width-down/250?cb=20150813200838&path-prefix=pt-br')

  embed.set_thumbnail(url='https://www.proibidoler.com/wp-content/uploads/2020/02/ursos-sem-curso-a-comica-e-divertida-integracao-ante-a-sociedade-humana.jpg')

  embed.set_image(url='https://sm.ign.com/ign_br/screenshot/default/ending-theme-1536x864_napm.jpg')



  await ctx.send(embed = embed)






@client.command()
async def  dado(ctx, numero):
  variavel = random.randint(1,int(numero))
  await ctx.send(f'o numero que caiu foi: {variavel} | muito obrigado por jogar')




client.run('ODgwOTgzNzY0MTM2Nzc5Nzk3.YSmOEQ.9IIYD3Cmp5RUmEMx0QsWbvaBvhc')