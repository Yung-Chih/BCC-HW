import os
from dotenv import load_dotenv
import discord

import discord
from discord.ext import commands
from discord.ext.commands import Context

class MyCommandBot(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')
        await super().on_message(message)


@commands.command()
async def hello(ctx: Context):
    await ctx.send( f"Hello {ctx.author}" )

def main():
    # load ".env"
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    print( f"Token: {TOKEN}")

    # Discord Bot setup
    intents = discord.Intents.default()
    intents.message_content = True

    bot = MyCommandBot(command_prefix='!', intents=intents)

    ## Add Command to Bot
    bot.add_command( hello )

    # Run bot with token
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
