# gen_1 = (i for i in range(1000000))
# gen_2 = [i for i in range(1000000)]
# for i in gen_1:
#     print(i)
# import sys
# print(sys.getsizeof(gen_2))
# print(sys.getsizeof(gen_1))
# lst = []
# for i in range(50):
#     if i % 2 == 0:
#         lst.append(i**2)
# print(lst)
# lst_2 = [j**2 for j in range(50) if j % 2 == 0]
# print(lst_2)
# l = [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304]
# print([k for k in l if k % 3 == 0])
# list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
# list_b = [x**2 if x%2 == 0 else x**3 for x in list_a]
# print(list_b)
#
# list_c = []
# for i in list_a:
#     if i % 2 == 0:
#         list_c.append(i**2)
#     else:
#         list_c.append(i**3)
# print(list_c)
# list_let = ['a', 'b', 'c']
# list_ = [i for i in enumerate(list_let)]
# print(list_)
l1 = [1, 2, 3, 4]
l2 = ['f', 'c', 'd', 'f']
l3 = [True, False, False, False]
z = zip(l1, l2, l3)
print(z)
for i in z:
    print(i)
