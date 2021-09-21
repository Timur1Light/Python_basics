from itertools import cycle, count

a = int(input("Введите число: "))
my_list = [b for b in range(a)]
counter =count()
cycler = cycle(my_list)

print([next(counter) for b in range(a)])
print([next(cycler) for b in range(a)])
