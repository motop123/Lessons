# num = 904069
# count = 0
# for i in range(2, num):
#     if num % i == 0:
#         count += 1
# print('Yep' if count == 0 else 'No')
#--------------------------------------------
s = '10 + 25 - 12 + 20 - 1 + 3'
s = s.replace('- ',' -').replace('+ ', '').replace('  ',' ')
print(s)
arr = list(map(int, s.split()))
print(sum(arr))