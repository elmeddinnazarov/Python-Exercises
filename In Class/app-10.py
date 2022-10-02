
# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# kq_ferma = ferma[:len(ferma)//2]
# bq_ferma = ferma[len(ferma)//2:]

# kqf_qiymet = 0
# bqf_qiymet = 0

# for i in kq_ferma:
#     kqf_qiymet += qiymetler.get(i) 
    
# for i in bq_ferma:
#     bqf_qiymet += qiymetler.get(i)


# if kqf_qiymet > bqf_qiymet:
#     borc = (kqf_qiymet - bqf_qiymet) / 2
#     print(
#         'Kicik Qardas, Boyuk Qardasa {} qederinde pul vermelidir.'
#         .format(borc)
#     )
# elif bqf_qiymet > kqf_qiymet:
#     borc = (bqf_qiymet - kqf_qiymet) / 2
#     print(
#         'Boyuk Qardas, Kicik Qardasa {} qederinde pul vermeldir.'
#         .format(borc)
#     )
# else:
#     print(
#         'Dagilisin!'
#     )
    

# print(
#     f"""
#     Boyuk Qardasin Fermasinin deyeri {bqf_qiymet:,} qederdir
#     Kicik Qardasin Fermasinin deyeri {kqf_qiymet:,} qederdir
#     Qardaslar arasinda olan borc : {int(borc)}
#     """
    
# )




# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
# farm = ['inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek']
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}



# text = f"""
# Axtarilan Heyvan: {animal}
# {"-"*10}
# Fermadaki {animal} sayi:  {farm.count(animal)}
# Diger heyvanlara olan faizi: {farm.count(animal)/len(farm):.2%}
# {animal} umumi qiymeti: {qiymetler[animal]*farm.count(animal)} AZN
# """
# print(text)

text = 'The   quick brown fox jumps over the lazy dog.'

def reverse_words(text):
#     return ' '.join([i[::-1] for i in text.split()])
    result = ''
    word = ''
    for i in text:
        if i != ' ':
            word += i
        else:
            if word:
                result += word[::-1]
                word = ''
            result += i
    result += word[::-1]
    return result


print(reverse_words(text))