import discord
import asyncio
import uvloop
import logging
import conf
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


cogs = [
    'delete'
]


bot = commands.Bot(command_prefix=conf.prefix,
                   description='DelBot', case_insensitive=True, self_bot=True)


@bot.listen()
async def on_ready():
    print('Logged in as {}'.format(bot.user.name))
    bot.remove_command('help')
    for cog in cogs:
        bot.load_extension(cog)
    return


@bot.event
async def on_command_error(ctx, error):
    """Ignore command not found errors."""
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

@bot.check
async def is_me(ctx):
    """Globally check if self enters command."""
    return ctx.author.id == bot.user.id

bot.run(conf.token, bot=False)
