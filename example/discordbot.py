import discord
from discord.ext import commands, tasks
import autostock
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=['.']
        )
        self.autostock = autostock.Auto(max=200)
    async def on_ready(self):
        self.loop.start()
        self.autostock.load('filename.json')
    @tasks.loop(seconds=100)
    async def loop(self)
        await self.autostock.loop()
    @commands.command('stock')
    async def stock_info(self, ctx, name):
        st_info = self.autostock.info(name=name)
        await ctx.send(content=st_info.text, file=discord.File(fp=self.autostock.img(st_info), filename="stock.png"))
    @commands.command('add')
    async def stock_add(self, ctx, name):
        r = self.autostock.add_stock(name=name)
        await ctx.send(str(r))
    @commands.command('remove')
    async def stock_remove(self, ctx, name):
        r = self.autostock.remove_stock(name=name)
        await ctx.send(str(r))
        
Bot().start('token')

        
        
    
    

        
