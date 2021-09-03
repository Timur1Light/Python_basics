def my_factorial(a):
    b = 1
    #for i in range(1, a + 1):
    for i in range( a + 1):
        yield f"{i}! = {b}"
        b *= i + 1

for j in my_factorial(int(input("Введите значение: "))):
    print(j)
#print(my_factorial(input("Введите значение: ")))