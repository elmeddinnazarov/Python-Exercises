######################## Sual 1 ###########################
############################################################

# from math import pi
# while True:
#     chc=input("Koni hesablamaq üçün '1', Küre hesablamaq üçün '2' daxil edin: ")
#     if chc =="1":
#         r=int(input("radiusu daxil edin: "))
#         h=int(input("hündürlüyü daxil edin: "))
#         V=(1/3)*(pi*h*(pow(r,2)))
#         print(V)
#         break
#     elif chc =="0":
#         r=int(input("radiusu daxil edin: "))
#         V=(4/3)*(pi*(pow(r,3)))
#         print(V)
#         break
#     else:
#         break

######################## Sual 2 ###########################
############################################################
# from cgitb import reset
# from math import factorial as f
# def Combination(n,r):
#     result=f(n)/f(r)*f((n-r))
#     return result

# def Permutation(n,r):
#     result=f(n)/f((n-r))
#     return result

# while True:
#     chc = input("press 'C' to calculate Combination, press 'P' to calculate Permutation: ")
#     if chc.upper() == "C":
#         n = int(input("write 'n' value please: "))
#         r = int(input("write 'r' value please: "))
#         print(Combination(n,r))
#         break
#     elif chc.upper() == "P":
#         n = int(input("write 'n' value please: "))
#         r = int(input("write 'r' value please: "))
#         print(Permutation(n,r))
#         break
#     else:
#         break

######################## Sual 3 ###########################
############################################################
# import random
# while True:
#     visitors=[]
#     count= input("Give Away programınızda neçe iştirakçı olacaq daxil edin: ")
#     if not count.isnumeric():
#         print("sadece reqem girişi edin!")
#     else:
#         c=int(count)
#         say=1
#         for i in range(1,(c+1)):
#             v=input("{}. iştirakçının adını daxil edin: ".format(say))
#             visitors.append(v)
#             say+=1
#     break

# def choiser(visitors):
#     winner=random.choice(visitors)
#     visitors.remove(winner)
#     return winner

# input("Give Away programını başlatmaq üçün 'Enter'e basın! ")
# say=1
# for i in range(1,(c+1)):
#     choiser(visitors)
#     print("{}. Qalib {} adlı iştirakçıdır. TEBRİKLER".format(say,winner))
#     say+=1


######################## Sual 4 ###########################
############################################################
    



######################## Sual 5 ###########################
############################################################

# import random

# def loto():
#     num_1=random.sample(range(1,10),2)
#     num_2=random.randrange(10,20)
#     num_3=random.sample(range(20,30),2)
#     num_4=random.sample(range(30,40),2)
#     num_5=random.sample(range(40,50),2)
#     num_6=random.sample(range(50,60),2)
#     num_7=random.randrange(60,70)
#     num_8=random.sample(range(70,80),2)
#     num_9=random.randrange(80,91)
#     num_empty="  "
#     loto_format="""
#     -------------------------------------
#     | {}  {}  {}  {}  {}  {}  {}  {}  {} |
#     | {}  {}  {}  {}  {}  {}  {}  {}  {} |
#     | {}  {}  {}  {}  {}  {}  {}  {}  {} |
#     -------------------------------------
#     """.format(num_1[0],num_2,num_3[0],num_4[0],num_5[0],num_6[0],num_empty,num_8[0],num_9," ",num_empty,num_3[1],num_empty,num_5[1],num_empty,num_empty,num_8[1],num_empty,num_1[1],num_empty,num_empty,num_4[1],num_empty,num_6[1],num_7,num_empty,num_empty)
#     print(loto_format)
# while True:
#     input("Yeni loterya yaratmaq üçün 'Enter' düymesine basın: ")
#     loto()
#     sec=input("yeni bir loterya yaratmaq üçün '1', çıxmaq üçün 'q' daxil edin: ")
#     if sec == "1":
#         pass
#     else: 
#         break


######################## Sual 6 ###########################
############################################################

# from datetime import datetime as date, timedelta as soon
# """Yer kürəsi ilə Pluton arasındakı məsfə 5.058 milyard kilometrdir. Saatda 90 km/saat sürətlə, fasiləsiz hərəkət edən Niva maşını hansı tarixdə Plutona çatar?"""

# s=5058000000
# v=90
# t=int((s/v)/24)
# today=date.now()
# result=today+soon(days=t)
# print("Niva Plutona {} bu tarixde çatacaq:)".format(result))

######################## Sual 7 ###########################
############################################################

