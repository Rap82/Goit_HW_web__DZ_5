#=========================================== *wraps ======================================
# ++++++++++++++++++++++++++ написання Декоратора для таймінгу виконання будь якої асинхроної і синхроної  функції +++++++++++++

from functools import wraps
from time import time

def async_timed (name:str) :
    """асинхрона функція приймає імя(*імя функції час виконання якої будемо заміряти ) тип *str
    Повертає час виконання асинхроної функції в секундах"""
    if name : # Якщо ми отримуємо імя функції то :
        print(name) # принтимо його  
    def wrapper(func): # Функція *wrapper - Приймає якесь імя функції - Ігнорує помилки які можуть виникати під час її виконання і повертає час коли всі процеси виконання закінчились успішно чи ні байдуже.
        @wraps(func) # декоратор для функції 
        async def wrapperd(*args, **kwargs):
            """асинхрона функція приймає будь яку кількість аргументів і параметрів(*інших_функції) 
            Повертає час коли їх робота завершилась"""
            start = time() # В зміну *start - записуємо поточний час
            try:  # Перевірка try ... expact ... funally  Якщо винекне якась ситсемна помилка під час виконання коду який розміщений в середені цих блоків програме невилетить а прдовжить працювати згідно інструкції які будуть нами написані. 
                return await func(*args, **kwargs) # повертаємо результат роботи переданої функції з її аргументами і параметрами
            finally:
                print(time()- start) # щоб нестались в попередній частині коду пінтимо різницю часу між початком і поточнийм часом. 
                                    #   Отриманий результат і буде часом виконання асинхроної функції
        return wrapperd # Повертає імя  асинхроної функції *wrapperd (Це потрібно щоб декоратор міг працювати)
    return wrapper      # Повертає імя   функції *wrapper (Це потрібно щоб декоратор міг працювати)

def sync_timed (name:str) :
    """синхрона функція приймає імя(*імя функції час виконання якої будемо заміряти ) тип *str
    Повертає час виконання асинхроної функції в секундах"""
    if name : # Якщо ми отримуємо імя функції то :
        print(name) # принтимо його  
    def wrapper(func): # Функція *wrapper - Приймає якесь імя функції - Ігнорує помилки які можуть виникати під час її виконання і повертає час коли всі процеси виконання закінчились успішно чи ні байдуже.
        @wraps(func) # декоратор для функції 
        def wrapperd(*args, **kwargs):
            """синхрона функція приймає будь яку кількість аргументів і параметрів(*інших_функції) 
            Повертає час коли їх робота завершилась"""
            start = time() # В зміну *start - записуємо поточний час
            try:  # Перевірка try ... expact ... funally  Якщо винекне якась ситсемна помилка під час виконання коду який розміщений в середені цих блоків програме невилетить а прдовжить працювати згідно інструкції які будуть нами написані. 
                return  func(*args, **kwargs) # повертаємо результат роботи переданої функції з її аргументами і параметрами
            finally:
                print(time()- start) # щоб нестались в попередній частині коду пінтимо різницю часу між початком і поточнийм часом. 
                                    #   Отриманий результат і буде часом виконання асинхроної функції
        return wrapperd # Повертає імя  асинхроної функції *wrapperd (Це потрібно щоб декоратор міг працювати)
    return wrapper      # Повертає імя   функції *wrapper (Це потрібно щоб декоратор міг працювати)
