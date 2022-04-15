try:
    with open("num.txt") as read_file:
        with open("num.txt", "w") as write_file:
            number_words_list = ["Один", "Два", "Три", "Четыре"]
            all_read_lines = read_file.readlines()
            for num, line in enumerate(all_read_lines):
                if len(line):
                    words = line.split()
                    print(f"{number_words_list[num]} {words[1]} {words[2]}", file=write_file)
    print("\tГотово\n")
except IOError:
    print("\tОшибка открытия файла!\n")
