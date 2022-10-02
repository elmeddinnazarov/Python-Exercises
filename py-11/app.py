baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'kotex vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}



"""
, 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset',
 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'"""

# 1. step (Quşların xüsusiyyətlərinə "2 ayaq" əlavə edin.)c
quslar.add("2 ayaq")

# 2. step (Balıqların xüsusiyyətlərindən `"4 ayaq"` məlumatını çıxarın.)
baliqlar.discard("4 ayaq")

# 3. step (Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın.)
# print(amfibialar.intersection(cuculer))

# 4. step (Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın.)
# print(baliqlar.difference(amfibialar))

# 5. step (Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın.)
# print(baliqlar.isdisjoint(amfibialar))
# print(baliqlar.isdisjoint(surunenler))
# print(baliqlar.isdisjoint(quslar))
# print(baliqlar.isdisjoint(memeliler))

for i in sinifler:
    if baliqlar.isdisjoint(i)==True:
        print(baliqlar.isdisjoint(i))
        print(i)
    else:
        continue



