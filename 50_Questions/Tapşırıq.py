################################################
#################### Sual 1 ####################

# for i in range(1500, 2700):
#     if not i%7 and not i%5:
#         print(i, end=", - ")

###############################################
################### Sual 2 ####################

# print("This program convert celsius to fahrenheit and fahrenheit to celsius.\nwhich service do you want?\n\n")
# while True:
#     inp=input("\nEnter '1' to convert celsius to fahrenheit,\nEnter '2' to convert fahrenheit to celsius.")
#     if not inp.isnumeric():
#         print("\nJust numbers please.")
#     elif inp=="1":
#         c=input("Enter Celsius: ")
#         if not c.isnumeric():
#             print("\nJust numbers please.")
#         else:
#             f=(int(c)*1.8)+32
#             print(str(int(f)))
#             break
#     elif inp=="2":
#         f=input("Enter Celsius: ")
#         if not f.isnumeric():
#             print("\nJust numbers please.")
#         else:
#             c=(int(f)-32)/1.8
#             print(str(int(c)))
#             break

###############################################
################### Sual 3 ####################

# import random
# intro_text="""
# This is the game that the program catch a random number between 1 and 9 and you have just 3 attempts to find the number.
   
#     Enter to Start!

#     Do your Best!

# """
# main_text="""
# Enter your guess: 
# """
# input(intro_text)
# rand_num=random.randint(1,9)
# c=1
# while True:
#     user_guess=input(main_text)
#     if c ==3:
#         print("Game Over!")
#         break
#     elif not user_guess.isnumeric():
#         print("\nEasy man! Write just number not anything else!")
#     elif not 1<= int(user_guess) <=9:
#         print("\nEasy man! Write just number between 1 and 9")
#     elif (int(user_guess)+2)==rand_num or (int(user_guess)-2)==rand_num:
#         print("Close Guess! You have just "+str((3-c))+" attempts, be carefull :)")
#         c+=1
#     elif (int(user_guess)-1)==rand_num or (int(user_guess)+1)==rand_num:
#         print("So Close! You have just "+str((3-c))+" attempts, be carefull :)")
#         c+=1
#     elif int(user_guess)==rand_num:
#         print("Congratulations!")
#         break
#     else:
#         print("Wrong Answer! You have just"+str((3-c))+" attempts, be carefull :)")
#         c+=1

    
###############################################
################### Sual 4 ####################





###############################################
################### Sual 5 ####################

# while True:
#     word=input("write a word: ")
#     if not word.isalpha():
#         print("Write just a word! not anything else!")
#     else:
#         break
# print(word[::-1])


###############################################
################### Sual 6 ####################

# numbers = [1,2,3,4,5,6,7,8,9,10,11]
# cüt =[]
# tek =[]

# for i in numbers:
#     if not i%2:
#         cüt.append(i)
#     elif i%2:
#         tek.append(i)

# print(len(cüt), len(tek))

###############################################
################### Sual 7 ####################
        
        
        

    
        
    
        
        




