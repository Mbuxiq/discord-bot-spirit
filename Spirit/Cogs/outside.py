import discord
from discord.ext import commands
from aiohttp import ClientSession
import requests
import asyncio

class API(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    # I don't have anything to add to this. You just have to learn how to work with ClientSessions. To be fair, I made this a while ago, and Im not sure how it works. I only did the definition and example recently.

    @commands.command(aliases=["urban", "urband", "def", "definition"],)
    @commands.cooldown(1, 10, type=commands.BucketType.member)
    async def urbandictionary(self, ctx, *, term):
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":term}
        headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "https://rapidapi.com/community/api/urban-dictionary"
        }
        async with ClientSession() as session:
            async with session.get(url, headers=headers, params=querystring) as response:
                r = await response.json()
                definition = r['list'][0]['definition']
                example = r['list'][0]['example']
                embed = discord.Embed(title=term, description="First definition found:") 
                await ctx.send(embed=embed)
                num = 1

                parts = [definition] #<- Basically I want to split the definition into multiple parts. If its larger than 1024 characters, then it will return an error and doesnt do anything. I want to split it and send it in multiple parts

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
                    await asyncio.sleep(1) #<- Asyncio sleep so the bot wont get slowed down for spamming

                exembed = discord.Embed(title="Example", description="Example for the term:") #<- Examples are not long, so I dont have to worry about the splitting part again
                exembed.add_field(name="-", value=example, inline=False)
                await ctx.send(embed=exembed)



def setup(bot):
    bot.add_cog(API(bot))
