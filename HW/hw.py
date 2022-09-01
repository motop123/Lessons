a = list(map(int, input().split()))
s = 0
for i in range(9):
    if i % 2 == 1:
        s += i+2
    print(s)