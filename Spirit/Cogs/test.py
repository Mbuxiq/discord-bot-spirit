import discord
from discord.ext import commands


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        var = discord.utils.get(ctx.guild.roles, name = "[Apex Legends]")
        author = ctx.author
        await author.add_roles(var)

def setup(bot):
    bot.add_cog(Test(bot))
