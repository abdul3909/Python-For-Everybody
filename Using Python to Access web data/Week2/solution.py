import re

lst = []
b = 0
hand = open('mbox-short.txt')

for j in hand:
    exp = re.findall('[0-9]+', j)
    for i in range(len(exp)):
        exp[i] = int(exp[i])
        lst.append(exp[i])
print(sum(lst))
