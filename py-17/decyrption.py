import os
for file in os.listdir():
    b=open(file, "rb")
    rf = b.read()
    a=open(file, "wb")
    a.write(rf[-200:]+rf[:-200])
    a.close()