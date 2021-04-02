a=int(input("Podaj liczbę:"))
i=1
silnia=1
if a>=0:   
    while i<=a:        
        silnia*=i
        i+=1
    print("Wynik:", silnia)         
else:
    print("błąd")
