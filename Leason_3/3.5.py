def my_finc():
    i = 0
    while True:
        numbers_list = input("Введите числа для сумvирования. Либо введите X для выхода: ").split()
        for number in numbers_list:
            if number.upper() == "X":
                return f"Выходим! Сумма введенных чисел = {i}"
            else:
                try:
                    i += int(number)
                except ValueError:
                    print("Для выхода из программы нажмите: X .")
        print(f"Сумма введенных чисел = {i}")
print(my_finc())