from random import randint
from os import system

punkty=0
for i in range(10):
    system("cls")
    x=randint(2,9)
    y=randint(2,9)
    print(x,"*",y,"=", end="")
    wynik=int(input())
    if wynik==x*y:
        print("wynik poprawny")
        punkty+=1
    else:
        print("Błąd! poprawny wynik to:", x*y)
    input()
if punkty<3:
    print("ndst")
elif punkty<5:
    print("dop")
elif punkty<7:
    print("dst")
elif punkty<9:
    print("db")
elif punkty<10:
    print("bdb")
else:
    print("cel")
input()
