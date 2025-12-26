import discord
from discord.ext import commands

class RoleGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create):
            if entry.user.id == self.bot.user.id:
                return
            try:
                await role.guild.kick(entry.user, reason="guard")
                await role.delete(reason="guard")
            except discord.Forbidden:
                pass
            break

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        async for entry in role.guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete):
            if entry.user.id == self.bot.user.id:
                return
            try:
                await role.guild.kick(entry.user, reason="guard")
            except discord.Forbidden:
                pass
            break

async def setup(bot):
    await bot.add_cog(RoleGuard(bot))