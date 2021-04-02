from random import randint
n=int(input("Podaj ilość liczb którą chcesz wylosować"))
i = 0
suma =0
iloczyn =1
while i<n:
    x=randint(1,8)
    print("Wylosowana liczna:",x)
    suma+=x
    iloczyn*=x
    i+=1
print("suma liczb wynosi:",suma)
print("iloczyn liczb wynosi:",iloczyn)
