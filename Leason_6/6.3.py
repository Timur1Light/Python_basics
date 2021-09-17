


class Worker:
    # атрибуты класса
    name = "Иван"
    surname = "Иванов"
    position = "Инженер"
    profit = 20000
    bonus = 2000
    _income = {"Оклад": profit,
               "Премия": bonus
               }    # доход (защищенный атрибут)
    total_profit = 0


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_profit(self):
        self.total_profit = self.profit + self.bonus
        return ", доход с учётом премии: {}".format(self.total_profit)


w = Worker()
print(w.name)
print(w.surname)
print(w.position)
print(w.profit)

p = Position()
print("\n<< Общая информация по сотруднику >>")
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w._income))