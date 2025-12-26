import discord, asyncio, json, os, console
from discord.ext import commands

with open('cfg.json', 'r') as f:
    config = json.load(f)

class BotSafe(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config.get('prefix', '-'),
            intents=discord.Intents.all(),
            help_command=None
        )

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                except Exception:
                    pass

    print("Brauchen 5s...")
    async def on_ready(self):
        print("Bot erfolgreich gestartet. Betrieb normal.")

bot = BotSafe()

if __name__ == '__main__':
    bot.run(config['token'],reconnect=True)