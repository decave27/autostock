import autostock
import asyncio
new = autostock.Auto()
new.load('filename.json')
async def stock_loop():
    while True:
        await new.loop()
        await asyncio.sleep(100)

asyncio.run(stock_loop())

print(new.info(name='example').name , new.info(name='example').now)
