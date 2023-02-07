import discord
from discord.ext import commands
import json


class ListSheets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @discord.slash_command(description="Lists all Google Sheets that are being tracked.")
    async def add_sheet(self, ctx: commands.Context):
        embed = discord.Embed()
        embed.title = f"Sheets Tracked by {ctx.author.name}"

        sheets = self.get_sheets(str(ctx.author.id))

        if not sheets:
            embed.description = "**No sheets are being tracked."
        else:
            for k,v in sheets:
                embed.description += f"[{k}]({v})\n"
            
        await ctx.respond(embed=embed)
    

    def get_sheets(self, user: str) -> dict[str,str]:
        with open('sheets.json', 'r') as f:
            data = json.load(f)
        if user in data.keys():
            return data[user]
        return None


def setup(bot):
    bot.add_cog(ListSheets(bot))
