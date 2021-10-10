import asyncio
import discord
from YTDLSource import YTDLSource


class MusicPlayer:
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.playing = False

    async def add(self, url):
        self.queue.append(await YTDLSource.from_url(url, loop=self.bot.loop))
        print(self.queue)

    def add_local(self, file):
        self.queue.append(file)

    def pop_next(self):
        file = self.queue[0]
        self.queue.pop(0)
        return file

    def is_queue_empty(self):
        return len(self.queue) == 0

    def handle_end_of_audio(self, ctx, error):
        # TODO: Error handling
        self.playing = False
        self.play_next(ctx)

    def is_playing(self):
        return self.playing

    def play_next(self, ctx):
        if not self.is_queue_empty():
            self.playing = True
            server = ctx.message.guild
            voice_client = server.voice_client 
            next_file = self.pop_next()
            voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=next_file), after=lambda e: self.handle_end_of_audio(ctx, e))
            
            loop = asyncio.get_event_loop()
            loop.run_until_complete(ctx.send('**Now playing:** {}'.format(next_file)))

    async def play(self, ctx):
        if not self.playing and not self.is_queue_empty():
            self.playing = True
            async with ctx.typing():
                await self.join(ctx)
                self.play_next(ctx)

    async def join(self, ctx):
        if ctx.message.guild.voice_client:
            return
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

