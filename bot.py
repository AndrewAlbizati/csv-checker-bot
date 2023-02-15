from discord.ext import commands
import discord


class Bot(commands.Bot):
    def __init__(self, **options):
        intents = discord.Intents.default()
        intents.message_content = True  
        super().__init__(intents=intents, command_prefix='/')
    
        
    async def on_ready(self):
        print(f'Logged in as {self.user}!')
