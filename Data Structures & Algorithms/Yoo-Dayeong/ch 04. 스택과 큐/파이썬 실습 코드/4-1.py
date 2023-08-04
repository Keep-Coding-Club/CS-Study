# 고정 길이 스택 클래스 FixedStack 구현

class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        '''스택초기화'''
        self.stk = [None]*capacity
        self.capacity = capacity
        self.ptr = 0  # 스택 포인터

    def __len__(self) -> ptr:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0  # 스택이 비어있으면 True

    def is_full(self) -> bool:
        return self.ptr >= self.capacity
