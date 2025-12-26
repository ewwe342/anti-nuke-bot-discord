import discord
from discord.ext import commands

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = discord.Embed(
                    title="BotSafe",
                    description=(
                        "Для корректной работы защиты выполните следующие действия:\n\n"
                        "1. Поднимите роль бота **выше всех остальных ролей**.\n"
                        "2. Убедитесь, что у бота есть право **Администратор**.\n\n"
                    ),
                )
                await channel.send(embed=embed)
                break

async def setup(bot):
    await bot.add_cog(Setup(bot))