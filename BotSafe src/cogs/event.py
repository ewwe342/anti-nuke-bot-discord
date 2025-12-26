import discord
from discord.ext import commands

class EventGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_scheduled_event_create(self, event):
        try:
            await event.delete(reason="guard")
        except discord.Forbidden:
            pass

async def setup(bot):
    await bot.add_cog(EventGuard(bot))