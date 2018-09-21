alpha = []

with open ('test.txt', 'rt') as in_file:
    for line in in_file:
        if line[5] == "A":
            alpha.append(line)
        print(len(alpha))
