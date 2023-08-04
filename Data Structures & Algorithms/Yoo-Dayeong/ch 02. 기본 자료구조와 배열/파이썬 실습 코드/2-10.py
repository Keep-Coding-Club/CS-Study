cnt = 0  # 나눗셈 횟수를 카운트
ptr = 0  # 이미 찾은 소수의 개수
prime = [None]*500 # 소수를 저장하는 배열

prime[ptr]=2 # 2는 소수
ptr += 1

prime[ptr]=3 # 3은 소수
ptr += 1


for n in range(5, 1001, 2): # 홀수만 대상으로 설정!
  i = 1
  while prime[i] * prime[i] <= n:
    cnt += 2 # 곱셈, 나눗셈의 실행 횟수를 세기때문에
    if n % prime[i] == 0:  # 나눠 떨어지면 소수가 아님
        break
    i += 1
  else:  # 끝까지 나눠 떨어지지 않으면 
    prime[ptr] = n
    ptr += 1
    cnt += 1 # 곱셈 횟수는 카운트 X 나눗셈 횟수만 카운트.
    
for i in range(ptr):
  print(prime[i])
  
print(f'나눗셈을 실행한 횟수: {cnt}')
