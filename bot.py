import discord
import os
from discord.ext import commands, tasks, timers
import random

client = commands.Bot(command_prefix='!')
client.remove_command("help")

#On Ready Event------------------------------------------

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(" !help"))
    print('Logged in as: {0.user}'.format(client))

#General Error Handling----------------------------------

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        command_not_found = discord.Embed(title="Command Not Found :(", description="Use !help to see the list of commands and how to use them.", colour=discord.Colour.orange())
        await ctx.send(content=None, embed=command_not_found)
    else:
        print (error)

#Commands-------------------------------------------------

@client.command(pass_context=True) #Custom Help Command
async def help(ctx):
    embed = discord.Embed(title="Help", colour = discord.Colour.orange())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717853456244670509/718950987762761758/SynergyyNoBg.png")
    embed.add_field(name='!random', value = 'Randomly chooses an option from the ones you give the bot.\n>>> eg. !random Pizza Taco Sushi Burger', inline=False)
    await ctx.send(embed=embed)

@client.command() #Ping Command
async def ping(ctx):
    await ctx.send(f'Pong! My current latency is {round(client.latency*1000)}ms.')

@client.command(aliases=['random']) #Random Command
async def rand(ctx, *information):
    output = random.choice(information)
    rand_embed = discord.Embed(description=f"The result is: **{output}**!", colour = discord.Colour.orange())
    await ctx.send(embed=rand_embed)

@client.command()
async def aadi(ctx):
    aadi = discord.Embed(description=f"**Aadi** is extremely cool and not at all gay.", colour = discord.Colour.orange())
    await ctx.send(embed=aadi)

@client.command()
async def yatin(ctx):
    aadi = discord.Embed(description=f"Unfortunately, **Yatin** is extremely gay.", colour = discord.Colour.orange())
    await ctx.send(embed=aadi)

@client.command()
async def jerry(ctx):
    aadi = discord.Embed(description=f"**Jerry** is slightly gay. Mostly bc he does not think Katara from ATLA is really hot.", colour = discord.Colour.orange())
    await ctx.send(embed=aadi)


#Error Handling ---------

@rand.error
async def rand_error(ctx, error):
    item_missing = discord.Embed(title='Missing Options!', description="You must provide the bot with options to select from!\n For more help,refer to !help", colour=discord.Color.green())
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(content=None, embed=item_missing)
    else:
        print(error)



#Bot Token Pairing-----------------------------------------
client.run('NzMxODk1NTc5MTI2MjY4MDA5.XwstPg.jOVkW9Ao6q_bFxr8H7LYEhoI8sk')

