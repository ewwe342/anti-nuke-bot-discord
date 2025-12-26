import discord
from discord.ext import commands

class GuildProtection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        if before.name == after.name:
            return

        async for entry in after.audit_logs(limit=1, action=discord.AuditLogAction.guild_update):
            if entry.user.id == self.bot.user.id:
                return

        try:
            await after.edit(name=before.name, reason="guard")
        except discord.Forbidden:
            pass

async def setup(bot):
    await bot.add_cog(GuildProtection(bot))