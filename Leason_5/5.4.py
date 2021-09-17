with open('my_file4.txt', 'r+') as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.split(' '))
print(lst)

rus = ["Один", "Два", "Три", "Четыре"]

j = 0
for i in range(0, len(lst), 3):
    lst[i] = rus[j]
    j += 1

print(lst)
out_f = open('my_file42.txt', 'w')
out_f.writelines(lst)
out_f.close()