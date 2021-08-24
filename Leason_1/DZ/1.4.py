number = int(input("Введите число: "))
max_number = 0
while number >= 10:
    last_number = number % 10
    #print(last_number)
    number = number // 10
   # print(number)
    if max_number < last_number:
        max_number = last_number
print(f" Максимальное число из введенных: {max_number}")

