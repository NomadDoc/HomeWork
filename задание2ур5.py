new_f = open("text1.txt", "r")
content = new_f.read()
print("Содержимое файла: ", content)
new_f = open("text1.txt", "r")
content = new_f.readlines()
print("Количество строк в файле: ", len(content))
new_f = open("text1.txt", "r")
content = new_f.readlines()
for i in range(len(content)):
    print("Количество символов в файле: ", (i + 1), "-ой строки", len(content[i]))
new_f = open("text1.txt", "r")
content = new_f.read()
content = content.split()
print("Количество слов: ", len(content))
new_f.close()
