import asyncio
import uvloop
import asyncpg
from datetime import datetime, date

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def run():
    conn = await asyncpg.connect(user='sanic_user', password='sanic',
                                 database='sanic_example', host='127.0.0.1')
    values = await conn.fetch('''SELECT myapp_mymodel.id, myapp_mymodel.name, myapp_mymodel.created FROM public.myapp_mymodel;''')
    print(values)
    await conn.close()


async def create():
    conn = await asyncpg.connect(user='sanic_user', password='sanic',
                                 database='sanic_example', host='127.0.0.1')
    for n in range(1):
        values = await conn.execute('''
            INSERT INTO myapp_mymodel(name, created) VALUES($1, $2)''', 'Bob', False)
    await conn.close()

loop = asyncio.get_event_loop()
initial_time = datetime.now()
print(initial_time)
loop.run_until_complete(run())
print(datetime.now() - initial_time)
initial_time = datetime.now()
loop.run_until_complete(create())
print(datetime.now() - initial_time)