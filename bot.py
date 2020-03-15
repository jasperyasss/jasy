import discord
from discord.ext		import commands
from discord.ext.commands	import Bot
import asyncio

bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
	print ("working_i_think")

async def react(message):
	custom_emojis = [
	"<:Like:681874120220475425>",
	"<:Dislike:681874243926884363>"
	]
	guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
	for emoji in custom_emojis:
		if emoji in guild_emoji_names:
			await message.add_reaction(emoji)

@bot.event
async def on_message(message):
	if message.channel.id == 654727829212102677:
			await react(message)

bot.run("NjgxODYzMTcyNzEzNzQyMzY2.XlU2IQ.cAgN5RDRentVmYyNFqjLZ2UffrI")
