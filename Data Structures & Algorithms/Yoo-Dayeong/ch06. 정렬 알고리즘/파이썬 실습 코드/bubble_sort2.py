def bubble_sort(a):
  n =len(a)
  for i in range(n-1):
    cnt = 0 # 교환 횟수
    for j in range(n-1, i, -1):
      if a[j-1] > a[j]:
        a[j-1], a[j] = a[j], a[j-1]
        cnt += 1
    if cnt == 0:
      break
    
num = int(input())
x = [0]*num 

for i in range(num):
  x[i] = int(input(f'x[{i}] :'))
  
bubble_sort(x)

print('오름차순으로 정렬')

for i in range(num):
  print(f'x[{i}]={x[i]}')
