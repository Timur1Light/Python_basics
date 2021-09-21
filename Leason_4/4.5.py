from functools import reduce


my_list = [i for i in range(100, 1001, 2)]
print(f"Список четных чисел от 100 до 1000: {my_list}")
print(f"Результат: {reduce(lambda a, b: a * b, my_list)}")