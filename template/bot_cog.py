import os
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from discord.ext import commands
import discord

import asyncio

class MyCommandBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as {0} ({0.id})'.format(self.user))

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')
        await super().on_message(message)


class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx: Context, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member


async def create_bot():
    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Add commands by cog
    bot = MyCommandBot(command_prefix='!', intents=intents)

    await bot.add_cog( Greetings(bot) )

    return bot


def main():
    load_dotenv()

    bot = asyncio.run( create_bot() )

    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

if __name__ == "__main__":
    main()

