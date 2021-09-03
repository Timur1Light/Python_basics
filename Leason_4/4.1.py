from sys import argv

def raschet():
    try:
        hours, stavka, premiya = map(float, argv[1:])
        #hours, stavka, premiya = argv
        print(f"Заработная плата сотрудника = {hours * stavka + premiya} руб.")
    except ValueError:
        print(" Введите данные корректно!")
raschet()