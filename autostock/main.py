from dbjson import Database
from .error import AutoStockException
from random import randint
import asyncio
import io
from .stock import Stock
class Auto:
    def __init__(self, loop=True, max : int = 200):
        self.loop = loop
        self.max = max
    
    
    def load(self, file=None):
        if not file:
            raise AutoStockException.FileNotFoundException("FileNotFound")
        self.db = Database(str(file))
        return None

    async def loop(self):
        for stock_name in self.db:
            stock  = self.db[stock_name]
            stock['history'].append(stock['old'])
            while len(stock['history']) > self.max:
                del stock['history'][0]
            stock['old'] = stock['now']
            now = stock['now']
            rand = randint(now - 150, now + 160)
            if rand <= 0:
                rand = 1
            stock['now'] = rand
        self.db.commit()
        return None

    def info(self, **kwargs):
        st_name = kwargs.get('name', 'all')

        if st_name == 'all':
            stocklist = []
            for stock_name in self.db:
                stock = self.db[stock_name]
                now = stock['now']
                old = stock['old']
                if old > now:
                    up = Stock.plus
                elif old > now:
                    up = Stock.down
                elif old == now:
                    up = Stock.middle

                stocklist.append(Stock(name=stock_name, up=up, now=now, old=old, history=self.db.get(st_name)['history']))
            return stocklist
        elif not self.db.get(st_name):
            raise AutoStockException.StockNameNotFoundException("StockNameNotFound")
        else:
            stock = self.db[st_name]
            now = stock['now']
            old = stock['old']
            if old > now:
                up = Stock.plus
            elif old > now:
                up = Stock.down
            elif old == now:
                up = Stock.middle
            
            
            return Stock(name=st_name, up=up, now=now, old=old, history=self.db.get(st_name)['history']) 
    def img(self, stock : Stock, color = 'r'):
        import matplotlib.pyplot as plt
        plt.clf()
        plt.plot(range(len(stock.history)), stock.history, color)
        plt.ylabel('Price')
        buf = io.BytesIO()
        plt.savefig(buf)
        buf.seek(0)
        return buf

    def add_stock(self, name):
        self.db[name] = {
            "now" : 5000,
            "old" : 0
        }
        self.db.commit()
        return None

    def remove_stock(self, name):
        if not self.db.get(name):
            raise AutoStockException.StockNameNotFoundException("StockNameNotFound")
        else:
            del self.data[name]
            self.db.commit()
            return None




   




        
        
            



    
        



        




    


            


        
        
       

    
