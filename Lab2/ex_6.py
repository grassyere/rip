#!/usr/bin/env python3
import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'data_light_cp1251.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    job = list(field(arg, 'job-name'))
    job = unique(job, ignore_case = True)
    job = sorted(job)
    return job


@print_result
def f2(arg):
    job = list(filter(lambda x: 'программист' in x.lower(), arg))
    return job


@print_result
def f3(arg):
    job = list(map(lambda x: x + 'с опытом Python', arg))
    return job


@print_result
def f4(arg):
    job = list(arg)
    salary = list(gen_random(100000, 200000, list(job)))
    salary = list(map(lambda x: 'зарплата' + str(x) + 'руб' , salary))
    progs = list(zip(job, salary))
    return progs


with timer():
    f4(f3(f2(f1(data))))
