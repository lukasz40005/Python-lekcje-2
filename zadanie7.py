a=int(input("Podaj pierwszą liczbę:"))
b=int(input("Podaj drugą liczbę:"))
if a<=0 or b<=00:
    print("Podałeś liczby niedodatnie")
else:
    if a >b:
        a,b=b,a #zamoiana iejscami(para ab)
    i=1
    while (a*i)%b!=0:
        i+=1
    print("NWW(", a,",", b, ")=", a*i)
input()
