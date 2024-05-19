#=================================== ProcessPoolExecutor ============================

# +++++++++++++++++++Реалізація за допомогою ProcessPoolExecutor і future двох процесів одночас . 
# один асинхроний з функцєю *ping(signal) інший синхроний  *cpu_bound_operation(counter:int)
# Поки синхрона функція *cpu_bound_operation(counter:int) проводила свої обчислення в одному прцесі , інша асинхрона продовжувала працювати в іншому процесі неприпиняючись .
# По завершенюю роботи синхроної завершились всі процеси (і асинхрона також ) Повернувся результат.


import asyncio

import random
from concurrent.futures import ProcessPoolExecutor # Exsecutor для процесів

from time import sleep, time

async def ping(signal): # асинхрона допоміжна  функція яка приймає один аргумент *signal і принтить його .
    print(f"Pinging--{signal}")


async def ping_worker(): # Асинхрона основна функція в якій раалізовано бескінечний цикл *while в якому з затримкою 1 сек будемо принтити випадково згенерований результат *signal через нашу функцію *ping(signal) 
    while True:
        await asyncio.sleep(1)
        await ping(random.randint(a=1, b=1000))

def cpu_bound_operation(counter:int):
    init = counter
    while counter > 0:
        counter -= 1
    print(f"Complated operation {init} ")
    return init


async def main():
    loop = asyncio.get_running_loop()
    task = loop.create_task(ping_worker())
            
    with ProcessPoolExecutor(2) as pool: # Через менеджер контексів і клас *ProcessPoolExecutor() - (для асинхроних процесів) -ProcessPoolExecutor(*кількість_процесів) , внашому випадку будемо задіювати два процеси(два ядра) .
                                        # заганяємо нашу синхрону функцію *culculate(power:int, p:int) в асинхроний процес
        futures =  [loop.run_in_executor(pool, cpu_bound_operation, counter ) for counter in  [100_000_000, 120_000_000, 150_000_000]] # в зіну *f  передаємо результат виконная синхроної функції *cpu_bound_operation(counter:int) через асинхроні процеси.
                            # Де *pool - event loop процеси ,  *cpu_bound_operation - імя синхроної функції яку будемо запускати в асинхроних процесах
                            #  числа 1000000000,120000000,150000000 - аргументи якы будемо передавати через цикл  for в *cpu_bound_operation
        result = await asyncio.gather(*futures) # збераємо згенеровані *futures - *asyncio.gather(*futures) і присвоюємо їх в *result
        task.cancel() # Зупеняємо рототу *task
        return result # Повертаємо з функції результат 


if __name__ == "__main__" :
    result = asyncio.run(main())
    print(result)