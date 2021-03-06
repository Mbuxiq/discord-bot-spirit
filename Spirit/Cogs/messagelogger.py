import discord
from discord.ext import commands
from discord.utils import get
import time
import datetime
import os

class logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def append_new_line(self, text_to_append): #<- Does what it says. Appends new line in a text file in a folder called 'Logs'. The text file is named like the current date
        today = datetime.datetime.now()
        date_time = today.strftime("%d_%m_%Y") #<- Set the time
        with open(f"./Logs/{date_time}.txt", "a", encoding="utf-8") as a: #<- This is pretty straightforward, the only thing needed is the encoding. Some characters or emojis can't be appended if not using the utf-8 encoding.
            text_to_append = text_to_append.replace('\n', ' ').replace('\r', '') #<- This is a bit of a mess. Basically I am removing new lines '\n' with just spaces, so multi lined messages will be long, and not fill up multiple lines
            a.write(f"\n{text_to_append}")

    async def create_log(self): 
        date_time = datetime.datetime.now().strftime("%d_%m_%Y") #<- Sets the time
        try:
            with open(f"./Logs/{date_time}.txt", "x") as a: #<- x means create folder if it doesn't exist. If it does exist, it will return an error
                info_message="\n[Time in CET][Message type][Name/ID][Channel ID]> ['Message', 'Link to attachment (if sent)' > 'New edited message (if message was edited)']\n---\n" #<- Appending some info if people are gonna read the logs
                a.write(info_message)
        except FileExistsError: pass

    @commands.Cog.listener()
    async def on_ready(self):
        await self.create_log()

    ### Logging messages starts here \/


    #Some of these look really complicated, but they are not. Its basically the same exact thing, but with some extras.
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message(self, message):
        if message.author == self.bot.user: return
        else:
            author = message.author
            now = datetime.datetime.now()
            time_detail = now.strftime("%Hh/%Mm/%Ss")
            if not message.attachments: await self.append_new_line(f"[{time_detail}][Sent][{author}/{author.id}][{message.channel.id}]> ['{message.content}']")
            else: await self.append_new_line(f"[{time_detail}][Sent][{author}/{author.id}][{message.channel.id}]> ['{message.content}', '{message.attachments[0].url}']")
    
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_edit(self, before, after):
        if before.author == self.bot.user: return
        else:
            now = datetime.datetime.now()
            time_detail = now.strftime("%Hh/%Mm/%Ss")
            author = before.author
            if not before.attachments or after.attachments: await self.append_new_line(f"[{time_detail}][Edited][{author}/{author.id}][{before.channel.id}]> ['{before.content}' > '{after.content}']")
            else: await self.append_new_line(f"[{time_detail}][{author}/{author.id}][Edited][{before.channel.id}]> ['{before.content}', '{before.attachments[0].url}' > '{after.content}', '{after.attachments[0].url}]'")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_raw_message_delete(self, payload):
        try:
            now = datetime.datetime.now()
            time_detail = now.strftime("%Hh/%Mm/%Ss")
            message = payload.cached_message
            authorid = message.author.id
            authornick = message.author.display_name

            if authorid == self.bot.user.id: return
            else:
                    if not message.attachments: await self.append_new_line(f"[{time_detail}][Deleted][{authornick}/{authorid}][{message.channel.id}]> ['{message.content}']")
                    else: await self.append_new_line(f"[{time_detail}][Deleted][{authornick}/{authorid}][{message.channel.id}]> ['{message.content}', '{message.attachments[0].url}']")
        except AttributeError: pass


    ### \/ This causes trouble. Logs cannot be downloaded the same date they were created. It's weird, and I didn't find any fixes, so just deal with it.
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def logdownload(self, ctx, date):
        date = date.replace("/","_")
        try: await ctx.send(content = "Log download", file = discord.File(f"./Logs/{date}.txt"))
        except discord.HTTPException: 
            await ctx.send("Logs cannot be downloaded the same day they were created")


def setup(bot):
    bot.add_cog(logging(bot))
