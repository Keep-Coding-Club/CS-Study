
from max import max_of

print('배열의 최댓값을 구하자')
print('End 입력시 종료')

number = 0
x= []

while True:
  s = input(f'x[{number}]값을 입력하세요: ')
  if s == 'End':
    break
  x.append(int(s))
  number += 1
print(f'{number}개 입력')
print(f'최댓값은 {max_of(x)}입니다.')
