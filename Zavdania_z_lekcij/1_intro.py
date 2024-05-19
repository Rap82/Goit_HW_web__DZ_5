# ================================ Модуль asyncio(асинхроне програмування) -  ================
#  ++++++++++++++++++++++++++++++ Створення самої простої асинхроної функціїї (Основа асинхроного програмування)+++++++++++++++++++++++++++++


import asyncio

async def foo():
    await asyncio.sleep(0) #Запис який з псевдоасинхроної функції гарантовано робить її асинхроною( тому час sleep (0))
    return "Helo word"

# async def main():
#     result = foo()
#     result = await result

#     return result

async def main(): # Простійший запис тоїж функції *async def main()
    result = foo()
    
    return await result

if __name__ == '__main__':
    r = asyncio.run(main())
    print(f"Result - {r}")