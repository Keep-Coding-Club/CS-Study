cnt = 0  # 나눗셈 횟수를 카운트
ptr = 0  # 이미 찾은 소수의 개수
prime = [None]*500 # 소수를 저장하는 배열

prime[ptr]=2 # 2는 소수이므로 초기값으로 지정
ptr += 1

for n in range(3, 1001, 2): # 홀수만 대상으로 설정!
  for i in range(1, ptr): # 이미 찾은 소수로 나눔    
        cnt += 1
        if n % prime[i] == 0:  # 나눠 떨어지면 소수가 아님
            break
  else:  # 끝까지 나눠 떨어지지 않으면 
    prime[ptr] = n
    ptr += 1
    
for i in range(ptr):
  print(prime[i])
  
print(f'나눗셈을 실행한 횟수: {cnt}')
