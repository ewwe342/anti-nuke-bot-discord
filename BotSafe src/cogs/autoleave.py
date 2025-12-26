import discord
from discord.ext import commands
import json

class ServerGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('cfg.json', 'r') as f:
            self.config = json.load(f)
        self.allowed_guilds = self.config.get('allowed_guilds', [])

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if guild.id not in self.allowed_guilds:
            await guild.leave()

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            if guild.id not in self.allowed_guilds:
                await guild.leave()

async def setup(bot):
    await bot.add_cog(ServerGuard(bot))