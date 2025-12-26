import discord
from discord.ext import commands

class IconProtection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        if before.icon == after.icon:
            return

        async for entry in after.audit_logs(limit=1, action=discord.AuditLogAction.guild_update):
            if entry.user.id == self.bot.user.id:
                return

        try:
            icon_bytes = await before.icon.read() if before.icon else None
            await after.edit(icon=icon_bytes, reason="guard")
            
            if entry.user:
                await after.kick(entry.user, reason="guard")
        except (discord.Forbidden, discord.HTTPException):
            pass

async def setup(bot):
    await bot.add_cog(IconProtection(bot))