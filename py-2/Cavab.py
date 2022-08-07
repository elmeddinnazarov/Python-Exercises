#################### Sual 1 ####################
################################################

# print("Girdiyiniz ededin hem 3, hem 7 ve hemde 8 e tam bölünüb bölünmediyini hesablayaq.")
# usinp = input("\nEdedi daxil edin: ")
# numbers = ["3", "7", "8"]
# a = 0
# if usinp.isnumeric():
#    usinp =int(usinp)
#    for i in numbers:
#        i = int(i)
#        if usinp%i==0:
#            print("\nDaxil Etdiyiniz eded "+numbers[a]+"'ə qalıqsız bölünür.\n")
#        else:
#            print("\nDaxil Etdiyiniz eded "+ numbers[a]+"'ə qalıqsız bölünmür.\n")
#        a+=1
# else:
#    print("\nxaiş edirem reqem daxil edin!\n")

################################################


#################### Sual 2 ####################
################################################

# cardId = input("Şexsiyet Vesiqesinin Seriasını ve Nömresini bitişik şekilde daxil edin: ")

# if cardId.isalnum():
#     if len(cardId) == 10 and cardId[0:3].isupper() and cardId[0:3].isascii() and cardId[3:].isnumeric():
#             print("düzdü qaqa")

#     else:
#         print("\nSeria veya Nömreni düzgün daxil etmediniz! Zehmet olmazsa aşağıdakı qaydalara uyğun daxil edin!\n")
#         print("-"*70)
#         print("\tQAYDALAR\n\n1. ilk 3 xarakter seria olmalıdır ve böyük herf ile yazılmalıdır!\n2. Daha sonra gelen 7 xarakter reqem olmalıdır!\n3. Seria ve nömre 10 simvoldan ibaret olmalıdır!\n")
#         print("-"*70)
    
# else:
#     print("Sadece herf ve reqem daxil edin!")

################################################


#################### Sual 3 ####################
################################################

# print("ASLAN Banka Xoş Geldiniz. ")
# enter = input("Düşük Faizli Kreditlerimizden Yararlanmaq Üçün 'Enter' Düymesine Basın.")
# if enter !="":
#     print("Yalnış giriş etdiniz.")
# else:
#     money = input("Kredit mebleğini daxil edin: ")
#     if money.isnumeric():
#         money = int(money)
#         if money < 2000:
#             print("Teessüf ki minimal kredit miqdarı 2000 AZN teşkil edir.")
#         elif 2000 <= money <= 10000:
#             result = money * 0.05
#             print("Götürdüyünüz kredit mebleğinin üzerine 5%, yeni "+str(int(result))+" AZN faiz hesablanacaq. Ve 24 ay müddetinde ödemeli olduğunuz toplam mebleğ "+str(int(result+money))+" AZN teşkil edir.\n24 ay erzinde aylıq ödenişiniz "+str(int((result+money)/24))+ " AZN teşkil edir.")
#         elif 10001 <= money <= 50000:
#             result = money * 0.04
#             print("Götürdüyünüz kredit mebleğinin üzerine 4%, yeni "+str(int(result))+" AZN faiz hesablanacaq. Ve 24 ay müddetinde ödemeli olduğunuz toplam mebleğ "+str(int(result+money))+" AZN teşkil edir.\n24 ay erzinde aylıq ödenişiniz "+str(int((result+money)/24))+ " AZN teşkil edir.")
#         elif 50001 <= money <= 200000:
#             result = money * 0.03
#             print("Götürdüyünüz kredit mebleğinin üzerine 3%, yeni "+str(int(result))+" AZN faiz hesablanacaq. Ve 24 ay müddetinde ödemeli olduğunuz toplam mebleğ "+str(int(result+money))+" AZN teşkil edir.\n24 ay erzinde aylıq ödenişiniz "+str(int((result+money)/24))+ " AZN teşkil edir.")
#         elif 200001 <= money <= 500000:
#             result = money * 0.02
#             print("Götürdüyünüz kredit mebleğinin üzerine 2%, yeni "+str(int(result))+" AZN faiz hesablanacaq. Ve 24 ay müddetinde ödemeli olduğunuz toplam mebleğ "+str(int(result+money))+" AZN teşkil edir.\n24 ay erzinde aylıq ödenişiniz "+str(int((result+money)/24))+ " AZN teşkil edir.")
#         else:
#             print("Teessüf ki maksimal kredit miqdarı 500000 AZN teşkil edir.")
    # else:
    #     print("Yalnız reqem girişi daxil edin.")

################################################
            
    
#################### Sual 4 ####################
################################################

# us = input("username: ")
# pswd = input("password: ")
# if 8 <= len(pswd) <= 40:
#     if pswd.isascii():
#         if not pswd.isnumeric() and not pswd.isalpha():
#             if not pswd.isupper() and not pswd.islower():
#                 print("Şifreniz Doğrudur.")
#             else:
#                 print("\nEn az bir böyük ve bir kiçik herf daxil edilmelidir.\n")
#         else:
#             print("\nŞifrenizde en azı bir herf ve bir reqem olmalıdır.\n")
#     else:
#         print("\nSadece ingilis elifbasından istifade edin.\n")
# else:
#     print("\nŞifreniz en az 8 karakterden ve en çox 40 karakterden ibaret olmalıdır.\n")
        
################################################