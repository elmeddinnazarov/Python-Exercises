file = open("py-14/hide-image.png","rb")
a= file.read()
file2=open("py-14/image2.png","wb")
file2.write(a[::-1])
file2.close()