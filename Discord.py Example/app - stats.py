import discord
import psutil

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$cpu'):
        await message.channel.send(f'{psutil.cpu_percent(interval=None)}!')

client.run('token')
