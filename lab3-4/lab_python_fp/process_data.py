import json
import sys
# Сделаем другие необходимые импорты
from cm_timer import cm_timer_1
from field import field
from get_random import get_random
from print_result import print_result
import sort
from unique import Unique

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария
path = 'data_light.json'

with open(path,'r', encoding = 'utf8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(Unique([data[i]['job-name'] for i in range(len(data))], ignore_case = True))


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower()=='программист',arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + 'с опытом Python',arg))


@print_result
def f4(arg):
    pay = get_random(len(arg), 100000, 200000)
    res = list(zip(arg, pay))
    return [res[i][0] + ',зарплата' + str(res[i][1]) + 'руб. ' for i in range(len(arg))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
