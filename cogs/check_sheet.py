import discord
from discord.ext import commands
from checker import Checker
import sheet_manager


class CheckSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @discord.slash_command(description="Checks Google Sheet that all minutes are reported correctly.")
    @discord.option("name", description="Name of the CSV")
    async def check_sheet(self, ctx: commands.Context, name: str):
        # Return if name not provided
        if not name:
            return
        
        url = sheet_manager.get_sheet_url(str(ctx.author.id), name)

        if not url:
            embed = discord.Embed()
            embed.title = "Error Finding Google Sheet"
            embed.description = f"The Google Sheet named {name} couldn't be found. Please ensure that it is spelled correctly."
            embed.color = discord.Colour.red()
            await ctx.respond(embed=embed, ephemeral=True)
            return

        embed = self.check_sheet(url)
        embed.title = f"Results from Sheet \"{name}\""
        await ctx.respond(embed=embed, ephemeral=True)


    def check_sheet(self, url: str) -> discord.Embed:
        embed = discord.Embed()
        checker = Checker(url)

        results = checker.check()
        if len(results) == 0:
            embed.description = "There were no errors detected in this sheet."
            embed.color = discord.Colour.green()
        else:
            description = f"**There were {len(results)} error{'s' if len(results) != 1 else ''} detected**\n"
            for err in results:
                description += f"**{err[0]}** was reported as {err[2]} instead of {err[1]}\n"
            embed.description = description
            embed.color = discord.Colour.red()

        return embed


def setup(bot):
    bot.add_cog(CheckSheet(bot))
