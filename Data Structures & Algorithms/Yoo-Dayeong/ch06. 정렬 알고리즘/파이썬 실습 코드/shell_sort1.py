def shell_sort(a):
  n = len(a)
  h = n//2
  while h>0:
    for i in range(h, n):
      j = i-h
      tmp = a[i]
      while j>=0 and a[j]>tmp:
        a[j+h] = a[j]
        j -= h
      a[j+h]=tmp
    h//=2

num = int(input())
x = [0]*num

for i in range(num):
  x[i] = int(input(f'x[{i}]:'))

shell_sort(x)

for i in range(num):
  print(f'x[{i}]={x[i]}')