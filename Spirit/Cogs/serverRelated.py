import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
from discord.utils import get
import asyncio
from Assets import embeds


class ServerRelated(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ##
    @commands.Cog.listener() 
    async def on_voice_state_update(self, member, before, after):
        if after.channel != None:
            if after.channel.id == 846117723825111110:
                for guild in self.bot.guilds:
                    maincategory = discord.utils.get(guild.categories, id=846117668217552956)
                    channel2 = await guild.create_voice_channel(name=f"{member.display_name}'s Voice Channel", category=maincategory)
                    await channel2.set_permissions(member, connect=True, mute_members=True, manage_channels=True)
                    await member.move_to(channel2)

                    def check(x, y, z):
                        return len(channel2.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await channel2.delete()





def setup(bot):
    bot.add_cog(ServerRelated(bot))
