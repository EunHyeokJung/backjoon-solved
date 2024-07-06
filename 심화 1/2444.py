N = int(input())

n = 2*N-1

for i in range(1, n+1, 2):
    print(" " * ((n - i) // 2), end="")
    print("*" * i)

for i in range(n-1, 0, -2):
    print(" " * ((n - i) // 2 + 1), end="")
    print("*" * (i-1))