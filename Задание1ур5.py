new_text = open("new_text.txt", "w")
content = [(input("Введите несколько строк. Для выхода нажмите Enter "))]
new_text.writelines(content)
print("Вы ввели: ", content, "Выход")
new_text.close()
