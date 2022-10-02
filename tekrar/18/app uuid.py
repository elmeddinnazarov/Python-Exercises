import random 
from math import inf
from timeit import timeit

ran_list = []



for i in range(1000):
    eded = random.uniform(0,1000)
    ran_list.append(eded)
    


def getmax(l):
    sort_list = sorted(l)
    max_value = sort_list[-1]
    return max_value


def getmax2(l):
    max_value = -inf
    for i in l:
        if i > max_value:
            max_value = i
            
    return max_value

print(getmax(ran_list))
print(getmax2(ran_list))
print(timeit('getmax(ran_list)', 'from __main__ import getmax, ran_list', number=1000))
print(timeit('getmax2(ran_list)', 'from __main__ import getmax2, ran_list', number=1000))