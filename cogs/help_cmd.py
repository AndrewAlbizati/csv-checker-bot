import discord
from discord.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Sends information about the bot.")
    async def help(self, ctx: commands.Context):
        embed = discord.Embed()
        embed.title = "Help with Time Tracker Bot"
        embed.set_image(url="https://github.com/AndrewAlbizati/csv-checker-bot/blob/main/sheet_screenshot.png?raw=true")
        embed.color = discord.Colour.green()
        
        embed.add_field(name="How to Use", value="""This bot is used for tracking hours logged on a Google Sheet in the format shown in the screenshot.
        The bot detects whenever the minutes reported doesn't match with the hours reported, and will alert you to these mistakes.""", inline=False)
        
        embed.add_field(name="Commands", value="""**/add_sheet <name> <link>** Adds a Google Sheet to be tracked by the bot.
        **/remove_sheet <name>** Removes a Google Sheet from being tracked by the bot.
        **/list_sheets** Lists all sheets being tracked.
        **/check <name>** Checks a sheet to see if all hours are logged correctly.
        """, inline=False)
        
        embed.add_field(name="More Information", value=f"Visit [here](https://github.com/AndrewAlbizati/csv-checker-bot) for more information.", inline=False)
        
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
