import sys

N = int(sys.stdin.readline())

DP = [1 for _ in range(N)]

for i in range(2, N):
    DP[i] = DP[i - 1] + DP[i - 2]

print(DP[N-1])
