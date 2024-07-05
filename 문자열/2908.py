import sys
print(max(map(lambda s:int(str(s)[::-1]), sys.stdin.readline().split())))
