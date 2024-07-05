N = int(input())

DP = [[1 for _ in range(10)] for _ in range(N)]

for n in range(1, N):
    for x in range(1, 10):
        DP[n][x] = DP[n - 1][x] + DP[n][x - 1]

re = 0
for i in range(10):
    re += DP[N - 1][i]

print(re % 10007)
