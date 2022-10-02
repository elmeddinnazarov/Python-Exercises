# l = [3, 12, 48, 7, 57, 41, 76, 62, 16, 48, 59, 53, 60, 79, 71, 81, 88, 26, 45, 72, 25, 65, 53, 88, 79, 34, 42, 40, 45, 92, 52, 85, 90, 16, 37, 50, 96, 67, 7, 59, 3, 41, 40, 58, 83, 16, 47, 23, 5, 22]

# new_list = print([i**2 for i in l if i%6==0])


# numbers = range(-100,101)

# result = [x*3 for x in numbers if x%7==0]

# print(result)

# from timeit import timeit
# def method2():
#     data = (1, 2, 3, True, False, 3.3)
#     return ('asdf',) + data + ((1, 2),)

# def method1():
#     data = (1, 2, 3, True, False, 3.3)
#     data_list = list(data)
#     data_list.append((1, 2))
#     data_list.insert(0,'asdf')
#     return tuple(data_list)

# result = timeit('method1()', 'from __main__ import method1')
# print(result)
# print(*[i for i in dir(str) if not i.endswith("__")], sep="\n")