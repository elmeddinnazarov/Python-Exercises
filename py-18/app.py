######################## Sual 1 ###########################
############################################################

# import time
# s=input("saniye cinsinden geri sayım başlangıc nöqtesini qeyd edin: ")
# for i in range(int(s)):
#     s=int(s)-1
#     print(s,"saniye")
#     time.sleep(1)

######################## Sual 2 ###########################
############################################################

# import imp
# from multiprocessing.spawn import import_main_path
# from pathlib import Path
# current_dir = Path('.').absolute()
# aimed_dir=current_dir.parent.parent

# for path in aimed_dir.iterdir():
#     if path.is_file():
#         print(Path.suffix)




# from pathlib import Path

# current_path = Path('.').absolute()

# target_path = current_path.parent.parent

# for path in target_path.iterdir():
#     if path.is_file():
#         print(path.suffix)


######################## Sual 3 ###########################
############################################################


# import json
# import uuid
# import secrets

# js=open("info.json", "r")
# data=json.load(js)

# for i in data:
#     usr_id=str(uuid.uuid4())
#     token = secrets.token_urlsafe(16)
#     i["uuid"]=usr_id
#     i["token"]=token
# js.close()

# js=open("info.json", "w")
# json.dump(data, js)
# js.close()
