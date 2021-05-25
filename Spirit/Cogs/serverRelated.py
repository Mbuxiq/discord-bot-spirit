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
    @commands.Cog.listener() ##! <- WORKS HERE BUT NOT IN COGS, WHY?
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

    @commands.command()
    async def rules(self, ctx):
        rulesembed=discord.Embed(title="Rules:", description="[Warnings are point based system. Any violation adds more points to your account. If the points reach a certain value, you will get banned]", color=0x000000)
        rulesembed.add_field(name="1. Attacking other users is prohibited.", value="[10 ban points]", inline=False)
        rulesembed.add_field(name="2. Posting NSFW/NSFL is prohibited.", value="[50 ban points]", inline=False)
        rulesembed.add_field(name="3. Mark loud and possible epilepsy triggers as a spoiler.", value="[20 ban points]", inline=False)
        rulesembed.add_field(name="4. Spreading drama is prohibited.", value="[10 ban points]", inline=False)
        rulesembed.add_field(name="5. Self advertising and/or raiding is prohibited.", value="[75 ban points]", inline=False)
        rulesembed.add_field(name="6. Use channels correctly", value="[5 ban points]", inline=False)
        rulesembed.add_field(name="7. Abusing the bot is prohibited.", value="[15 ban points]", inline=False)
        rulesembed.add_field(name="8. Spamming is prohibited.", value="[ (2^spam messages)/2 ban points]", inline=False)
        await ctx.send(embed= rulesembed)




def setup(bot):
    bot.add_cog(ServerRelated(bot))
