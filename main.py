import discord
from discord.ext import commands


bot = commands.Bot(intents=discord.Intents.all(), command_prefix='-')

token = "MTAzNDE2MTQwNjAxNjI0MTY3NA.GFYZIU.FS1p82YXjRX1RjDddIQT9hrS2Ggbn-hTPt9nNU"


@bot.event
async def on_ready():
    print("Je suis prêt avec les slash command")
    await bot.change_presence(status=discord.Status.online)





@bot.event
async def on_message(message):
    if message.channel.id == 1076669947410927707:
        new_nickame = message.content
        membre = message.author
        autre = bot.get_channel(1077261314453422191)
        await membre.edit(nick=new_nickame)
        await autre.send(f"Le surnom de {membre} a été changé en : {new_nickame}")
        await membre.add_roles(discord.utils.get(membre.guild.roles, name='🍽️ | Client'))
        await membre.remove_roles(discord.utils.get(membre.guild.roles, name="verification"))
        await membre.remove_roles(discord.utils.get(membre.guild.roles, name='reglement'))




bot.run(token)
