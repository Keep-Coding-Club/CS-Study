cnt = 0  # 나눗셈 횟수를 카운트

for n in range(2, 1001):
    for i in range(2, n):
        cnt += 1
        if n % i == 0:  # 나눠 떨어지면 소수가 아님
            break
    else:  # 끝까지 나눠 떨어지지 않으면 다음 수행
        print(n)
print(f'나눗셈을 실행한 횟수: {cnt}')
