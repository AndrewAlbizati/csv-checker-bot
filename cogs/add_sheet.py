import discord
from discord.ext import commands
import json


class AddSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @discord.slash_command(description="Adds a Google Sheet to be tracked.")
    @discord.option("name", description="Name of the CSV")
    @discord.option("link", description="Link to the CSV")
    async def add_sheet(self, ctx: commands.Context, name: str, link: str):
        if not name or not link:
            return

        self.add_csv(str(ctx.author.id), name, link)
        await ctx.respond("test")
    

    def add_csv(self, user: str, name: str, link: str):
        with open('sheets.json', 'r') as f:
            data = json.load(f)
        
        data[user][name] = link
        with open('sheets.json', 'w') as f:
            json.dump(data, f)


def setup(bot):
    bot.add_cog(AddSheet(bot))
