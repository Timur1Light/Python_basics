from random import randint
with open('my_file5.txt', 'w') as my_file5:
    list = [randint(1, 1000) for _ in range(100)]
    my_file5.write(" ".join(map(str, list)))
print(f"Сумма элементов - {sum(list)}")
