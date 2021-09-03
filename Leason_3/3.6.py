def int_finc(word):
    ls = []
    for i in range(len(word)):
        ls.append(word[i][0:1].title() + word[i][1:])
    return ' '.join(ls)
print(int_finc(input('Введите слова разделенные пробелом: ').lower().split()))
