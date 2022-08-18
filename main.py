import os
import discord
#from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('$test'):
            channel = message.channel
            await channel.send('copy')

@client.event
async def on_message(message):
    if message.content.startswith('$rem'):
        channel = message.channel
        await channel.send('Enter reminder name')

        def check(m):
            return m.content == '' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))




token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
#keep_alive()
#token = os.environ.get('DISCORD_BOT_SECRET')
#client.run(token)




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
