time = int(input("Введите время в секундах: "))
hours = time // 3600
minuts = (time - hours * 3600) // 60
sec = time - hours * 3600 - minuts * 60

print(f"Введенное время: {hours:02}:{minuts:02}:{sec:02}")
