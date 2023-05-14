import asyncio
#create a coroutine
# async def main():
#     print('hello')
#     task = asyncio.create_task(full("chicken"))
#     await asyncio.sleep(1)
#     print("finished")

# async def full(text):
#     print(text)
#     await asyncio.sleep(1)

# asyncio.run(main())
async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}
async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.2)
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)
    await task2
asyncio.run(main())