f = open('my_file.txt')
line_count = 0
for line in f:
    line_count += 1
    flag = 0
    word = 0
    for j in line:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(line, word, 'сл.')

print("Количество строк в файле: ", line_count)
f.close()