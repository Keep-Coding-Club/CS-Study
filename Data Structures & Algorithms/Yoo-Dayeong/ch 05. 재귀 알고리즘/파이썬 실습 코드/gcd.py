def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x%y)
x=int(input())
y=int(input())
print(f'두 정수의 최대공약수 {gcd(x,y)}')