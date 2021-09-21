with open('my_files6.txt', 'r') as my_file6:
    print({line.split(':')[0]: sum(int(s[:s.index('(')]) for s in line.split() if '(' in s) for line in my_file6})
