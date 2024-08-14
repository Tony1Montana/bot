import discord

API_TOKEN = ''

bot = discord.Intents.all()
client = discord.Client(intents=bot)
guild = discord.Guild


@client.event
async def on_ready():
    print('Hello {0.user} !'.format(client))
    await client.change_presence(activity=discord.Game('👀'))


@client.event
async def on_message(message):
   message_content = message.content
   message_author = message.author.id
   if message_content == "A wild countryball appeared!" and message_author == 999736048596816014:
    channel = client.get_channel(1269676858220220426)
    await channel.send('<@&1273279540935921736>')



if __name__ == "__main__":
    client.run(API_TOKEN)
