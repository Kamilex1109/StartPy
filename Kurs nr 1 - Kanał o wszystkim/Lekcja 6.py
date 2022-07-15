
from random import randint

"""
DoOdgadniecia = randint(1,10)
for i in range(100):
    print(DoOdgadniecia)
    liczba = input("Podaj liczbę: ")
    if int(liczba) > DoOdgadniecia:
        print("Za dużo!")
    elif int(liczba) < DoOdgadniecia:
        print("Za mało!")
    elif int(liczba) == DoOdgadniecia:
        print("Trafiłeś!")
"""

los = randint(1,10)
odp = -1
i = 0
print("Podaj liczbę z przedziału 1 - 10")
while odp != los:
    i += 1
    print("To Twoja"+ " " + str(i) + " " + "próba!")
    odp = input("Podaj liczbę: ")
    if int(odp) > los:
        print("Za dużo!")
    elif int(odp) < los:
        print("Za mało!")
    elif int(odp) == los:
        print("Trafiłeś!")
        print("Trafiłeś za" + " " + str(i) + " " + "razem!")
        break
