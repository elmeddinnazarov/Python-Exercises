userData = [
    {
        'debt': 12543,
        'payed': 341.346742,
        'payed_percent': 0.027214122777644904,
        'card_number': '5326-6644-1234-6432',
        'first_name': 'Akif',
        'last_name': 'Serifov',
        'father_name': 'Elekber',
    }
]

# cumle = '%s her gun %s %s oyrenir'
# print(cumle % ('Aslan', 'Python', 3) )
# print(cumle % ('Eli', 'Javascript', 'ES7') )
# print('Men %s oyrenirem' % 'Python')

"""
.format()
.format_map()
format()
f""
"""

# cumle = '{} her gun {} {} oyrenir'
# cumle = '{1} her gun {0} {2} oyrenir'
# cumle = '{} her gun {:*^15} {} oyrenir'
# cumle = '{} her gun {:*^15.5} {} oyrenir'
# cumle = '{} her gun {:*<7.3} {:0>5} oyrenir'
# cumle = '{0} {ne_zaman:$<10} {1:*<7.3} {2:0>5} oyrenir'

# print(cumle.format('Aslan', 'Python', 3, ne_zaman='Her Gun'))
# print(cumle.format('Eli', 'Javascript', 'ES7', ne_zaman='Arada'))

# message = 'Hormetli {}, siz {}% ile {}AZN kredit goturmusunuz. \
# Her ay odeyeceyiniz faiz deyeri: {:0>10.3f}AZN-dir'.format(
#     'Elmeddin', 33.333, 1254, 1254 * 33.333 / 100
# )

# message = 'Hormetli {soyad:.1}. {ad}. Sizin hesabinize {:,}$ medaxil edilib!'
# ad = 'Elmeddin'
# message = message.format(12851829751, ad=ad, soyad='Nezerov')
# print(message)

telebe_sayi = 150
ugurlu_telebe_sayi = 43

# print('Imtahana daxil olan {} telebeden {} qederi ugurlu olub.\
# Ugurlu olma faizi {:.3%} olmusdur'.format(
#     telebe_sayi, ugurlu_telebe_sayi, ugurlu_telebe_sayi / telebe_sayi
# ))


# data = {
#     'ts': telebe_sayi,
#     'us': ugurlu_telebe_sayi,
#     'ratio': ugurlu_telebe_sayi / telebe_sayi
# }
# print('Imtahana daxil olan {ts} telebeden {us} qederi ugurlu olub.\
# Ugurlu olma faizi {ratio:.3%} olmusdur'.format_map(data))

# address = r'D:\Users\Ujer\Desktop\K311\Python\lesson.py'
# address = repr('\n\t')
# print(address)


# ad = 'Elmeddin'
# medaxil = 128375891275
# message = f"Hormetli {'nezerov'.capitalize():.1}. {ad.upper()}. \
# Sizin hesabinize {medaxil:,}$ medaxil edilib!\
# Hesabiniza daxil olacaq faiz {7/15:.3%} olacaq"

# print(message)

# print(format(7/15, '.2%'))

# eded = 1253

# print(f"""
# Onluq: {eded:0>10},
# Ikilik: {eded:0>10b}      
# Sekkizleik: {eded:0>10o}
# On altiliq: {eded:0>10x}
# """)

