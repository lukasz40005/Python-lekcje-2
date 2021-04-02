a=int(input("Podaj liczbę:"))
if a>0:
    i=1
    while i<=a:
        if a%i==0:
            print(i)
        i+=1
#    for i in range(a,0,-1):
#        if a%i==0:
 #           print(i)
else:
    print("Błędne dane")
