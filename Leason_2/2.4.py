data = input("Введите несколько слов разделенные пробелом: ").split()
for v, i in enumerate(data, 1):
    print(v, i[:10])