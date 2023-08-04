def push(self, value:Any) -> None:
  if self.is_full():
    raise FixedStack.Full # 예외처리
  self.stk[self.ptr] = value
  self.ptr += 1

def pop(self)->Any:
  if self.is_empty():
    raise FixedStack.Empty # 예외처리
  self.ptr -= 1
  return self.stk[self.ptr]

def peek(self)->Any:
  if self.is_empty():
    raise FixedStack.Empty
  return self.stk[self.ptr-1]

def clean(self)->None:
  self.ptr= 0