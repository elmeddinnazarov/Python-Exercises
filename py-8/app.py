
######################### Sual 1 ###########################
############################################################

# print("\nBu program sizin yazdığınız cümlenin her bir herfini Elifbada özünnen sonrakı herf ile deyişdirib ekranda gösterecek!\n")
# text=input("Cümle yazın: ")
# result=""
# for i in text:
#     char=ord(i)
#     if 65<=char<=90 or 97<=char<=122:
#         result+=chr(char+1)
#     else:
#         result+=i
# print(result)

######################### Sual 2 ###########################
############################################################

# text=input("Cümle yazın: ")
# result="" 
# for char in text:
#     char_ord=ord(char)
#     if 65<=char_ord<=90 or 97<=char_ord<=122:
#         result+=str(char_ord)+", "
#     else:
#         result+=char
# print(result)
        
####################### Sual 3 #############################
############################################################

# farm = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# prices = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
# prices_1={}
# prices_2={}
# farm_dict={}
# farm=list(farm)
# total_1=0
# total_2=0
# x=int(len(farm)/2)
# farm_1=farm[:x]
# farm_2=farm[x:]

# for i in farm_1:
#     c=farm_1.count(i)
#     prices_1[i]=farm_1.count(i)

# for i in farm_2:
#     c=farm_2.count(i)
#     prices_2[i]=farm_2.count(i)

# c=0
# for i in farm:
#     if not farm[c] in farm_dict:
#         farm_dict[i]=farm.count(i)
#     c+=1
    
# for i in prices_1:
#     total_1+=prices_1[i]*prices[i]

# for i in prices_2:
#     total_2+=prices_2[i]*prices[i]

# result="""
# {}
# Fermadakı heyvanların sayı: {}
# {}
# Fermadakı heyvanların qiymetleri: {}
# {}
# Böyük qardaşa düşen pay: {}
# {}
# Böyük qardaşın fermasının ümumi deyeri: {}
# {}
# Kiçik qardaşa düşen pay: {}
# {}
# Kiçik qardaşın fermasının ümumi deyeri: {}
# {}
# Böyük qardaşın kiçik qardaşa vermeli olduğu mebleğ: {}
# {}
# """.format("-"*100,farm_dict,"-"*100,prices,"-"*100,prices_1,"-"*100,total_1,"-"*100,prices_2,"-"*100,total_2,"-"*100,int((total_1-total_2)/2),"-"*100)

# print(result)


######################### Sual 4 ###########################
############################################################

# farm = ['inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek',
#  'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 
#  'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 
#  'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek']

# prices = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# farm_dict={}
# c=0
# for i in farm:
#     if not farm[c] in farm_dict:
#         farm_dict[i]=farm.count(i)
#     c+=1

# while True:
#     animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvanın adını daxil edin: ')
#     if not animal.isalpha() or not animal.isascii():
#         print("Heyvanın adını düzgün daxil edin ve sadece ingilis şriftlerinden istifade ettiyinizden emin olun.")
#     else:
#         if animal in farm_dict:
#             nisbet=round(sum(list(farm_dict.values()))/farm_dict[animal],2)
#             if animal in prices:
#                 price=prices[animal]
#             result="""
#             Axtarılan Heyvan: {}
#             {}'n Fermadakı sayı: {}
#             Fermadakı diger heyvanlara olan nisbeti {} %
#             Heyvanın satış qiymeti: {} AZN
#             """.format(animal.capitalize(),animal.capitalize(),farm_dict[animal],nisbet,price)
#             print(result)
#             choose=input("Başqa heyvan axtarmaq üçün 'Y', Çıxmaq üçün 'Q' daxil edin\n....")
#             if choose=="y" or choose=="Y":
#                 pass
#             else:
#                 print("Bizi seçdiyiniz üçün teşekkür ederik.")
#                 break
#         elif not animal in farm_dict:
#             choose=input("Bu heyvan fermada yoxdur. Başqa heyvan axtarmaq üçün 'Y', Çıxmaq üçün 'Q' daxil edin\n....")
#             if choose=="y" or choose=="Y":
#                 pass
#             else:
#                 print("Bizi seçdiyiniz üçün teşekkür ederik.")
#                 break


######################### Sual 5 ###########################
############################################################

# inp=input("binary sisteme çevirmek istediyiniz metini daxil edin: ")
# l=[]
# for i in inp:
#     l.append(str(bin(ord(i)))[2:])
# print(*l)

######################### Sual 6 ###########################
############################################################

# print("CSS rengini RGB formatında daxil edin\n")
# condution=True
# while condution:
#     inp=input("color: ")
#     if not inp[:4]=="rgb(" or not inp[-1]==")" or not len(inp)==16 or not inp.count(",")==2:
#         print("\nrgb(***,***,***) formatında daxil edin")
#     else:
#         rslt=inp[4:-1]
#         l=rslt.split(",")
#         c=0
#         result=""
#         for i in l:
#             if int(l[c])>255:
#                 st=2
#                 pass
#             else:
#                 st=0
#                 hex_result=hex(int(l[c]))
#                 no_hex=hex_result[2:]
#                 result+=no_hex
#                 c+=1
#                 condution=False
#         if st==2:
#             print("RGB rengleri 255'den yuxarı ola bilmez")
            
# print("color: #",result,sep="")


######################### Sual 7 ###########################
############################################################

