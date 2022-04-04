def welcome():
    print("Приветствую в программе для расчета зарплаты сотрудникам")

def salary():
    hours = int(input("Введите количество отработанных часов: "))
    moneyhours = int(input("Введите количество зарплаты в час: "))
    prize = int(input("Введите размер премии: "))
    allmoney = hours*moneyhours + prize
    return print("Зарплата составила: ", allmoney)

from my_function import welcome
from my_function import salary

welcome()
salary()




