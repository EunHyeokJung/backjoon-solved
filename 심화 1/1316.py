N = int(input())

cnt = 0

for i in range(N):
    new_string = input()

    isGroupNumber = True

    last_char = ''
    char_list = [False for _ in range(26)]

    for c in [*new_string]:
        ind = ord(c) - 97

        if last_char == c:
            continue

        if not char_list[ind]:
            char_list[ind] = True
        else:
            isGroupNumber = False
            break

        last_char = c

    if isGroupNumber:
        cnt += 1

print(cnt)