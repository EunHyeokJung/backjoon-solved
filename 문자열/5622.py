# dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
#
# sum = 0
#
# s = input()
# for c in s:
#     for i, ch in enumerate(dial):
#         if c in ch:
#             sum += 3 + i
# print(sum)

dial = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

sum=0
for c in input():
    sum += dial[ord(c)-65] + 1

print(sum)