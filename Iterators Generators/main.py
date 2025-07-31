# 1 ile sonsuz arasındaki sayıların karesini getiren fonksion
"""
def sayi_karesi():
    sayi = 1
    while True:
        yield sayi**2
        sayi +=1

generator = sayi_karesi()
print(generator)

print(next(generator))
print(next(generator))
print(next(generator))

for i in generator:
    print(i)
    """

# Fibonacci dizisi

def fibonacci(max):
    a, b = 0,1
    count = 0

    while count<= max:
        a , b = b , a + b
        yield b
        count +=1

# for i in fibonacci(10000):
#     print(i)

# Bellek performansları

import sys

liste = [i for i in range(10000)]
print(sys.getsizeof(liste))

generator_liste = (i for i in range(10000))
print(sys.getsizeof(generator_liste))

import time

start_time_list = time.time()
sum([i for i in range(10000)])
stop_time_list = time.time() - start_time_list

start_time_gen = time.time()
sum((i for i in range(10000)))
stop_time_gen = time.time() - start_time_gen

print(stop_time_gen)
print(stop_time_list)

# yield tanımlamadan list-comperhension ile de ama () parantezele generator tanımlanabilir