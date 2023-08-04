n = int(input())
w = int(input())

for i in range(n):  # n번 반복
    print('*', end='')
    if i % w == w-1:  # n번 판단
        print()
if n % w:  # 1번 판단
    print()  # 줄바꿈
