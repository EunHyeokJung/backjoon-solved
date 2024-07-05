import sys

N, M = map(int, sys.stdin.readline().split())

bucket = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    bucket = bucket[:i] + bucket[j:i-1:-1] + bucket[j+1:]

print(" ".join(map(str, bucket[1:])))
