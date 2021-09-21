data = ['Строка 1', 1, 'Строка 2', 2.2, 'Строка 3', True, 'Строка 4', None, 'Строка 5']
for i, v in enumerate(data, 1):
    print(f"Позиция: {i}  Тип - {type(v)}")