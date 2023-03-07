import os
import asyncio

from dotenv import load_dotenv
from discord.ext import commands
import discord

from basic_feature import Basic

class MyCommandBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as {0} ({0.id})'.format(self.user))

    async def on_message(self, message: discord.Message, /) -> None:
        print(f'Message from {message.author}: {message.content}')
        return await super().on_message(message)

async def create_bot():
    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Add commands by cog
    bot = MyCommandBot(command_prefix='!', intents=intents)

    await bot.add_cog( Basic(bot) )

    return bot

def main():
    load_dotenv()

    bot = asyncio.run( create_bot() )

    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

