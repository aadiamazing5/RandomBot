import discord
import os
from discord.ext import commands, tasks
import random
import itertools

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
    embed.add_field(name='!range', value = 'Randomly chooses a number between the start and end point you define.\n>>> eg. !range 0 500', inline=False)
    embed.add_field(name='!shuffle', value = 'Shuffles a sequence that you provide. Use this to easily decide on an order to do an activity.\n>>> eg. !shuffle John Gary Kevin Brian', inline=False)
    embed.add_field(name='!8ball', value = 'Ask the magical 8 ball a question!\n>>> eg. !8ball Will France win the next World Cup?', inline=False)
    embed.add_field(name='!flip', value = 'Flip a coin!', inline=False)
    await ctx.send(embed=embed)

@client.command() #Ping Command
async def ping(ctx):
    await ctx.send(f'Pong! My current latency is {round(client.latency*1000)}ms.')

@client.command(aliases=['random']) #Random Command
async def rand(ctx, *information):
    output = random.choice(information)
    rand_embed = discord.Embed(description=f"The result is: **{output}**!", colour = discord.Colour.orange())
    await ctx.send(embed=rand_embed)

@client.command(aliases=['range']) #Range Command
async def rand2(ctx, start, stop):
    output = random.randint(int(start), int(stop))
    range_embed = discord.Embed(description=f"The result is: **{output}**!", colour = discord.Colour.orange())
    await ctx.send(embed=range_embed)

@client.command(aliases=['shuffle']) #Shuffle Command
async def rand3(ctx, *information):
    l = list(information)
    output = random.sample(l, len(l))
    shuffle_embed = discord.Embed(description=f"Shuffled Order: {output}", colour = discord.Colour.orange())
    await ctx.send(embed=shuffle_embed)

@client.command() #Coinflip Command
async def flip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    coinflip_card = discord.Embed(colour = discord.Colour.orange(), description=f"The result was **{rancoin}**!")
    await ctx.send(embed=coinflip_card)

@client.command(aliases=['8ball']) #8ball Command
async def _8ball(ctx, *, question):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
                "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
                "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    _8ball_card = discord.Embed(colour = discord.Colour.orange(), description = f"**Question:** {question}\n**Answer:** {random.choice(responses)}")
    await ctx.send(embed=_8ball_card)

@client.command() #Server Listing Command (Priv)
async def servercount(ctx):
    servercount = len(client.servers)
    await ctx.send(servercount)

#Error Handling ---------

@rand.error
async def rand_error(ctx, error):
    unexcpected_error = discord.Embed(title='Unexcpected Error :(', description="Please try again later or refer to !help for more help.", colour=discord.Color.orange())
    item_missing = discord.Embed(title='Missing Options!', description="You must provide the bot with options to select from!\n For more help,refer to !help", colour=discord.Color.orange())
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(content=None, embed=item_missing)

    else:
        print(error)
        await ctx.send(content=None, embed=unexcpected_error)

@rand2.error
async def rand2_error(ctx, error):
    unexcpected_error = discord.Embed(title='Unexcpected Error :(', description="Please try again later or refer to !help for more help.", colour=discord.Color.orange())
    item_missing = discord.Embed(title='Missing Argument!', description="You must enter a beggining and end point for the range!\nFor more help,refer to !help", colour=discord.Color.orange())
    bad_argument = discord.Embed(title='Argument Error!', description="There was a problem with the arguments you provided.\nRefer to !help for the correct format.", colour=discord.Color.orange())
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(content=None, embed=item_missing)
    
    elif isinstance(error, commands.BadArgument):
        await ctx.send(content=None, embed=bad_argument)

    else:
        print(error)
        await ctx.send(content=None, embed=unexcpected_error)

@rand3.error
async def rand3_error(ctx, error):
    unexcpected_error = discord.Embed(title='Unexcpected Error :(', description="Please try again later or refer to !help for more help.", colour=discord.Color.orange())
    item_missing = discord.Embed(title='Missing Argument!', description="You must provide a sequence to shuffle!\nFor more help,refer to !help", colour=discord.Color.orange())
    bad_argument = discord.Embed(title='Argument Error!', description="There was a problem with the arguments you provided.\nRefer to !help for the correct format.", colour=discord.Color.orange())
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(content=None, embed=item_missing)
    
    elif isinstance(error, commands.BadArgument):
        await ctx.send(content=None, embed=bad_argument)

    else:
        print(error)
        await ctx.send(content=None, embed=unexcpected_error)

@_8ball.error
async def _8ball_error(ctx, error):
    arg_missing = discord.Embed(title='Missing Required Argument!', description="You need to ask the 8ball a question!\neg. !8ball Am I cool?\n Please refer to !help for more info.", colour=discord.Color.green())
    format_error = discord.Embed(title='Format Error!', description="Please follow this format: !8ball Am I cool?\n Please refer to !help for more info.", colour=discord.Color.green())
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(content=None, embed=arg_missing)
    else:
        await ctx.send(content=None, embed=format_error)

#Bot Token Pairing-----------------------------------------
client.run(os.environ['TOKEN'])

