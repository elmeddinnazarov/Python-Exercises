
#################### Sual 1 ####################
################################################

def write():
    for i in range(1000,0,-1):
        file.write(str(i).zfill(4)+"."+"\n")
try:
    file=open("py-13/reqem.txt","x")
    write()
    file.close()
except :
    file=open("py-13/reqem.txt","w")
    write()
    file.close()

#################### Sual 2 ####################
################################################





#################### Sual 3 ####################
################################################

from math import inf
mx=inf
mn=-inf
file=open("py-13/ders.txt","r")
lines=file.readlines()
for line in lines:
    line=line.split(" ")
    print(line)
    if mx > int(line[2]):
        print(mx,line[2],"den böyükdür")
        mx =int(line[2])