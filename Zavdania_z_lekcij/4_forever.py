# ================================ Модуль asyncio(асинхроне програмування) - Використаня модуля forever  ================
# +++++++++++++++++++++++++++ Основне задання Організація самих простих *task (Розгляд того що є підкапотом в *asyncio.run() ++++++++++++++++++
# 


import asyncio
import random

from time import sleep, time

async def ping(signal): # асинхрона допоміжна  функція яка приймає один аргумент *signal і принтить його .
    print(f"Pinging--{signal}")

async def foo(): # асинхрона допоміжна  функція яка приймає один аргумент *signal і принтить його .
    print(f"Один раз покажи Hello Word")   

async def main(): # Асинхрона основна функція в якій раалізовано бескінечний цикл *while в якому з затримкою 1 сек будемо принтити випадково згенерований результат *signal через нашу функцію *ping(signal) 
    while True:
        await asyncio.sleep(1)
        await ping(random.randint(a=1, b=1000))

if __name__ == "__main__" : # Реалізація основної функції коду.
    #asyncio.run(main()) # Запуск асинхроної функції в основнову коді за допомогою функції *asyncio.run(*асинхрона_функція)
    """ Ще одна реалізація тої ж функції але через функцію *run_forever() . 
    Примітка: ще один розбір можливостай *asyncio.run(*асинхрона_функція) - того що внеї підкапатом(реалізовано в середені)"""
    loop = asyncio.new_event_loop() # Створення event loop (обробник подій в асинхроному коді )
    asyncio.set_event_loop(loop)    # Встановлення event loop (обробник подій в асинхроному коді )
    loop.create_task(main())        # Створення завдання *task для нашої функції *main() через метод *імя_evant_lopp.create_task(*функція_для_якої_створюємо_task)
    loop.create_task(foo())         # Створення завдання  *task для нашої функції *foo() через метод *імя_evant_lopp.create_task(*функція_для_якої_створюємо_task)
    loop.run_forever()              # Запуск бескінечної події loop- *event loop- за допомогою методу *імя_evant_lopp.run_forever()