from MusicPlayer import MusicPlayer


class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.music_player = MusicPlayer(bot)

        @bot.command(name='join')
        async def join(ctx):
            await self.music_player.join(ctx)

        @bot.command(name='leave')
        async def leave(ctx):
            await self.music_player.leave(ctx)

        @bot.command(name='korso')
        async def korso(ctx):
            await self.music_player.play(ctx, 'https://www.youtube.com/watch?v=_GdTW9V6hY4')
        
        @bot.command(name='play')
        async def play(ctx, url):
            await self.music_player.play(ctx, url)