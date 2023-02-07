from discord.ext import commands
import json
from checker import Checker


class Bot(commands.Bot):
    def __init__(self, **options):
        super().__init__(intents=None, command_prefix='/')
    
        
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
