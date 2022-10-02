# import time
# user_inp = input("Enter a number: ")

# for i in range(int(user_inp),-1,-1):
#     time.sleep(1)
#     print(i)

# print("zaman bitdi")    
    


"""    Task 2   """

# from pathlib import Path


# current_path = Path('.').absolute()


# target_path = current_path.parent.parent

# for path in target_path.iterdir():
#     if path.is_file():
#         print(path.suffix)
        

import json
import uuid
import secrets

with open('data.json', 'r') as file:
    info_data = json.load(file)



for user in info_data:
    user_id = str(uuid.uuid4())
    token = secrets.token_urlsafe(16)
    user['id'] = user_id
    user['token'] = token

with open('data.json', 'w') as new_file:
    json.dump(info_data, new_file)