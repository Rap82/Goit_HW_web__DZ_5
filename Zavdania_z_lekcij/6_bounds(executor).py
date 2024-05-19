
#========================= Робота з Executor ===========================
#===============================основне завдання за допомогою *Executor перетворювати викнання синхроних функції в асинхроний спосіб

import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from sys import argv


def read_file(): # 
    """Функція синхрона,без аргументів, відкриває якись файл і зчитує з нього перших 100 рядків та повертає їх з функції"""
    with open(__file__, "r") as fh:
        return fh.read(100)

def calculate(power:int, p:int):
    """Функція синхрона отримує два аргументи , цілі числа , суму всіх чисел від нуля до 10 в степіні *p ,піднесених до степіню *power """
    r=[i**power for i in range (10**p)] # Запис циклу *for одним ряком
    return sum(r)

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool: # Через менеджер контексів і клас *ThreadPoolExecutor() - (для асинхроних потоків) - 
                                        # заганяємо нашу синхрону функцію *read_file в асинхроний потік
        f = await loop.run_in_executor(pool, read_file) # в зіну *f  передаємо результат виконная синхроної функції *read_file() через асинхроні потоки.
        print(f)
        
    with ProcessPoolExecutor() as pool: # Через менеджер контексів і клас *ProcessPoolExecutor() - (для асинхроних процесів) - 
                                        # заганяємо нашу синхрону функцію *culculate(power:int, p:int) в асинхроний процес
        f = await loop.run_in_executor(pool, calculate, 20,5 ) # в зіну *f  передаємо результат виконная синхроної функції *culculate(power:int, p:int) через асинхроні процеси.
                            # Де *pool - event loop процеси ,  *calculate - імя синхроної функції яку будемо запускати в асинхроних процесах
                            #  числа 20,5 - аргументи якы будемо передавати в *calculate 
        print(f)


if __name__ == "__main__" :
    asyncio.run(main())