1.
def numbers(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'

print(numbers((int(input("Введите первое значение "))), (int(input("Введите второе значение ")))))

2.
def people(**kwargs):
    return list(kwargs.values())
 
 
print(people(name=input('Введите имя: '),
    surname=input('Введите фамилию: '),
    birthday=input('Введите дату рождения: '),
    town=input('Введите город проживания: '),
    email=input('Введите email: '),
    tel=input('Введите номер телефона: ')))

3.
def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)

print(my_func(1, 2, 3))

4.
def my_func(x, y):
    return x**y
print(my_func(int(input("Введите положительное число x - ")), (int(input("Введите отрицательное число y - ")))))

#второй способ не понял

def my_func():
    sum = 0
    while True:
        numbers = input('Введите числа через пробел или нажмите * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма равна {sum}. Выход')
                    return
                else:
                    sum = sum + int(i)
            except ValueError:
                print('Введите число или нажмите *')
        print(f'Сумма равна {sum}')


my_func()


    

    
