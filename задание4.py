
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = []
for i in range(len(my_list)-1):
    if my_list[i]!= my_list[i+1]:
        new_list.append(my_list[i])

print(new_list)