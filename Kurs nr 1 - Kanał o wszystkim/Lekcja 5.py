"""
i = 0
while i <= 5:
    print(i)
    i += 1
print("Koniec!")
"""

"""    
while i <= 5:
    print(i)
    i += 1
else:
    print("Koniec!")
"""
i = 0
while True:
    i += 1
    if i % 2 ==0:
        continue
    print(i)
    if i > 10:
        break
print("Koniec!")


"""
while True:
    print(i)
    i += 1
    if i >= 1000:
        break
    continue
print("Koniec!")
"""