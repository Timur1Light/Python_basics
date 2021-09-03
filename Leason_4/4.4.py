from random import randint


numbers = [randint(0, 9) for _ in range(20)]
print(f"Исходные данные: {numbers}")
print(f"Итоговые данные: {[i for i in numbers if numbers.count(i) == 1]}")