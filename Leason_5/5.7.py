"""
import json

with open("/my_json_files7.json", "w") as leason7:
    with open("my_files7.txt") as my_obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_obj}
        rezult = [profit, {"averange_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]
json.dump(rezult, leason7, ensure_ascii=False, indent=4)

"""

with open("my_files7.txt", "w") as leason7:
    # = open("my_files7.txt")
    #onstring = file.read().split("\n")[:-1]
    print(leason7)
    dict_firm_profit = {}
    dict_firm_profit_rent = {}

    for item in leason7:
        key = item.split(" ")[0]
        value = item.split(" ")[2:]
        revenue = item.split(" ")[2:-1]  # выручка
        revenue = int(revenue[0])
        profit = int(value[0]) - int(value[1])  # прибыль
        rent = profit / revenue * 100  # рентабельность
        rent = int(rent)
        dict_firm_profit[key] = profit
        dict_firm_profit_rent[key] = profit, rent
        # print("%.1f" % rent, "%")
    print(dict_firm_profit)


# создание словаря {'Средняя прибыль': средняя прибыль}
dict_middle_profit = {}
middle_profit = sum(dict_firm_profit.values())/len(dict_firm_profit)
dict_middle_profit['Средняя прибыль всех компаний'] = middle_profit
print(dict_middle_profit)


list = [dict_firm_profit_rent, dict_middle_profit]
print("\n\n", list)