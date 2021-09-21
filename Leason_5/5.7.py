import json

with open("my_json_files7.json", "w") as leason7:
    try:
        with open("my_files7.txt") as my_obj:
            profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_obj}
            rezult = [profit, {"averange_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len(
                [int(i) for i in profit.values() if int(i) > 0]))}]
        json.dump(rezult, leason7, ensure_ascii=False, indent=4)
    except ZeroDivisionError:
        print("Ошибка! Файл пуст!")

