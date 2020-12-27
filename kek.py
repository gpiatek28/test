import random

liczba = random.randint(1,20)

print('Mam na myśli liczbę z zakresu od 1 do 20')

for zgadywane in range (1,7):
    print('Spróbuj odgadnąc liczbę')
    guess = int(input())
    print("próba:",zgadywane,"/6")

    if guess > liczba:
        print('Liczba jest zbyt duża')
    elif guess < liczba:
        print('Liczba jest za mala')
    else:
        break

if guess == liczba:
    print('Doskonale' +str(zgadywane))
else:
    print('nie udało sie, liczba to:'+str(liczba))