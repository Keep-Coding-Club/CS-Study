class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.no=0   # 노드 개수
    self.head = None    # 머리 노드
    self.current = None   # 주목 노드
    
  def __len__(self):
    return self.no # 연결리스트의 노드 개수 반환
  
  # data와 값이 같은 노드 검색
  def search(self, data):
    cnt =0
    ptr = self.head
    
    while ptr is not None:
      if ptr.data == data:
        self.current = ptr
        return cnt
      cnt +=1
      ptr = ptr.next
  
    return -1
  
  # 연결리스트에 data가 포함되어 있는지 확인
  def __contains__(self, data):
    return self.search(data) >= 0
  
  # 맨 앞에 노드 삽입
  def add_first(self, data):
    ptr = self.head   # 삽입 전 머리 노드
    self.head =self.current = Node(data, ptr)
    self.no += 1
    
  # 맨 끝에 노드 삽입
  def add_last(self, data):
    if self.head is None:
      self.add_first(data)
    else:
      ptr = self.head
      while ptr.next is not None:
        ptr = ptr.next
      ptr.next = self.current = Node(data, None)
      self.no += 1
  
  # 머리 노드 삭제
  def remove_first(self):
    if self.head is not None:
      self.head = self.current = self.head.next
    self.no -= 1
  
  # 꼬리 노드 삭제
  def remove_last(self):
    if self.head is not None:
      if self.head.next is None: # 노드가 1개뿐이라면
        self.remove_first()
      else:
        ptr = self.head # 스캔 중인 노드
        pre = self.head # 스캔 중인 노드의 앞쪽 노드
        
        while ptr.next is not None:
          pre=ptr
          ptr = ptr.next
        pre.next = None
        self.current = pre
        
        self.no -= 1
  # 노드 삭제
  def remove(self, p):
    if self.head is not None:
      if p is self.head:
        self.remove_first() # 머리 노드 삭제
      else:
        ptr = self.head
        
        while ptr.next is not p:
          ptr = ptr.next
          if ptr is None:
            return # ptr은 리스트에 존재 x
        ptr.next = p.next
        self.current = ptr
        self.no -= 1
  # 주목 노드 삭제
  def remove_current_node(self):
    self.remove(self.current)
  # 전체 노드 삭제
  def clear(self):
    while self.head is not None:
      self.remove_first()
    self.current = None
    self.no = 0
  # 주목 노드를 한 칸 뒤로 이동
  def next(self):
    if self.current is None or self.current.next is None:
      return False
    self.current = self.current.next
    return True