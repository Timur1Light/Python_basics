from random import randint
#my_list = [1, 2, 3, 4, 5, 6]
my_list = [randint(0, 500) for _ in range(0, randint(5, 30))]
print(f"Исходные данные : {my_list}")
rez = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(f"Итоговые данные : {rez}")
