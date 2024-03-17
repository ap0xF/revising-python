import asyncio


async def funcn1():
    # await asyncio.sleep(5)
    print("I am from funcn 1")
    return "Aadit"


async def funcn2():
    # await asyncio.sleep(3.5)
    print("I am from funcn 2")
    return "Babu"


async def funcn3():
    # await asyncio.sleep(2)
    print("I am from funcn 3")
    return "Pant"


async def funcn4():
    # await asyncio.sleep(0.5)
    print("I am from funcn 4")
    return " ,PHD"


async def run_the_code():
    # await funcn1()
    # await funcn2()
    # await funcn3()
    # await funcn4()

    res = await asyncio.gather(
        funcn1(),
        funcn2(),
        funcn3(),
        funcn4()
    )
    print(res)


asyncio.run(run_the_code())

lst = [1, 2, 3, 4]
