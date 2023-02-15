import discord
from discord.ext import commands
import sheet_manager


class AddSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @discord.slash_command(description="Adds a Google Sheet to be tracked.")
    @discord.option("name", description="Name of the CSV")
    @discord.option("link", description="Link to the CSV")
    async def add_sheet(self, ctx: commands.Context, name: str, link: str):
        # Return if name or link not provided
        if not name or not link:
            return
    
        embed = discord.Embed()
        if sheet_manager.add_sheet(str(ctx.author.id), name):
            embed.title = "Successfully Added Sheet"
            embed.description = f"The Google Sheet **{name}** was added successfully. You can check it by typing /check_sheet {name}"
            embed.color = discord.Colour.green()
        else:
            embed.title = "Error Adding Sheet"
            embed.description = f"The Google Sheet **{name}** couldn't be added. You may want to use a different name."
            embed.color = discord.Colour.red()
        
        await ctx.respond(embed=embed, ephemeral=True)
        

def setup(bot):
    bot.add_cog(AddSheet(bot))
