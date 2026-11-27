import asyncio
import time
async def task1():
    print("Task 1 Started")
    await asyncio.sleep(3)          # Simulate a long-running task with asyncio sleep
    print("Task 1 Completed")

async def task2():
    print("Task 2 Started")
    await asyncio.sleep(3)
    print("Task 2 Completed")

async def task3():
    print("Task 3 Started")
    await asyncio.sleep(3)
    print("Task 3 Completed")

async def main():
    start = time.time()
    await asyncio.gather(
        task1(),
        task2(),
        task3()
    )
    print("Total Time:", time.time() - start)

asyncio.run(main())