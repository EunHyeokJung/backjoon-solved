# import sys
#
# chess = list([1, 1, 2, 2, 2, 8])
# mylist = [0, 0, 0, 0, 0, 0]
# for i, n in enumerate(list(map(int, sys.stdin.readline().split()))):
#     mylist[i] = chess[i] - n
#
# print(" ".join(map(str, mylist)))

import sys
k, q, r, b, n, p = map(int, sys.stdin.readline().split())
print(1-k, 1-q, 2-r, 2-b, 2-n, 8-p)
