n = int(input())

for _ in range(n//2):
    print('+-', end='')  # +-를 n//2 개 만큼 출력
if n % 2:
    print('+', end='')  # n이 홀수일때만 + 출력

print()
