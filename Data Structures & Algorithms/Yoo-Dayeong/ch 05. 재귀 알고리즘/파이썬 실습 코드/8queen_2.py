pos = [0]*8
flag = [False]*8  # 각 행에 퀸을 배치했는지 체크

def put():
  for i in range(8):
    print(f'{pos[i]:2}', end='')
  print() 
  
def set(i):
  for j in range(8):
    if not flag[j]: # j행에 퀸 배치 x
      pos[i]=j
      if i == 7:
        put()
      else:
        flag[j]=True
        set(i+1)
        flag[j]=False
      
set(0)  