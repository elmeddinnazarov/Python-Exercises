# Istifadəçi sizə "5 salam" şəklində solda ədəd, ortada, boşluq, sağda isə bir input verəcək. Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər yazıb, istifadəçiyə qaytarın. Örnək yuxaridakı inputun outputu salam salam salam salam 
# salam  

# user_inp = input("melumat daxil girin: ")
# 5 salam, 3 necesen, 10 alma

# info_list = user_inp.split(" ")

# print((info_list[1] + ' ') * int(info_list[0]))


# l = ['alma', 'armud', 'heyva', 'nar', 'saftali']


# result = {i:len(i) for i in l}

# print(result)

# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]
# username = input("Enter your username: ")
# password = input("Enter your password: ")

# user_not_found = True
# for i in users:
#     if i['username'] == username:
#         user_not_found = False
#         if i['password'] == password:
#             if not i['blocked']:
#                 print("Welcome",i['name'])
#             else:
#                 print("Siz blok olunubsunuz")
#         else:
#             print("password is wrong")
#         break

# if user_not_found:
#     print('User doesn\'t exist')


user_info = {
    'firstname': 'Elvin',
    'lastname': 'Huseynov',
    'username': 'elivin_h_ov',
    'password': '12345',
    'birthday': '19-08-1997'
}

# input: firstname Elcin, username elchina, birthday 18-08-2000

new_info = input("Melumati daxil edin: ")

new_infoup = new_info.split(", ") # ["firstname Elcin", "username elchina", "birthday 18-08-2000"]

info = [i.split() for i in new_infoup]

info = dict(info)

user_info.update(info)

print(user_info)