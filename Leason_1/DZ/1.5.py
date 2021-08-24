viruchka = float(input("Введите значение выручки : "))
izderjki = float(input("Введите значение издержек фирмы : "))
fin_rez = viruchka - izderjki
if fin_rez > 0:
    print(f"Фирма работает с прибылью : {fin_rez:.2f}")
    print(f"Рентабильность составляет : {100 * fin_rez / viruchka:.2f}")
    sontrudniki = int(input("Введите численность сотрудников : "))
    print(f"Прибыль фирмы в расчете на одного сотрудника : {fin_rez / sontrudniki:.2f}")
elif fin_rez < 0:
    print(f"Фирма работает в убыток : {fin_rez:.2f}")
else:
    print("Фирма работает в ноль!")

