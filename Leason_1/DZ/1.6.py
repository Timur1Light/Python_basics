start = float(input("Введите старовый результат : "))
fin = float(input("Введите кончный результат : "))
days = 1
if start <= 0 or fin < 0:
        print("Ошика: Неверно введены данные!")
else:
    while start < fin:
        start += start * 0.1
        days += 1
    print(f"Спортсмент добоется резульат за {days} дней")