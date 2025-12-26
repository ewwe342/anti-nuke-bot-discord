import discord
from discord.ext import commands

class ChannelGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create):
            if entry.user.id == self.bot.user.id:
                return
            try:
                await channel.guild.kick(entry.user, reason="guard")
                await channel.delete(reason="guard")
            except discord.Forbidden:
                pass
            break

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        async for entry in channel.guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete):
            if entry.user.id == self.bot.user.id:
                return
            try:
                await channel.guild.kick(entry.user, reason="guard")
            except discord.Forbidden:
                pass
            break

async def setup(bot):
    await bot.add_cog(ChannelGuard(bot))