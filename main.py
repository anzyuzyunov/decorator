from functools import wraps
import datetime
def decorator(old_func):

    @wraps(old_func)
    def new_fun(*args,**kwargs):

    #Действия до вызова исходной функции

        result = old_func(*args,**kwargs)

        with open('log.txt', 'a') as f:
            time = datetime.datetime.now().strftime('%Y %B %d %H:%M')
            f.write(f'Функция {old_func.__name__} Время запуска {time},  Аргументы функции ={args}, результат {result}\n')
    # действия после вызова исходной функции


        return result

    return new_fun
@decorator
def fun(a,b):
    result = a * b
    return result

# fun = decorator(fun)
fun(23,2)
