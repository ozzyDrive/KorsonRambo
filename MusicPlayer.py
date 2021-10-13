import asyncio
import discord
from YTDLSource import YTDLSource


class MusicPlayer:
    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.playing = False

    def add(self, player):
        self.queue.append(player)
        print(self.queue)

    def pop_next(self):
        url = self.queue[0]
        self.queue.pop(0)
        return url

    def is_queue_empty(self):
        return len(self.queue) == 0

    def handle_end_of_audio(self, voice_client):
        # TODO: Error handling
        self.playing = False
        self.start_playing(voice_client)

    def is_playing(self):
        return self.playing


    async def play(self, ctx, url):
        async with ctx.typing():
            file = await YTDLSource.from_url(url, loop=self.bot.loop)

            if self.is_queue_empty() and not self.is_playing():
                self.add(file)

                server = ctx.message.guild
                voice_client = server.voice_client 

                self.start_playing(voice_client)
                await ctx.send(f':mag_right: **Searching for** ``' + url + '``\n<:youtube:763374159567781890> **Now Playing:** ``{}'.format(file.title()) + "``")
            else:
                self.add(file)
                await ctx.send(f':mag_right: **Searching for** ``' + url + '``\n<:youtube:763374159567781890> **Added to queue:** ``{}'.format(file.title()) + "``")

    def start_playing(self, voice_client):
        if not self.is_queue_empty() and not self.is_playing():
            file = self.pop_next()
            self.playing = True
            voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=file), after=lambda e: self.handle_end_of_audio(voice_client))

    # def start_playing(self, voice_client):
    #     i = 0
    #     while i < len(self.queue):
    #         try:
    #             voice_client.play(self.pop_next(), after=lambda e: print('Player error: %s' % e) if e else None)

    #         except:
    #             pass
    #         i += 1

    # async def play(self, ctx):
    #     if not self.playing and not self.is_queue_empty():
    #         self.playing = True
    #         async with ctx.typing():
    #             await self.join(ctx)

    #             server = ctx.message.guild
    #             voice_client = server.voice_client 

    #             self.start_playing(voice_client)

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

