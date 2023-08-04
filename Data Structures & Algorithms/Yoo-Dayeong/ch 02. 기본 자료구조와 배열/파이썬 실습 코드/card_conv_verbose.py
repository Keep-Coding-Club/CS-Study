# 10진수 정수값을 입력받아 2~36진수로 변환해 출력하기(실습 2-7 수정)

def card_conv(x: int, r: int) -> str:
  '''정수값 x를 r진수로 변환 후에 수를 나타내는 문자열 반환'''
  d = '' # 변환 후 문자열
  dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  n = len(str(x))
  
  print(f'{r:2} | {x: {n}d}')
  
  while x>0:
    print(' +'+(n+2)*'-')
    if x//r:
      print(f'{r:2} | {x//r:{n}d} ··· {x%r}')
    else:
      print(f'  {x//r:{n}d} ··· {x%r}')
    d += dchar[x%r]
    x //= r

  return d[::-1] # 역순으로 반환!