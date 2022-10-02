# def get_perimeter(width, height):
    # return (width + height) * 2
    # print( (width + height) * 2)
    
# print(get_perimeter(5, 10))



# def salam_ver(debt, name='Anonim'):
#     return f'Salam hormetli {name}, sizin borucunuz {debt}AZN-dir'

# print(salam_ver(15, 'Alishka'))
# print(salam_ver(20))

# def topla(ilkin, *args, **kwargs):
#     for i in args:
#         ilkin += i
#     print(f'{kwargs.get("name")} adli ve {kwargs.get("id")} IDli musterimiz,\
# Sizin hesabinizde {ilkin}AZN qeder balans vardir')
    
# topla(10, 35, 12, 78, 32, 26, name='Ali', id='12515631')

# alfa = 'Eli'

# def f():
#     a = 5
#     b = 3
    # print(locals())
    # return a + b + c

# c = 3

# print(f())
# f()

# d = 5
# def sqr_d():
    # d**=2
    # global d
    # global c
    # d = d ** 2
    # c = 3 * d
    
# sqr_d()
# print(d)


# print(globals())
# globals()['student'] = 'Aslan'

# print(student)

# print(__name__)

# def ftoc(temp):
#     return (temp-32) * 5/9

# def ktoc(temp):
#     return temp - 273

# def boil(current, callback=None, bt=100):
#     if callback:
#         current = callback(current)
#     return bt - current

# print(boil(70, ftoc))

eq = {'ə': 'e', 'ü': 'u', 'ç': 'ch', 'ş': 'sh', 'ı': 'i', 'ğ': 'gh', 'ö': 'o'}
def change_letters(text):
    result =''
    for i in text.lower():
        result += eq.get(i, i)
    return result

def shrift_deyis(f):
    def wrapper(name, debt, percent=10):
        result = f(name, debt, percent)
        result = change_letters(result)
        return result
    return wrapper

def shrift_deyis(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        result = change_letters(result)
        return result
    return wrapper

@shrift_deyis
def borc_hesabla(name, debt, percent=10):
    return f'Hörmətli {name}. Sizin bankımıza bu ay üçün {debt * percent / 100}AZN borcunuz vardır'

@shrift_deyis
def melumat_ver(first_name, last_name, balance):
    return f'Hörmətli {first_name:.1}. {last_name}. Sizin hesabınızda {balance} AZN məbləğində pul vardır'

# borc_hesabla = shrift_deyis(borc_hesabla)

# print(borc_hesabla('Elmeddin', 2500))
print(melumat_ver(balance=3000, last_name='Əlizadə', first_name='Əli'))