#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, pi, log, sin
from multiprocessing import Process, Queue


eps = .0000001


def inf_sum(x, out):
    summa = x
    prev = 0
    i = 1
    while abs((summa - prev) > eps):
        prev = summa
        summa += (cos(x*i))/i
        i += 1

    out.put(summa)


def check(x, out):
    result = -1 * log(2*sin(x/2))

    out.put(result)


if __name__ == '__main__':
    x = pi
    out1 = Queue()
    out2 = Queue()
    process_1 = Process(target=inf_sum, args=(x, out1))
    process_2 = Process(target=check, args=(x, out2))
    process_1.start()
    process_2.start()
    result1 = out1.get()
    result2 = out2.get()
    process_1.join()
    process_2.join()

    print(f"The sum is: {result1}")
    print(f"The check sum is: {result2}")