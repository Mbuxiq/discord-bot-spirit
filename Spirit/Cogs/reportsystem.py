import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
from discord.utils import get
import asyncio

class ReportSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reports(self, ctx):
        em = discord.Embed(title="Report users here: ", description="React to the emoji. A new channel will be created where you can give all the additional info")
        message = await ctx.send(embed=em)
        await message.add_reaction("⬜")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = message.guild.get_member(payload.user_id)
        guild = self.bot.get_guild(payload.guild_id)
        emoji = payload.emoji
        if message.id == 849734638595211285:
            await message.remove_reaction(emoji, user)
            maincategory = discord.utils.get(guild.categories, id=849734947627597864)
            channel2 = await guild.create_text_channel(name=f"{user.display_name}'s-report-ticket", category=maincategory)
            role = discord.utils.get(guild.roles, id=849352231047659540)
            await channel2.set_permissions(role, view_channel=False)
            await channel2.set_permissions(user, read_messages=True,send_messages=True)
            em = discord.Embed(title="Report ticket", description=f"created by {user.mention}")
            em.add_field(name = "You will need to send __two messages. First is the reported's discord ID__", value="If you don't know how to see ID's, check https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-", inline=False)
            em.add_field(name = "__Second message is the reason.__", value="NOTE: The messages have a timeout of 120 seconds. If the messages are not send fast enough, the channel will be deleted and you will have to start again.")
            await channel2.send(embed=em)
            def check(message):
                return message.author.id == user.id
            try:
                msg = await self.bot.wait_for('message', check=check, timeout=120)
                reportedid = str(msg.content)
                msg2 = await self.bot.wait_for('message', check=check, timeout=120) 
                reason = str(msg2.content)
                await channel2.send("Thank you for your cooperation. The information has been sent to moderators and they will investigate the reported user. This channel will delete itself in 60 seconds")
                reportchannel = discord.utils.get(guild.channels, id=849738461955227660)
                rem = discord.Embed(title=f"New report created by {user.display_name}/{user.id}", description="-")
                rem.add_field(name=f"Reported ID: {reportedid}", value=f"Reason: {reason}")
                await reportchannel.send(embed=rem)
                await asyncio.sleep(60)
                await channel2.delete()
            except asyncio.TimeoutError:
                await channel2.delete()
                await user.send("Your channel was deleted due to a timeout. The time is limited to 120 seconds.")



def setup(bot):
    bot.add_cog(ReportSystem(bot))
