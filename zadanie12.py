"""n=int(input("Podaj liczbę: "))
a=1
b=1
if n==1:
    print(1)
elif n==2:
    print(1)
    print(1)
else:
    print(1)
    print(1)
    for i in range(3,n+1):
        c=a+b
        print(c)
        a=b
        b=c"""
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Podaj liczbę: "))
for i in range(1,n+1):
    print(fib(i))
