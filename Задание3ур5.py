my_f = open("salary.txt")
sal = []
poor = []
content = my_f.readlines()
for i in content:
    i = i.split()
    if int(i[1]) < 20000:
        poor.append(i[0])
    sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')