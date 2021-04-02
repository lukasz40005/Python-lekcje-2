a=int(input("Podaj cyfrę:"))
i=1
silnia=1
if a>0:
    while i<a:
        silnia*=a
        a-=2
        if a==2 or a==1:
            
            print("Wynik:", silnia)
else:
    print("błąd")
input()
