import discord
from discord.ext import commands
from discord.ext.commands.context import Context

########
# Basic Bot Features
########

class Basic(commands.Cog):
    def __init__(self, bot: commands.Bot ):
        self.bot: commands.Bot = bot

    @commands.command()
    async def hello(self, ctx: Context, *, member: discord.Member = None):
        # [TODO]
        pass
    
    @commands.command()
    async def say(self, ctx: Context, *, s: str):
        # [TODO]
        pass
        
    @commands.command()
    async def prefix(self, ctx: Context, s: str):
        # [TODO]
        pass

    @commands.command()
    async def GPA(self, ctx: Context, *, s: str = ""):
        # [TODO]
        pass
