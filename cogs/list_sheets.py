import discord
from discord.ext import commands
import sheet_manager


class ListSheets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @discord.slash_command(description="Lists all Google Sheets that are being tracked.")
    async def list_sheets(self, ctx: commands.Context):
        embed = discord.Embed()
        embed.title = f"Sheets Tracked by {ctx.author.name}#{ctx.author.discriminator}"

        sheets = sheet_manager.get_sheets(str(ctx.author.id))

        if not sheets or len(sheets.keys()) == 0:
            embed.description = "**No sheets are being tracked.**"
            embed.color = discord.Colour.red()
        else:
            description = ''
            for k,v in sheets.items():
                description += f"[{k}]({v})\n"

            embed.description = description
            embed.color = discord.Colour.green()
            
        await ctx.respond(embed=embed, ephemeral=True)
    

def setup(bot):
    bot.add_cog(ListSheets(bot))
