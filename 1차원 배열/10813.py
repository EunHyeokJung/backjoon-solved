import sys

N, M = map(int, sys.stdin.readline().split())

bucket = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    bucket[i-1], bucket[j-1] = bucket[j-1], bucket[i-1]

print(" ".join(map(str, bucket)))
