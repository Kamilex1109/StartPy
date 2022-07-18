x = 12
y = 0

try:                                    #spróbuj przeliczyć
    print(x / y)
    print("Przeliczono!")
except ZeroDivisionError:               #Musi być po try i ustala wyjątek
    print("Nastąpiło dzielenie przez zero!")

try:  # spróbuj przeliczyć
    print(x / y)
    print("Przeliczono!")
except ZeroDivisionError:               #Musi być po try i ustala wyjątek konkretny (dzielenie przez zero)
    print("Nastąpiło dzielenie przez zero!")
except TypeError:
    print("Nastąpiło sumowanie typów!")
except (ZeroDivisionError, TypeError):
    print("Wystąpił 1 z 2 błędów!")
except:
    print("Jakiś inny błąd!")           #Wywołanie w przypadku wszytkich rodzaji błędów

finally:
    print("Wykonam się i tak!")         #Blok finally i tak się wykona. Nie ma na niego wyjątków!
