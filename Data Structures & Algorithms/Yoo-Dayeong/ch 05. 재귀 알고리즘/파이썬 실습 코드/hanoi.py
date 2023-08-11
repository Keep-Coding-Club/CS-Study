# 원반 no개를 x기둥에서 y기둥으로 옮김

def move(no, x, y):
    if no > 1:
        move(no-1, x, 6-x-y)
    print(f'원반 [{no}]개를 {x}기둥에서 {y}기둥으로 옮김')

    if no > 1:
        move(no-1, 6-x-y, y)


n = int(input())
move(n, 1, 3)
