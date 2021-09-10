def my_fun1(x, y):
    try:
        #res = 1 / x ** abs(y)
        res = x ** y
    except TypeError:
        return "Ошибка! Введите только цифры!"
    return res

def my_fun2(x, y):
    for i in range(abs(y + 1)):
        x *= x
    return 1 / x
while True:
    var_fun = int(input("Введите вариант.\nВведите цифру 1 для запуска функции с использованием оператора ** .\nВведите цифру 2 для запуска функции с использованием цикла: "))
    if var_fun == 1:
        print(my_fun1(2, -2))
    elif var_fun == 2:
        print(my_fun2(2, -2))
    else:
        print("Вводите только 1 или 2 !")
    out = input('Продолжить? Для выхода нажмите "N", для продолжения нажмите любую кнопку!')
    if out.upper() == "N":
        break
