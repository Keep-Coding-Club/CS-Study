# 양의 정수 n의 팩토리얼

def fac(n):
    if n > 0:
        return n * fac(n-1)
    else:
        return 1


n = int(input('팩토리얼 값: '))
print(f'{n}의 팩토리얼: {fac(n)}')
