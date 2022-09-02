


######################### Sual 1 ###########################
############################################################

# words=input("Qısaltmaq istediyiniz kelimeni daxil edin: ")
# def shorter(words):
#     res=""
#     l=[str(i[0]).capitalize() for i in words.split(" ")]
#     for i in l:
#         res+=i
#     print(res)
# shorter(words)

######################### Sual 2 ###########################
############################################################
"""chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') => 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'"""
# def chstr(text, **kwargs):
#     for i in kwargs:
#         text = text.replace(i, kwargs[i])
#     return text

    
# print(chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren', Kitabi='Kitabı'))


######################## Sual 3 ###########################
############################################################

# def hesabla(old,new):
#     result=(new-old)*100/old
#     if old>new:
#         result=-(result)
#         print("qiymet {0}% enmişdir".format(int(result)))
#     elif old<new:
#         print("qiymet {0}% qalxmışdır".format(int(result)))
#     return result

# hesabla(180,120)

######################## Sual 4 ###########################
############################################################

# eq = {'ə':'e','ü':'u','ı':'i','ğ':'gh','ş':'sh','ç':'ch', 'ö':'o'}
# def ascii_letters(text):
#     result = ''
#     for i in text.lower():
#         result += eq.get(i, i)
#     return result

# def ing_cevir(f):
#     def wrapper(*args, **kwargs):
#         result = f(*args, **kwargs)
#         result = ascii_letters(result)
#         return result
#     return wrapper

# @ing_cevir
# def salam_ver(ad, soyad):
# 	return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)

# print(salam_ver('Arif', 'Həsənov'))

######################## Sual 5 ###########################
############################################################

# from math import inf

# minimum=-inf
# maximum=inf
# l=[10,4,56,34,87,23,89,32,12,97]
# for i in l:
#     if minimum<i:
#         minimum=i
#     elif maximum>i:
#         maximum=i
# result=minimum-maximum
# print(result)




######################## Sual 5 ###########################
############################################################
