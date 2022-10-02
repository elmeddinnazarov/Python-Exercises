# # print('asdf\n 34edg \tgdg \aggg')

# # print('Python 3 1991-ci ilde Guido Van Rossum terefinden\
# #  yaradilib. Interpereter bir proqramlasdirma dilidir')

# # print("""Yeni
# # Setr""")


# # print('Yeni setir yaratmaq ucun \\n escapeinden istifade olunur')

# # print('You can\'t do it')

# # address = r'D:\Users\Ujer\Desktop' # 'D:\\Users\\Ujer\\Desktop'

# # print(address)

# # a = [1, 2, 3]
# # b = [1, 2, 3]

# # print(a == b)
# # print(a is b)

# # print(bool([]))

# print(type([]), type({}))


# l = [1, 2, 6.7, 'asdf', True, False, None, [1, 2, 3]]

# for i in l:
#     print(i)

# # print(l[0], l[1], l[-3])
# # print(l[1: -3])
# # print(l[::-1])
# # print(l[-1][-1])
# print(l[-1][::-1])
# # l[2] = 10.1
# l[1:4] = ['a', 'b', 'c', 'd' , 'e']
# print(l)
# # del l[1: 4]
# # del l[-1]
# # print(l)

# # l*3
# # print(l)

# # print([1, 2, 3] + ['a', 'b', 'c'])

# print(dir(list))

# meyveler = ['alma', 'saftali', 'heyva', 'armud', 'nar']
# meyveler.append('portagal')
# meyveler.insert(1, 'erik')
# meyveler.insert(0, 'nar')
# meyveler.pop()
# meyveler.pop(0)
# meyveler.remove('armud')
# meyveler.reverse()
# meyveler.sort()
# meyveler.sort(reverse=True)

# l = [53, 123 ,64, 12, 54, 342, 75, 64, 123, 64]
# # print(l.sort())
# # l.sort(reverse=True)
# # print(l)
# # print(meyveler)
# # d = l
# # d = l.copy()    
# # l.append(10)
# # print(d)
# # print(l)

# # l.clear()
# # print(l)

# # print(l.index(64))
# # print(l.count(64))
# # print(64 in l)

meyveler = 'alma, armud, heyva, nar'

# print(meyveler.split(', '))

# # nomre = '+994-55-666-77-88'
# # print(nomre.split('-'))

# # value = '12345'
# # print(list(value))

# # meyveler = ['alma', 'armud', 'nar', 'heyva', 'saftali']
# # m1, m2, m3, *m4 = meyveler

# # print(m4)


# print(meyveler, sep='---')
# print(*meyveler, sep='---')
# print('alma', 'armud', 'nar', 'heyva', 'saftali', sep='---')

# # print(*'elialfa', sep='+++')

# # l = ['e', 'ə']
# # print('elmeddin'.replace(*l))
# # print('elmeddin'.replace('e', 'ə'))

# # a = '123456789'
# # print(*a[::-1], sep=' saniye\n', end=' saniye\nBitdi!')
# # print('9', '8', '7', '6', '5', '4', '3', '2', '1', sep=' saniye\n', end=' saniye\nBitdi!')