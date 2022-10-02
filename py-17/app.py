"""1. 1000 ədəd random yığılmış floatdan ibarət list hazırlayın. Daha sonra girilən listin ən böyük elementini tapan 2 funksiya hazırlayın. 
Birincisi parametrdəki listi sort edib, son elementi çıxarsın, digəri isə bu əməliyyat üçün seçilmiş alqoritm (infinity ilə başlayan ilk dəyərə
 sahib alqoritm) ilə işləsin. timeit ilə hazırladığınız iki funksiyanın sürətlərini ölçün"""
######################### Sual 1 ###########################
############################################################
# import math
# from random import random as r
# from timeit import timeit


# def random():
#     random_list=[]
#     for i in range(0,1000):
#         random_list.append(r())
#     return random_list
# random_list=random()

# def sort_method(random_list):
#     result=random_list.sort()
#     return random_list[-1]
# print(sort_method(random_list), timeit('sort_method(random_list)', 'from __main__ import sort_method, random_list', number=1000))

# def inf_method(random_list):
#     min_int=-(math.inf)
#     for i in random_list:
#         if i>min_int:
#             min_int=i
#     return min_int
# print(inf_method(random_list), timeit('inf_method(random_list)', 'from __main__ import inf_method, random_list', number=1000))
