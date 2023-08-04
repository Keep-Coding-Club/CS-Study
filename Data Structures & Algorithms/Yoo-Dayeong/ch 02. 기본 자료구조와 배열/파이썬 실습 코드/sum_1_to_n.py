
def sum_1_to_n(n):
    # 1부터 n까지 정수의 합
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s


x = int(input('x의 값을 입력: '))
print(f'1부터 {x}까지 정수의 합 {sum_1_to_n(x)}')
