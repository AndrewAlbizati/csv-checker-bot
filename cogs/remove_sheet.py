import discord
from discord.ext import commands
import sheet_manager


class RemoveSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @discord.slash_command(description="Removes a Google Sheet from being tracked.")
    @discord.option("name", description="Name of the CSV")
    async def remove_sheet(self, ctx: commands.Context, name: str):
        # Return if name not provided
        if not name:
            return
    
        embed = discord.Embed()
        if sheet_manager.remove_sheet(str(ctx.author.id), name):
            embed.title = "Successfully Removed Sheet"
            embed.description = f"The Google Sheet **{name}** was removed successfully."
            embed.color = discord.Colour.green()
        else:
            embed.title = "Error Removing Sheet"
            embed.description = f"The Google Sheet **{name}** couldn't be removed. You may want to check that you submitted the correct name."
            embed.color = discord.Colour.red()
        
        await ctx.respond(embed=embed, ephemeral=True)
    

def setup(bot):
    bot.add_cog(RemoveSheet(bot))
