import discord
from discord.ext import commands
from YTDLSource import YTDLSource
import logging
import sys

logging.basicConfig(level=logging.INFO)

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    pass

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='korso')
async def korso(ctx):
    server = ctx.message.guild
    voice_client = server.voice_client 
    
    await ctx.send('KORSON RAMBO')
    filename = await YTDLSource.from_url('https://www.youtube.com/watch?v=_GdTW9V6hY4', loop=bot.loop)
    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))



@bot.command(name='play', help='To play song')
async def play(ctx,url):
    try:
        server = ctx.message.guild
        voice_client = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
        ctx.send('Error trying to play the song.')


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
        
bot.run(sys.argv[1])