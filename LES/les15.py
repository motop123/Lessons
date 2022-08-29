# from string import punctuation
#
# with open('bulgakov.txt', 'r', encoding= 'utf-8' ) as f:
#     lst = [word.strip(punctuation) for word in ' '.join([line.strip() for line in f.readlines()]).split()]
#     lst2 = [word.lower() for word in lst if len(word) > 3]
#     # print(len(lst2))
#     set_ = set(lst2)
# dct = {}
# n = 0
# for i in lst2:
#     if i not in dct:
#         dct[i] = 1
#     else:
#         dct[i] += 1
#
# keys = sorted(dct, key=dct.get, reverse=True)
# for ind, word in enumerate(keys, 1):
#     if ind <= 20 or word == 'мастер':
#         print(f'{ind}. {word} - {dct[word]}')
# -------------------------------------------------------------
# MATRIX
# lst = []
# for _ in range(4):
#     lst2 = []
#     for _ in range(3):
#         lst2.append([0] * 2)
#     lst.append(lst2)
# print(lst)
# lst = [[0] * 5 for _ in range(4)]
# for line in lst:
#     print(*line)
import random
w, h = 5, 3
#
# matrix = [
#     [0, 1, 2, True],
#     [{}, 11, ['a', 'b', 'c'], 13],
#     [20, 23]
# ]
# for line in matrix:
#     print(*line)

matrix = [[y for x in range(w)] for y in range(h)]
for line in matrix:
    print(*line)
# lst1 = []
# for x in range(h):
#     lst2 = []
#     for y in range(w):
#         lst2.append(0)
#     lst1.append(lst2)
# print(lst1)
