import discord
from discord.ext import commands
from aiohttp import ClientSession
import requests
import asyncio

class API(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=["urban", "urband", "def", "definition"],)
    @commands.cooldown(1, 10, type=commands.BucketType.member)
    async def urbandictionary(self, ctx, *, term):
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":term}
        headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "fb380aa4f0mshb55eb665deb7a61p138de1jsna7aa06a3228a"
        }
        async with ClientSession() as session:
            async with session.get(url, headers=headers, params=querystring) as response:
                r = await response.json()
                definition = r['list'][0]['definition']
                example = r['list'][0]['example']
                embed = discord.Embed(title=term, description="First definition found:") 
                await ctx.send(embed=embed)
                num = 1

                parts = [definition]

                while len(parts[-1]) > 1024: #<- https://stackoverflow.com/questions/509211/understanding-slice-notation
                    firstPart = parts[-1][:1024] 
                    secondPart = parts[-1][1024:] 

                    parts[-1] = firstPart
                    parts.append(secondPart)
                
                for i in parts:
                    lenght = len(parts)
                    em = discord.Embed(title=" ", description = " ")
                    em.add_field(name=f"{num}/{lenght}", value=i, inline = False)
                    await ctx.send(embed=em)
                    num += 1
                    await asyncio.sleep(1)

                exembed = discord.Embed(title="Example", description="Example for the term:")
                exembed.add_field(name="-", value=example, inline=False)
                await ctx.send(embed=exembed)



def setup(bot):
    bot.add_cog(API(bot))