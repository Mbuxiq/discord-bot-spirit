import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
from discord.utils import get
import asyncio


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

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #rulesembed=discord.Embed(name="Rules:", description="[Warnings are point based system. Any violation adds more points to your account. If the points reach a certain value, you will get banned]", color=0x000000)
        rulesembed = discord.Embed(title="Rules", description="This is a placeholder. The rules still exist, but the system will be different in the future. For now, everything is moderated by a person.")
        rulesembed.add_field(name="1. Attacking other users is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="2. Posting NSFW/NSFL is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="3. Mark loud and possible epilepsy triggers as a spoiler.", value="-", inline=False)
        rulesembed.add_field(name="4. Spreading drama is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="5. Self advertising and/or raiding is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="6. Use channels correctly", value="-", inline=False)
        rulesembed.add_field(name="7. Abusing the bot is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="8. Spamming is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="9. Breaking Discord TOS is prohibited", value="-", inline=False)
        rulesembed.add_field(name="Please, react to confirmation message in #confirmation with <:checkmark:849012134540869672> if you accept the rules.", value="If not, react with <:decline:849012134952173610>")
        await member.send(embed=rulesembed)
        role = discord.utils.get(member.guild.roles, name='[Unverified Member]')
        await member.add_roles(role)

    @commands.command()
    async def rulestext(self, ctx):
        rulesembed = discord.Embed(title="Rules", description="This is a placeholder. The rules still exist, but the system will be different in the future. For now, everything is moderated by a person.")
        rulesembed.add_field(name="1. Attacking other users is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="2. Posting NSFW/NSFL is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="3. Mark loud and possible epilepsy triggers as a spoiler.", value="-", inline=False)
        rulesembed.add_field(name="4. Spreading drama is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="5. Self advertising and/or raiding is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="6. Use channels correctly", value="-", inline=False)
        rulesembed.add_field(name="7. Abusing the bot is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="8. Spamming is prohibited.", value="-", inline=False)
        rulesembed.add_field(name="9. Breaking Discord TOS is prohibited", value="-", inline=False)
        await ctx.send(embed=rulesembed)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = message.guild.get_member(payload.user_id)
        guild = self.bot.get_guild(payload.guild_id)
        emoji = payload.emoji
        if message.id == 849352038801211403:
            apex = discord.utils.get(guild.roles, name = "[Apex Legends]")
            war = discord.utils.get(guild.roles, name = "[Warzone/MW2019]")
            ow = discord.utils.get(guild.roles, name = "[Overwatch]")
            tf2 = discord.utils.get(guild.roles, name = "[Team Fortress 2]")
            gta = discord.utils.get(guild.roles, name = "[GTA V]")
            sticc = discord.utils.get(guild.roles, name = "[Stick Fight the Game]")
            scp = discord.utils.get(guild.roles, name = "[SCP:SL]")
            spell = discord.utils.get(guild.roles, name = "[Spellbreak]")
            osu = discord.utils.get(guild.roles, name = "[OSU]")
            mine = discord.utils.get(guild.roles, name = "[Minecraft]")
            rust = discord.utils.get(guild.roles, name = "[Rust]")
            r6 = discord.utils.get(guild.roles, name = "[R6]")
            val = discord.utils.get(guild.roles, name = "[Valorant]")
            csgo = discord.utils.get(guild.roles, name = "[CSGO]")
            sus = discord.utils.get(guild.roles, name = "[Among Us]")
            if emoji.id == 849345681277452328: await user.add_roles(apex)
            elif emoji.name == "💰": await user.add_roles(war)
            elif emoji.id == 849345405731864586: await user.add_roles(ow)
            elif emoji.id == 849345407574212679: await user.add_roles(tf2)
            elif emoji.id == 849345406038835211: await user.add_roles(gta)
            elif emoji.id == 849345407170772993: await user.add_roles(sticc)
            elif emoji.id == 849345402401456178: await user.add_roles(scp)
            elif emoji.id == 849345406030970890: await user.add_roles(spell)
            elif emoji.id == 849345406550016040: await user.add_roles(osu)
            elif emoji.id == 849345402653769738: await user.add_roles(mine)
            elif emoji.id == 849345403928313868: await user.add_roles(rust)
            elif emoji.id == 849345402998489208: await user.add_roles(r6)
            elif emoji.id == 849345403400617995: await user.add_roles(val)
            elif emoji.id == 849345402960609291: await user.add_roles(csgo)
            elif emoji.id == 849012137522495488: await user.add_roles(sus)
            else:
                await user.send("Incorrect emoji")
                await message.remove_reaction(emoji, user)
        elif message.id == 849340074453893190:
            if emoji.id == 849012134540869672:
                role = discord.utils.get(guild.roles, name='[Unverified Member]')
                await user.remove_roles(role)
                newrole = discord.utils.get(guild.roles, name='[Verified Member]')
                dash2 = discord.utils.get(guild.roles, id=849666767772581930)
                await user.add_roles(newrole)
                await user.add_roles(dash2)

            elif emoji.id == 849012134952173610:
                await user.send("We will not tolerate members that do not accept the rules.")
                await user.kick(reason="Not confirming the rules")
            else:
                await user.send("Incorrect emoji")
                await message.remove_reaction(emoji, user)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = message.guild.get_member(payload.user_id)
        guild = self.bot.get_guild(payload.guild_id)
        emoji = payload.emoji
        if message.id == 849352038801211403:
            apex = discord.utils.get(guild.roles, name = "[Apex Legends]")
            war = discord.utils.get(guild.roles, name = "[Warzone/MW2019]")
            ow = discord.utils.get(guild.roles, name = "[Overwatch]")
            tf2 = discord.utils.get(guild.roles, name = "[Team Fortress 2]")
            gta = discord.utils.get(guild.roles, name = "[GTA V]")
            sticc = discord.utils.get(guild.roles, name = "[Stick Fight the Game]")
            scp = discord.utils.get(guild.roles, name = "[SCP:SL]")
            spell = discord.utils.get(guild.roles, name = "[Spellbreak]")
            osu = discord.utils.get(guild.roles, name = "[OSU]")
            mine = discord.utils.get(guild.roles, name = "[Minecraft]")
            rust = discord.utils.get(guild.roles, name = "[Rust]")
            r6 = discord.utils.get(guild.roles, name = "[R6]")
            val = discord.utils.get(guild.roles, name = "[Valorant]")
            csgo = discord.utils.get(guild.roles, name = "[CSGO]")
            sus = discord.utils.get(guild.roles, name = "[Among Us]")
            if emoji.id == 849345681277452328: await user.remove_roles(apex)
            elif emoji == ":moneybag:": await user.remove_roles(war)
            elif emoji.id == 849345405731864586: await user.remove_roles(ow)
            elif emoji.id == 849345407574212679: await user.remove_roles(tf2)
            elif emoji.id == 849345406038835211: await user.remove_roles(gta)
            elif emoji.id == 849345407170772993: await user.remove_roles(sticc)
            elif emoji.id == 849345402401456178: await user.remove_roles(scp)
            elif emoji.id == 849345406030970890: await user.remove_roles(spell)
            elif emoji.id == 849345406550016040: await user.remove_roles(osu)
            elif emoji.id == 849345402653769738: await user.remove_roles(mine)
            elif emoji.id == 849345403928313868: await user.remove_roles(rust)
            elif emoji.id == 849345402998489208: await user.remove_roles(r6)
            elif emoji.id == 849345403400617995: await user.remove_roles(val)
            elif emoji.id == 849345402960609291: await user.remove_roles(csgo)
            elif emoji.id == 849012137522495488: await user.remove_roles(sus)
            else:
                await user.send("Incorrect emoji")
                await message.remove_reaction(emoji, user)
            
    @commands.command()
    async def conf(self, ctx):
        embed = discord.Embed(name="REACT TO THIS MESSAGE", description="If you are confirming that you have read the rules. \nReact with <:checkmark:849012134540869672> to accept, <:decline:849012134952173610> to decline")
        message = await ctx.send(embed = embed)
        await message.add_reaction('<:checkmark:849012134540869672>')
        await message.add_reaction('<:decline:849012134952173610>')


def setup(bot):
    bot.add_cog(ServerRelated(bot))
