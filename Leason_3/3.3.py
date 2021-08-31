def my_func(arg1, arg2, arg3):

    try:
        arg_list = [int(arg1), int(arg2), int(arg3)]
        arg_list.remove(min(arg_list))
        return sum(arg_list)
    except ValueError:
        return "Ошибка! Не верно введены данные! Введите число!"

while True:
    arg1 = input("Введите первое число: ")
    arg2 = input("Введите второе число: ")
    arg3 = input("Введите третье число: ")
    print(my_func(arg1, arg2, arg3))
    out = input('Продолжить? Для выхода нажмите "N", для продолжения нажмите любую кнопку!')
    if out.upper() == "N":
        break