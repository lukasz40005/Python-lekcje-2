a=int(input("Podaj pierwszą liczbę:"))
b=int(input("Podaj drugą liczbę:"))

if a>0 and b>0:
    while a!=0 and b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    print("NWD:",a)
else:
    print("Błędne dane")
input()
