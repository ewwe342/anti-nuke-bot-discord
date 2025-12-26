import discord
from discord.ext import commands
from collections import defaultdict
import time

class BotSpamGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.anti_spam = defaultdict(list)
        self.limit = 4
        self.window = 2

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild or message.author.id == self.bot.user.id:
            return

        if message.author.bot:
            now = time.time()
            self.anti_spam[message.author.id] = [t for t in self.anti_spam[message.author.id] if now - t < self.window]
            self.anti_spam[message.author.id].append(now)

            if len(self.anti_spam[message.author.id]) > self.limit:
                try:
                    await message.guild.ban(message.author, reason="guard")
                    await message.channel.purge(limit=50, check=lambda m: m.author.id == message.author.id)
                except discord.Forbidden:
                    pass

async def setup(bot):
    await bot.add_cog(BotSpamGuard(bot))