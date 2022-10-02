'''
comprehensions
range
tuple
dictionary
'''

# r = range(1, 100)
# print(r)
# print(r[3])
# print(r[3:10])
# print(len(r))

# for i in r:
#     print(i)

# r2 = range(15) # range(0, 15, 1)
# r3 = range(4, 15) # range(4, 15, 1)
# r4 = range(15, 4, -1)
# r5 = range(15, 4, -3)

# print(list(r5))
# print(list(range(4, 15, -1)))

# print(list(range(105, 200, 7)))

# for v1 in range(1, 10):
#     for v2 in range(1, 10):
#         print(v1, 'x', v2, '=', v1*v2)
#     print('\n\n')


# user_input = input('Eded girin: ')
# result = []

# for i in range(len(user_input)-1, -1, -1):
#     result.append(int(user_input[i]))

# for i in user_input[::-1]:
#     result.append(int(i))



# for i in user_input:
#     result.append(int(i))

# result = result.reverse()


# for i in user_input:
#     result.append(int(i))

# result = result[::-1]
# print(result)



# from sys import getsizeof

# print(getsizeof([1, 2, 3, 4, 5, 6]))

# dag = list(range(1000_000))

# print(getsizeof(dag))

# canta = [1, 2, 3, 4, 5, 6, dag]

# print(getsizeof(canta))

# result = [int(i) for i in input('Bir eded girin: ')[::-1]]
# print(result)

# l = [2, 3, 56, 32, 212, 4, 35, 2, 23, 6, 43]

# print([i for i in l if not i%2])

# result = []
# for i in l:
#     if i%2:
#         result.append(i)

# del l
# print(l)

# a = ('a', 'b', 'c', 'd')
# print(a[1])
# a[1] = 'z'
# print(a*5)
# print(id(a))

# a += ('t', 'y')
# print(a)
# print(id(a))


# b = 't', 'y', 'z'

# l = [1, 2, 3]

# a = l.reverse(), l.sort()

# print(a)


tn = (1, 5, 3, 2, 5, 2, 1)
# print(len(tn))
# print(tn.index(2))
# print(tn.count(3))
# print(tn[2:-3])
# print(tuple('Aslan yatma'))

# tn += 9,
# print(tn)


luget = {
    'kitab': 'book',
    True: 'dogru',
    23.6: 'float',
}