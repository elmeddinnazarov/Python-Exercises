# from pathlib import Path

# current_dir = Path('.').absolute()
# file_dir = Path('file1.mp4').absolute()
# env_dir = Path('demoenv').absolute()
# mp3 = Path('mahni.tar.gz.mp3').absolute()
# olmayan_folder = Path('./alfa_list/aze_alfas/baku_alfa/alishkaalfa')

# val = current_dir
# val = type(current_dir)
# val = file_dir
# val = file_dir.absolute()
# val = file_dir.parts
# val = file_dir.drive
# val = tuple(file_dir.parents)
# val = env_dir.parent.parent.parent
# val = file_dir.name
# val = mp3.suffix
# val = mp3.suffixes
# val = mp3.stem
# val = Path(Path(mp3.stem).stem).stem
# val = mp3.as_posix()
# val = file_dir.as_uri()
# val = mp3.is_absolute()
# val = Path(mp3.name).is_absolute()
# val = mp3.is_relative_to(r'D:\Users\Ujer\Desktop')
# olmayan_folder.mkdir(parents=True)

# print(val)


# from secrets import token_urlsafe

# print(token_urlsafe(25))

# import uuid
# print(uuid.uuid4())

# import json

# data = """[
#    {
#       "title": "M&M Food Market",
#       "price": "17.0616609356653"
#    },
#    {
#       "title": "Soprole",
#       "price": "11.6234613464323"
#    },
#    {
#       "title": "Kinder",
#       "price": "2.62073436454904"
#    }
# ]"""

# l = json.loads(data)

# print(l[0]['title'])

# with open('data_source.json') as file:
#     l = json.load(file)
    
# print(l[-3:])

# a = [1, 2, None, True, False]

# print(json.dumps(a))

# with open('new-data.json', 'w') as file:
#     json.dump(a, file)
    
    
from pressure import get_pressure
print(get_pressure(15, 12, 10, 5))

# import sys
# print(*sys.path, sep='\n')
