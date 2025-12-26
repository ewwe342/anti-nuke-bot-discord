import discord
from discord.ext import commands

class KickBanGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        async for entry in member.guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
            if entry.target.id == member.id:
                if entry.user.id == self.bot.user.id:
                    return
                try:
                    await member.guild.kick(entry.user, reason="guard")
                except discord.Forbidden:
                    pass
                break

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            if entry.target.id == user.id:
                if entry.user.id == self.bot.user.id:
                    return
                try:
                    await guild.kick(entry.user, reason="guard")
                except discord.Forbidden:
                    pass
                break

async def setup(bot):
    await bot.add_cog(KickBanGuard(bot))