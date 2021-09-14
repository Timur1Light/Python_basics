nabor = [9, 8, 7, 6, 5, 4, 3, 2, 1]
while True:
    try:
        data = int(input("Введите новый элемент рейтинга в виде натурального числа: "))
        i = 0
        for n in nabor:
            if data <= n:
                i += 1
            else:
                break
        nabor.insert(i, data)
        print(nabor)
        out = input('Продолжить? Для выхода нажмите "N", для продолжения нажмите любую кнопку!')
        if out.upper() == "N":
            break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")





