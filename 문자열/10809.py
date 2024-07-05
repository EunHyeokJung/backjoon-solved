# l = [-1 for i in range(26)]
# s = input()
# for i, c in enumerate(s):
#     if l[ord(c)-97] == -1:
#         l[ord(c)-97] = i
#
# print(' '.join(map(str, l)))

s = input()
for i in range(97, 123):
    print(s.find(chr(i)), end=' ')
