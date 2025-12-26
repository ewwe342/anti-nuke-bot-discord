import discord
from discord.ext import commands
import re

class WebhookGuard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_pattern = re.compile(r"@(everyone|here)", re.IGNORECASE)

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.webhook_id:
            return

        if self.spam_pattern.search(message.content):
            try:
                webhooks = await message.channel.webhooks()
                for webhook in webhooks:
                    if webhook.id == message.webhook_id:
                        await webhook.delete(reason="guard")
                        
                        await message.channel.purge(limit=10, check=lambda m: m.webhook_id == message.webhook_id)
                        break
            except discord.Forbidden:
                pass
            except discord.HTTPException:
                pass

async def setup(bot):
    await bot.add_cog(WebhookGuard(bot))