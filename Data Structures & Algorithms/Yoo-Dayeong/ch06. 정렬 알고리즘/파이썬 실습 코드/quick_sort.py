def qsort(a, left, right):
  pl = left
  pr = right
  x = a[(left+right)//2] # 피벗(가운데 원소)
  
  while pl<=pr:
    while a[pl]<x:
      pl+=1
    while a[pr]>x:
      pr-=1
    if pl <= pr:
      a[pl], a[pr] = a[pr], a[pl]
      pl += 1
      pr -=1
  if left < pr:
    qsort(a, left, pr)
  if pl<right:
    qsort(a, pl, right)


def quick_sort(a):
  qsort(a, 0, len(a)-1)
  
num = int(input())
x = [0]*num

for i in range(num):
  x[i]=int(input(f'x[{i}]: '))

quick_sort(x)

for i in range(num):
  print(f'x[{i}] = {x[i]}')
  