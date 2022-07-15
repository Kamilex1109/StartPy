Zmienna = 1
Zmienna2 = "Abc"
lista = [Zmienna, Zmienna2]

print(lista)

print(lista[1])     #Wywołanie konkretnego elemnetu z listy
print(lista[0])     #Wywołanie konkretnego elemnetu z listy

lista[1] = "BDC"
print(lista)        #Zamienianie poszczególnych elementów

Tekst1 = "Hello world"
print(Tekst1[1])
"""
print(Tekst1*3)     #Mnożenie list
print("Ilość elementów: ", len(Tekst1))

lista.append(["abc"])       #append dołącza na samym końcu listy
print(lista)
print(lista[2][0][1])

lista.insert(2,1)           #dołączanie w dowolnym miejscu
print(lista)

print("Ilość: ", lista.count(3))        #ilość wystąpień danego obiektu
print("Indeks: ", lista.index("f"))     #miejsce występowania w liście
"""
lista.remove("1")                       #usuwa dany element po indeksie
print(lista)
print("Min: ", min(lista2))
print(lista.reverse())                  #zamiana kolejności na liście
print(lista.clear())                    #wyczyszczenie listy




