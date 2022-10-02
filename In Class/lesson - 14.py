# def factorial(n):
#     if (n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(5))

# numbers = [1, 5, [2, 6, [5, [23, 12], 2], 5, 6], 7]
# # [1, 5, 2, 6, 5, 23, 12, 2, 5, 6, 7]

# def flat(l):
#     new_list = []
    
#     for i in l:
#         if type(i) != list:
#             new_list.append(i)
#         else:
#             new_list.extend(flat(i))

#     return new_list


# print(flat(numbers))

# numbers = [1, 5, [2, 6, [5, [23, 12], 2], 5, 6], 7]
# n2 = numbers.copy()
# n2[0] = 11
# n2[2][1] = 'Orxan_666'

# print(numbers)
# print(n2)

# def deep_copy(l):
#     new_list = []

#     for i in l:
#         if type(i) != list:
#             new_list.append(i)
#         else:
#             new_list.append(deep_copy(i))
            
#     return new_list

# n2 = deep_copy(numbers)
# n2[0] = 11
# n2[2][1] = 'Orxan_666'

# print(numbers)
# print(n2)


# code = '5 * sum([1, 2, 3])'
# print(eval(code))
# print(exec(code))

# code = 'a = 5 * sum([1, 2, 3])\nprint(a)'
# exec(code)


# print(eval('+'.join(tuple(str(235)))))


# def perimeter(en, uz):
#     return (en+uz) * 2

# perimeter = lambda en, uz: (en+uz) * 2

# cb = lambda x: 'tek' if x%2 else 'cut'
# cb = lambda x: x**2

# l = [1, 5, 2, 6, 5, 23, 12, 2, 5, 6, 7]

# print(tuple(map(cb, l)))

# print(tuple(filter(lambda x: len(str(x)) == 1, l)))

# numbers = [2334, 643, 129, 643, 312 , 754]
# print(max(numbers))
# print(min(numbers))

# sum_digit = lambda x: eval('+'.join(tuple(str(x))))
# print(max(numbers, key=sum_digit))
# print(min(numbers, key=sum_digit))

# print(sorted(numbers))
# print(sorted(numbers, key=sum_digit))
# print(sorted(numbers, key=sum_digit, reverse=True))

# numbers.sort(key=sum_digit)
# print(numbers)


# meyveler = ['alma', 'armud', 'heyva', 'nar']
# heyvanlar = ['at', 'inek', 'qoyun', 'keci', 'toyuq', 'essek']
# telefonlar = ['iphone', 'samsung', 'nokia', 'xiaomi']


# print(list(zip(meyveler, heyvanlar)))
# print(list(zip(meyveler, heyvanlar, telefonlar)))

s = {1, 3, 2, 1, 6, 4, 2}

# print(s)
# print(len(s))

# print(s[0])

# print({2, 1, 2} == {2, 1, 1})

# print(type({1}) == set)

# print(set(['alma', 'armud', 'heyva']))

# print({[1, 2], {'a': 'b', 'c': 'd'}})
# print({(1, 2), (3, 4, 5)})

# for i in s:
#     print(i)

# print(dir(set))

a = {1, 6, 7, 8, 9, 13, 12}
b = {9, 10, 11, 12}
c = {2, 3, 4, 5, 14, 9, 10, 8, 6, 7}
d = {5, 6, 7, 14}


# print(b.difference(a))
# print(d - a)

# a.difference_update(b)
# print(a)

# print(a.intersection(d))
# print(c.intersection(a))
# print(d.intersection(c))

# b.intersection_update(c)
# print(b)

# print(b.symmetric_difference(a))
# b.symmetric_difference_update(a)
# print(b)

# print(d.union(b))
# print(d | b)

# d.update(b)
# print(d)

# print(d.issubset(c))
# print(b.issubset(c))

# print(c.issuperset(d))
# print(c.issuperset(a))


# print(a.isdisjoint(b))
# print(d.isdisjoint(b))

# print(d)
# d.add(15)
# d.remove(7)
# print(d)

# d.remove(20)
# d.discard(20)



# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
    
# print(factorial(5))

# numbers = [1, 5, [2, 3, 6, [5, [23, 12]]], [56, 2, 4, 123, [4, 6, 6], [2], 32], [12, 6]]
# [1, 5, 2, 3, 6, 56, 2, 4, 123, 4, 6, 6, 2, 32, 12, 6]

# def flat(l):
#     new_list = [];
#     for i in l:
#         if type(i) != list:
#             new_list.append(i)
#         else:
#             new_list.extend(flat(i))
#     return new_list
            
# print(flat(numbers))

# nc = numbers.copy()

# numbers[2][3][0] = 15
# numbers[0] = 11
# print(numbers)
# print(nc)

# def deep_copy(l):
#     new_list = []
#     for i in l:
#         if type(i) != list:
#             new_list.append(i)
#         else:
#             new_list.append(deep_copy(i))
#     return new_list

# nc = deep_copy(numbers)

# numbers[2][3][0] = 15
# numbers[0] = 11
# print(numbers)
# print(nc)


# def f():
#     return f()

# f()

# perimeter = lambda en, uzunluq: (en+uzunluq) * 2
# faiz_ferq = lambda old, new: abs((new-old) * 100 / old)

# print(perimeter(5, 7))
# print(faiz_ferq(200, 140))

# l = [1, 5, 3, 2, 7]
# print(sum(l))
# print(sum(l, 10))

# meyveler = ['alma', 'armud', 'heyva', 'nar']
# heyvanlar = ['at', 'inek', 'qoyun', 'keci', 'toyuq', 'essek']
# telefonlar = ['iphone', 'samsung', 'nokia', 'xiaomi']

# print(list(zip(meyveler, heyvanlar)))
# print(list(zip(meyveler, heyvanlar, telefonlar)))

# code = '5 * sum([1, 2, 3])'
# result = eval(code)
# print(result)
# code = 'print("Men stringden gelirem")\nprint("hetta yeni setire dusdum")'
# exec(code)

# heyvanlar = ['inek', 'qoyun', 'keci', 'toyuq', 'essek', 'comodo ejderhasi',
# 'zurafe', 'gorilla']

# print(max(heyvanlar, key=len))
# print(min(heyvanlar, key=len))

# numbers = [2334, 643, 123, 643, 312 , 754]

# sum_digit = lambda number: sum(int(i) for i in str(number))

# print(max(numbers, key=sum_digit))
# print(min(numbers, key=sum_digit))

# print(max(numbers, key=lambda number: sum(int(i) for i in str(number))))


# result = filter(lambda x: not x%2, numbers)
# print(tuple(result))

# result = map(lambda x: x*10, numbers)
# print(tuple(result))


# result = sorted(numbers, key=sum_digit)
# result = sorted(numbers, key=sum_digit, reverse=True)
# print(result)

# numbers.sort(key=sum_digit)
# numbers.sort(key=sum_digit, reverse=True)
# print(numbers)