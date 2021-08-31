def print_data(**args):
    for arg, name in args.items():
        print(f"{arg}: {name}")

print_data(name = input(" Введите свое имя: "),
last_name = input(f"Введите свою фамилию: "),
date_birth = input(f"Введите дату своего рождения: "),
city = input(f"Введите город проживания: "),
email = input(f"Введте email: "),
tel = input(f"Введите номер своего телефона: "))
