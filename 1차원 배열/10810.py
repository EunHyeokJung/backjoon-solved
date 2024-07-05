import sys

N, M = map(int, sys.stdin.readline().split())

bucket = [0 for _ in range(N+1)]

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for ind in range(i, j+1):
        bucket[ind] = k

print(" ".join(map(str, bucket[1:])))
