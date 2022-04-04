def fact(n):
    number = 1
    for i in range(1, n+1):
        number = i*number #number*=i
        yield number


n = int(input("Введите число, чтобы узнать его факториал: "))
for el in fact(n):
    print(el)