#NABEGHEHA.COM

a = (4, 6, 2, 8, 3, 1) 
print(a)

a = a + (9,)
print(a)

#Ezafe kardan 1 item be Yek index Khas:
a = a[:5] + (15, 20, 25) + a[:5]
print(a)

#convert Tuple Be List:
listx = list(a) 

#Yek Raveshe Dige:
listx.append(30)
a = tuple(listx)
print(a)