wiek = input("Podaj wiek: ")
kasa = input("Podaj stan gotówki: ")

if int(wiek) >=18:
    if int(kasa) >= 35:
        print("Możesz wejść!")
    else:
        print("Nie masz wystarczająco pieniędzy!")
else:
    print("Nie masz wystarczająco lat!")