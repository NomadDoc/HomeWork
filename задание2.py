list = input("Заполните список - ").split()
list[:-1:2], list[1::2] = list[1::2], list[:-1:2]
print(list)

list = ["name", 1, True, 1.0]
print(type( "name"))
print(type(1))
print(type(True))
print(type(1.0))

  
num = int(input("Введите номер месяца: "))
if num == 1 or num== 2 or num== 12:
    print("Зима")
elif num == 9 or num == 10 or num== 11:
    print("Осень")
elif num == 3 or num == 4 or num== 5:
    print("Весна")
elif num == 6 or num == 7 or num== 8:
    print("Лето")
else:
    print ("Ошибка! Введите число от 1 до 12!")

words=input("Введите слова - ").split()
for word in words:
    print(word)



