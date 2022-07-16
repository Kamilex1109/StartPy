#FUNKCJE
# print("Funkcja")    #Funkcja wyświetlania na konsoli

def funkcja_test():  #Tworzenie własnych funkcji
    print("Funkcja")

funkcja_test()       #Wywołanie funkcji

def dodaj(x):
    print(x+1)

#dodaj(5)

def dodaj(x, y = 4):    #zadanie wartości domyślnej w y
    print(x + y)

dodaj(2, 3)
dodaj(5)

def dodaj(x, y = 4, z = 0):    #zadanie wartości domyślnej w y
    return x + y + z
print(dodaj(2,3))