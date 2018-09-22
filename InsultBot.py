from discord.ext import commands
import discord
from random import *

linkInsult = ['Insert insults in the list here. These will be called when someone links anything in the chat']

TOKEN = 'Your token here'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

# If someone uses the rhythm bot, it makes a sarcastic comment. This can also be changed to have 
# a list of insults similar to that of the link insults
    if message.content.startswith('!play'):
        msg = 'You have great taste... {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

# If a message containing 'http' is sent in the chat (a link), the bot makes a series of comments that are 
# randomised. This is done by using randint to pick a random position between the first and last in the list.
    if message.content.startswith('http'):
        a = randint(0,len(linkInsults))
        msg = linkInsult[a].format(message)
        await client.send_message(message.channel, msg)

# The following three conditional statements respond to the user's potential question with "what/wat/wot"
    if message.content.startswith('what'):
        msg = 'what {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('wot'):
        msg = 'wat {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('wat'):
        msg = 'wot {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

# This function prints the author id and author display name of the message owner in the console window.
    if message.content.startswith('yes'):
        msg = message.author.id.format(message)
        print(message.author.display_name, msg)

# If the author of the message is a specific person, the bot will send a message catered to that person only. 
    if message.author.display_name == 'Insert display name':
        msg = 'Hello my son {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Ready')


client.run(TOKEN)