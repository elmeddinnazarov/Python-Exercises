# def upunion(*args):
#     result = ''
#     for i in args:
#         result += i[0].upper()
    
#     return result

# print(upunion('birlesmis', 'milletler', 'teskilati'))




# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') => 'Kitabi \
# sehife-sehife oxumalisan ki, oyrenesen'

# def chstr(text, **kwargs):
#     for i in kwargs:
#         text = text.replace(i, kwargs[i])
#     return text
    
# print(chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren'))
    
    
    
    
"""   Task 3    """
# def find_percent(old,new):
#     result = (new - old)*100/old
    
#     if result > 0:
#         print(f" qiymet {result}% artmisdir")
#     elif result<0:
#         print(f" qiymet {-result}% azalmisdir")
#     else:
#         print("nothing changed")
    

# find_percent(2000, 600)


"""   End of Task 3   """




"""   Task 4   """ 




eq = {'ə':'e','ü':'u','ı':'i','ğ':'gh','ş':'sh','ç':'ch', 'ö':'o'}
def ascii_letters(text):
    result = ''
    for i in text.lower():
        result += eq.get(i, i)
    return result

def ing_cevir(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        result = ascii_letters(result)
        return result
    return wrapper

@ing_cevir
def salam_ver(ad, soyad):
	return 'Salam hörmətli {} {}, necəsiniz?'.format(ad, soyad)


print(salam_ver('Arif', 'Həsənov'))



"""   End of  Task 4   """ 


# from math import inf 

# maximum = -inf
# minimum = inf

# numbers = [6, 3, 8, 9, 24, 4]

# for i in numbers:
#     if maximum < i:
#         maximum = i
#     if minimum > i:
#         minimum = i
        
# print(maximum - minimum)