
def func(x):
    return x * x
zmienna = func
print(zmienna(5))

def func2(f1, x):
    return f1(x) * x

print(func2(func, 5))