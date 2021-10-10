import logging
import sys

from discord.ext import commands

from CommandHandler import CommandHandler

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    bot = commands.Bot(command_prefix='.')
    
    command_handler = CommandHandler(bot)
    
    bot.run(sys.argv[1])
