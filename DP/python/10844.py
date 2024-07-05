N = int(input())

DP = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    DP[1][i] = 1

for digit in range(2, N + 1):
    for number in range(10):
        if number == 0:
            DP[digit][number] = DP[digit - 1][1]
        elif number == 9:
            DP[digit][number] = DP[digit - 1][8]
        else:
            DP[digit][number] = DP[digit-1][number-1] + DP[digit-1][number+1]

print(sum(DP[N]) % 1000000000)
