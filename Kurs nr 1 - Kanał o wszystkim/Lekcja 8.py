lista = ["Kurs", "Pythona", "Kanał", "o", "Wszystkim"]
print(len(lista))
"""
i = 0
while i < len(lista):
    print(lista[i])
    i += 1
"""
for x in lista:
    print(x)

print(list(range(10)))              #wyświetla od 0 do 9
print(list(range(3, 10)))           #wyświetla od 3 do 9
print(list(range(3, 20, 3)))        #wyświetla od 3 do 20 co 3

for y in range(10):  #wyświetla od 0 do 9
    print(y)