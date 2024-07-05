X = int(input())

DP = [0] * 1000001

for i in range(2, len(DP)):

    DP[i] = DP[i - 1] + 1

    if i % 2 == 0:
        DP[i] = min(DP[int(i / 2)] + 1, DP[i])
    if i % 3 == 0:
        DP[i] = min(DP[int(i / 3)] + 1, DP[i])

print(DP[X])
