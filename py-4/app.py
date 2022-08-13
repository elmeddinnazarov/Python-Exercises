#################### Question 1 ####################
####################################################
ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']
print("\nFermada olan heyvanlar bunlardır: ", ferma)
print("\nkeçinin sırası: ",str(ferma.index("keci"))+"'dir.")
ferma.sort(reverse=False)
print("\nAd sırasına göre sıralama: ", ferma)
ferma.remove("at"), ferma.append("toyuq")
print("\nAt silinde ve toyuq elave edildi: ",ferma)
ferma.insert(0,"keci")
print("\nListenin başına keçi elave edildi: ",ferma)
del ferma[0:(int(len(ferma)/2))]
print("\nListenin yarısı silindi: ",ferma)
yeni=['at', 'qoyun', 'inek', 'inek', 'qoyun']
ferma.extend(yeni)
print("\nYeni gelen heyvanlar elave edildi: ",ferma)
ferma=ferma*3
print("\nHeyvanlar 3 qatına çıxarıldı: ",ferma)
ferma.sort(reverse=True)
print("\nTersine sıralama: ",ferma)
total=len(ferma)
inek=ferma.count("inek")
print("\nFermadaki inekler ümumi heyvanların "+str(int(round((inek*100)/total)))+"%'ni teşkil edir.")
ferma2=ferma.copy()
print("\n1-ci ferma: ",ferma,"\n\n2-ci Ferma: ",ferma2)
ferma.clear()
print("\nTemir işleri sebebiyle ferma temizlendi: ",ferma)
####################################################

#################### Question 2 ####################
####################################################

# result = [0, 0]
# a=0
# b=0
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# for i in numbers:
#     if i<0:
#         a=a+i
#     else:
#         b=b+i
# result[1]=float(a)
# result[0]=float(b)
# print(result)

####################################################

#################### Question 3 ####################
####################################################

# result=[]
# while True:
#     inp=input("Ededi daxil edin: ")
#     if not inp.isnumeric():
#         print("sadece eded daxil edin!")
#         continue
#     else:
#         result.extend(inp)
#         result.sort(reverse=True)
#     break
# print(result)

####################################################

#################### Question 4 ####################
####################################################

# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# numbers.sort(reverse=False)
# print("\n",numbers)
# print("\nEn kiçik eded:",numbers[0],"\nEn böyük eded:",numbers[-1])

####################################################

#################### Question 5 ####################
####################################################

# points=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# bad=0
# good=0
# excelent=0
# say=len(points)
# for i in points:
#     if i<=51:
#         bad+=1
#     elif i>80:
#         excelent+=1
#     else:
#         good+=1
# bad = int(round((bad*100)/say))
# good = int(round((good*100)/say))
# excelent = int(round((excelent*100)/say))
# result="""
# Sinifdeki ümumi telebe sayı: {}
# İmtahan neticelerinin ümumi ortalaması: {}
# Kəsilən tələbələrin ümumi faizi: {}% 
# Orta netice ile keçen telebeler: {}%
# Yüksək nəticə göstərən tələbələrin ümumu faizi: {}%
# """.format(say,sum(points)/len(points),bad,good,excelent)

# print(result)

