obj = {}
with open("Lesson.txt", "r") as init_f:
    for line in init_f:
        object, lecture, practice, lab = line.split()
        obj[object] = int(lecture)+int(practice)+int(lab)
    print(f'Общее количество часов по предмету {obj}')

