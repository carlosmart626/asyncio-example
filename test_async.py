# import asyncio
# import requests
# import datetime
# import uvloop

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# async def main():
#     loop = asyncio.get_event_loop()
#     futures = [
#         loop.run_in_executor(
#             None, 
#             requests.get, 
#             'http://localhost:8000/'
#         )
#         for i in range(100)
#     ]
#     for response in await asyncio.gather(*futures):
#         pass

# t1 = datetime.datetime.now()
# print(t1)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# t2 = datetime.datetime.now()
# print(t2 - t1)
# print(t2)

import asyncio
import concurrent.futures
import requests
import datetime

async def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                'http://localhost:8000/'
            )
            for i in range(1000)
        ]
        for response in await asyncio.gather(*futures):
            pass


t1 = datetime.datetime.now()
print(t1)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
t2 = datetime.datetime.now()
print(t2 - t1)
print(t2)
