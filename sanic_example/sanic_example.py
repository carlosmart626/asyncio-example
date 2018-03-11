import asyncio
import requests
import asyncpg
import uvloop

from sanic.response import text
from sanic import Sanic

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic()


async def create():
    conn = await asyncpg.connect(user='sanic_user', password='sanic',
                                 database='sanic_example', host='postgres')
    await conn.execute('''
        INSERT INTO myapp_mymodel(name, created) VALUES($1, $2)''', 'Bob', False)
    await conn.close()


@app.route('/')
async def hello(request):
    await create()
    return text("OK")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, workers=5)