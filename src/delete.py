import discord
import logging
from discord.ext import commands


class Delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def  _authorized(self, message):
        return message.author.id == self.bot.user.id and \
                    message.type == discord.MessageType.default


    async def _delete_messages(self, channel, max_delete=300000):
        """Deletes messages from a Discord channel
        
        Retrieves messages from a discord channel limited  by a max
        variable. Each retrieved message will be iterated over. If the
        bot user is authorized to delete the message, then the message 
        will be deleted.
        """
        try:
            [await message.delete() async for message in 
                channel.history(limit=max_delete) if await self._authorized(message)]
        except discord.Forbidden as e:
            logging.exception(str(e))
        except discord.HTTPException as e:
            logging.exception(str(e))


    @commands.group(
        name='remove',
        description='delete own messages',
        aliases=['rm'],
        case_insensitive=True,
        invoke_without_command=True
    )
    async def remove(self, ctx, max_delete=None):
        if max_delete:
            await self._delete_messages(ctx.channel, max_delete=int(max_delete) + 1)
            return
        await self._delete_messages(ctx.channel)
        

    @remove.command()
    async def private(self, ctx):
        await ctx.message.delete()
        [await self._delete_messages(channel) for channel in self.bot.private_channels]

def setup(bot):
    bot.add_cog(Delete(bot))
