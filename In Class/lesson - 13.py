# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
    
# print(factorial(5))



numbers = [1, 5, [2, 3, 6, [5, [23, 12]]], [56, 2, 4, 123, [4, 6, 6], [2], 32], [12, 6]]
# [1, 5, 2, 3, 6, 56, 2, 4, 123, 4, 6, 6, 2, 32, 12, 6]

def flat(l):
    new_list = [];
    for i in l:
        if type(i) != list:
            new_list.append(i)
        else:
            new_list.extend(flat(i))
    return new_list
            
print(flat(numbers))

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

perimeter = lambda en, uzunluq: (en+uzunluq) * 2
faiz_ferq = lambda old, new: abs((new-old) * 100 / old)

print(perimeter(5, 7))
print(faiz_ferq(200, 140))

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