n = int(input())
w = int(input())

for _ in range(n//w): # n//w 번 반복
  print('*' * w)
rest = n%w
if rest: # if문 판단 1번
  print('*'*rest)
