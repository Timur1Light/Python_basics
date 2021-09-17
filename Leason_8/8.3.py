class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'q':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as ex:
        print('Вы ввели не число! Вводить разрешается только числа!', ex)
print(f"\nВведенный вами список чисел: {my_list}")