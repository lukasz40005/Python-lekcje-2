x=int(input('podaj liczbę: '))
p=2
while x>2:
    while x%p==0:
        x=x/p
        print(p)
    p=p+1
