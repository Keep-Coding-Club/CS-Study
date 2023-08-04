def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c


print('세 정수의 중앙값을 구합니다.')
a = int(input())
b = int(input())
c = int(input())
print(f'중앙값은 {med3(a,b,c)}입니다.')
