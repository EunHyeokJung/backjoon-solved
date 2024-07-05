DP = [1, 2, 4] + [0] * 8

for i in range(3, len(DP)):
    DP[i] = (DP[i - 3] + DP[i - 2] + DP[i - 1])

T = int(input())

for i in range(T):
    N = int(input())
    print(DP[N - 1])
