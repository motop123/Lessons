i = 'JavaScript', 'C++', 'C#', 'Ruby', 'PHP', 'КОНЕЦ', 'Python'

for a in range(0, len(i)):
    if 'Конец' and 'конец' in i:
        break
    else:
        a += 1
print(i)
