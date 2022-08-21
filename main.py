import os
import discord
from discord.ext import commands 
import logging



## DO NOT DELETE
#defining a few things
client = discord.Client()
bot = commands.Bot(command_prefix='$', case_insensitive=True)
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
logging.basicConfig(level=logging.INFO)



@bot.event
async def on_ready():
    print(f"=====\nLogged in as: {bot.user.name} : {bot.user.id}\n=====\nMy current prefix is: $\n=====")
    await bot.change_presence(activity=discord.Game(name=f"Hi, I am {bot.user.name}.\n Use $ to interact with me!")) #changes bots displayed 'activity' 

@bot.command(name='test')
async def _test(ctx):
    """
    A simple command which says hi to the author.
    """
    await ctx.sent(f"Hi {ctx.author.mention}")
    # another way to do this is (user object).mention
    #await ctx.send(f"Hi <@(ctx.author.id)>!")

    

    
#checks that message author isnt the same as the client (the bot) so that the bot doesnt respond to its own messages

#@client.event
#async def on_message(message):
#    if message.author != client.user:
#        await message.channel.send(message.content[::-1])

#takes $greet as trigger, tells user ot say hello
# makes function called check, checks message content for "hello" and that the channel matches the initial channel the $greet was triggered in then replies with "hello + author of user that said hello"

#@client.event
#async def on_message(message):
#    if message.content.startswith('$greet'):
#        channel = message.channel
#        await channel.send('Say hello!')
#
#        def check(m):
#            return m.content == 'hello' and m.channel == channel
#
#        msg = await client.wait_for('message', check=check)
#        await channel.send('Hello {.author}!'.format(msg))
