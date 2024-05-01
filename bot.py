import discord

client = discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Crushing today's Wordle"))

@client.event
async def on_message(message):
    # Bot shouldn't be responding to itself
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

client.run(TOKEN)