
f = open('my_file.txt', 'w')
print("Введите данные в файл: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()