
while True:
    try:
        input_a = int(input("Введите первое число: "))
        input_b = int(input("Введите второе число: "))
        rez = input_a / input_b
        print(rez)
    except ValueError:
        print("Ошибка! Не верно введены данные! Введите число!")
    except ZeroDivisionError:
        print("Ошибка! Деление на наоль!")
    out = input('Продолжить? Для выхода нажмите "N", для продолжения нажмите любую кнопку!')
    if out.upper() == "N":
        break
