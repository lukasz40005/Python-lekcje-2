n=str(input("Podaj ciąg znaków: "))
liczba=len(n)
def policz(kod, element):
    ile = 0
    for i in range(len(kod)):
        if kod[i] == element:
            ile = ile + 1
    return ile
print(n)
print(policz(n,'a'))
print(liczba)


