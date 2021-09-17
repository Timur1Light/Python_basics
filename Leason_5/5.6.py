file = open("my_files6.txt")
onstring = file.read().split("\n")[:-1]
dict = {}

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value
print(dict)

print("\n<< Общее количество занятий по предметам >>")
for i in dict:
    list = dict[i]
    summ = 0
    for j in range(0, len(list)):
        summ += int(list[j])
    print(i, ":", summ)