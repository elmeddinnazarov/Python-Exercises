
######################## Sual 1 ###########################
############################################################

# physic = {
#     "f": lambda m, a: m*a,
#     "a": lambda v, t: v/t,
#     "s": lambda a, t: (a*(t**2)/2),
#     "Ep": lambda m, g, h: m*g*h,
#     "v": lambda s, t: s/t,
#     "W": lambda F, s: F*s,
#     "T": lambda f: 1/f,
#     "Ek": lambda m, v: (m*(v**2)/2),
#     "p": lambda Fn, S: Fn/S,
#     "Vsr": lambda S_total, T_total: S_total/T_total,
#     "Ew": lambda W, Q: W+Q,
#     "U": lambda W, q: W/q,
#     "I": lambda q, t: q/t,
# }
# print(physic.get("Ep")(5,4,3))


######################## Sual 2 ###########################
############################################################

# fac= lambda n:True if n==1 else n*fac(n-1) 
# print(fac(10))

######################## Sual 3 ###########################
############################################################

# letdict = {'a': 1, 'v': {'b': 2}, 'c': {'f': 3, 'c': 3, 'h': {'r': 5}, 'p': 3}, 'y': 9} 

# def maker(letdict):
#     newdict={}
#     for key,value in letdict.items():
#         if not type(value)==dict:
#             newdict[key]=value
#         else:
#             newdict.update(maker(value)) 
#     return newdict

# print(maker(letdict))

######################## Sual 4 ###########################
############################################################

# l=[85856, 73930, 95298, 57870,999999,99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400]

# def find_up(l):
#     from math import inf
#     mn =-inf
#     for i in l:
#         temp=[*str(i)]
#         temp = list(map(int, temp))
#         a=sum(temp)
#         if mn<a:
#             mn=a

#     return mn 

# print(find_up(l))

######################## Sual 5 ###########################
############################################################


# children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
# gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
# prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Socks': 10, 'Play Station': 1200}

# count=0
# for i in children:
#     print(i, prices[gifts[count]],"AZN deyerinde", gifts[count], "götürüb")
#     count +=1

######################## Sual 6 ###########################
############################################################

# l=[{1, 2}, {'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True, {5, 6}, False]
# """Listlər, Setlər, Dictonarylər, Booleanlar, İntegerlər, Floatlar, Stringlər"""
# new_list=[]
# for i in l:
#     if type(i)==list:
#         new_list.insert(-1,i)
#     if type(i)==dict:
#         new_list.insert(-1,i)
#     if type(i)==bool:
#         new_list.insert(-1,i)
#     if type(i)==int:
#         new_list.insert(-1,i)
#     if type(i)==float:
#         new_list.insert(-1,i)
#     if type(i)==str:
#         new_list.insert(-1,i)
# print(new_list)

