n = int(input())

for i in range(n):
    if i % 2:  # 홀수인 경우
        print('-', end='')
    else:  # 짝수인 경우
        print('+', end='')
print()
