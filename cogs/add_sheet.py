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
    
        embed = self.add_link(str(ctx.author.id), name, link)
        await ctx.respond(embed=embed, ephemeral=True)
    

    def add_link(self, user: str, name: str, link: str) -> discord.Embed:
        embed = discord.Embed()

        with open('sheets.json', 'r') as f:
            data = json.load(f)
        
        if not user in data.keys():
            data[user] = {}
        
        if name in data[user].keys():
            embed.title = "Error with Adding Sheet"
            embed.description = f"You already have a Google Sheet named {name}. Please delete it before adding it again."
            embed.color = discord.Colour.red()

            return embed


        if link in data[user].values():
            embed.title = "Error with Adding Sheet"
            embed.description = f"You already have a Google Sheet with the link {link}. Please delete it before adding it again."
            embed.color = discord.Colour.red()

            return embed
        
        data[user][name] = link
        with open('sheets.json', 'w') as f:
            json.dump(data, f)
        
        embed.title = "Successfully Added Sheet"
        embed.description = f"The sheet with name {name} has been added successfully. Use /remove_sheet {name} to delete it."
        embed.color = discord.Colour.green()
        return embed


def setup(bot):
    bot.add_cog(AddSheet(bot))
