def shaker_sort(a):
  left = 0 # 스캔 범위의 첫 원소 인덱스
  right = len(a)-1 # 스캔 범위의 마지막 원소 인덱스
  last = right
  while left < right:
      for j in range(right, left, -1): # 원소를 맨 뒤에서 맨 앞으로 스캔
        if a[j-1] > a[j]:
          a[j-1], a[j] = a[j], a[j-1]
          last = j
      left= last
      for j in range(left, right): # 원소를 맨 앞에서 맨 뒤로 스캔
        if a[j] > a[j+1]:
          a[j], a[j+1] = a[j+1], a[j]
          last = j
      right = last
      
num = int(input())
x = [0]*num 

for i in range(num):
  x[i] = int(input(f'x[{i}] :'))
  
shaker_sort(x)

print('오름차순으로 정렬')

for i in range(num):
  print(f'x[{i}]={x[i]}')
