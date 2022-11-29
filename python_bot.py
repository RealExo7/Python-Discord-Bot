#BOT_CHAT_FILTER

import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = '!')

@Bot.event
async def on_ready():
	print("Bot is online")

@Bot.event
async def on_message(msg):
	if msg.content == "TEST":
		await Bot.delete_message(msg)
		

Bot.run("NzkyMTM3NDIyNjE0ODIyOTIy.X-ZVdg.2vxa1fuBLvWrB6Z3gfiZfWt7-nI")



#BOT_VOICE_CHANNEL_RADIO


# @Bot.command(name = 'join', aliases = ['summon'])
# async def _join (ctx, *, channel: discord.VoiceChannel = none):

# 	destination = channel if channel else ctx.author.voice.channel
# 	if ctx.voice_client:
# 	await ctx.voice_state.voice.move_to(destination)

# 		return

# 	await destination.connect()
# 	await ctx.send("Succesfully joined the voice channel") 







# @Bot.command(pass_context=True)
# async def yt(ctx, url):

# 	author = ctx.message.author
# 	voice_channel = author.voice_channel
# 	vc = await client.join_voice_channel(voice_channel)

# 	player = await vc.create_ytdl_player(url)
# 	player.start








# async def yt(ctx):
# 	url = ctx.message.content
# 	url = url.strip('!yt ')

# 	author = ctx.message.author
# 	voice_channel = author.voice_channel
# 	vc = await client.join_voice_channel(voice_channel)

# 	player = await vc.create_ytdl_player(url)
# 	player.start()


