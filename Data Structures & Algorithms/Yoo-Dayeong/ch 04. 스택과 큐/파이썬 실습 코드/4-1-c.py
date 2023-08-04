def find(self, value:Any)->Any:
  for i in range(self.ptr-1, -1, -1): # 꼭대기부터 선형 탐색
    if self.stk[i]==value:
      return i
  return -1

def count(self, value:Any)->Any:
  c= 0
  for i in range(self.ptr): # 바닥부터 선형 탐색
    if self.stk[i]==value:
      c+=1
  return c

def __contains__(self, value:Any)->bool:
  return self.count(value)>0

def dump(self)->None:
  if self.is_empty():
    print('스택이 비어있음')
  else:
    print(self.stk[:self.ptr])
      