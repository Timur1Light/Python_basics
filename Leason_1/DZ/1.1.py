age = input("Введите свой возраст: ")
name = input("Введите ваше имя")
sename = input("Введите вашу фамилию")
otchestvo = input("Введите ваше отчиство")

age_last = int(age) % 10
if age_last<= 4:
    age_let = "года"
else:
    age_let = "лет"
print(f"Тебя зовут {name} {sename} {otchestvo} и тебе {age} {age_let}")
