N = int(input())

DP = [1, 2] + [0] * 999

for i in range(2, len(DP)):
    DP[i] = DP[i - 1] + DP[i - 2]

print(DP[N-1] % 10007)
