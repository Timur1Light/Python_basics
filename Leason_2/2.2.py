data = list(input("Введите число через пробел: "))
for i in range(1, len(data), 2):
    data[i -1], data[i] = data[i], data[i - 1]
print(data)
