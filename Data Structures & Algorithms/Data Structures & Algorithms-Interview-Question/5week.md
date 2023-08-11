# 질문

## 김선경

## 박은비
1. 원소의 값이 정렬되지 않은 배열에서 데이터를 검색하는 유일한 방법은? 
2.  링 버퍼를 활용할 수 있는 곳은?
3.  이진 탐색 손코딩하기 
4. 스택의 push(), pop() 함수를 작성하고 설명하기 (수도 코드도 좋음)

## 유다영

1. 해시법의 충돌을 해결하는 2가지 방법은? 무엇인지, 각 방법을 설명해주세요.

## 이희래
1. Big-O 표기법의 시간 복잡도 크기 순서를 말해주세요.
        
2. 재귀 알고리즘에 대해 설명해주세요.
        
3. 팩토리얼의 N번째 값을 구하는 메소드에 대해 각각 재귀와 반복문으로 손코딩(또는 수도코딩) 해주세요.

# 모범답안

## 김선경

## 박은비
1. 선형 검색 (p.114)
2. 오래된 데이터를 버리는 용도로 사용할 수 있다 
	가장 최근에 들어온 n 개의 데이터만 저장하고 오래된 데이터는 오래된 순서대로 버릴 수 있다  
3. 
```python
def binary_search(array, target, start, end):
	if start > end:
		return None

	mid = (start + end) // 2

	if array[mid] == target:
		return mid
	elif array[mid] > target:
		return binary_search(array, target, start, mid -1)
	else:
		return binary_search(array, target, mid + 1, end)

a = [1, 2, 3, 4]
target = 2
print(binary_search(a, target, 0, len(a) -1))
```
4.  
```python
def push(self, value: Any) -> None:
	if is_full():
		# 예외 처리 
	self.stk[self.ptr] = value
	self.ptr += 1

def pop(self) -> Any:
	if is_empty():
		# 예외처리 
	ptr -= 1
	return self.stk[self.ptr]
```


## 유다영

1. 해시법은 추가, 삭제가 일어나는 데이터 집합에서 아주 빠른 검색이 가능하며 키와 해시값은 일반적으로 다대1 이므로, 저장할 버킷이 중복되는 현상을 충돌이라고 함. 이때 해시 충돌을 해결하는 방법이 2가지가 있음.

- 체인법
  해시값이 같은 원소를 연결리스트로 관리
- 오픈주소법
  빈 버킷을 찾을 때까지 해시 반복

## 이희래

1. Big-O 표기법의 시간 복잡도 크기 순서를 말해주세요.
    - 정답
        
        *O(1) < O(log N) < O(N) < O(N log N) < O(N^2) < O(2^N) < O(N!)*
        
        ![빅오표기법 그래프 이미지](https://images.velog.io/images/welloff_jj/post/5d29a3fb-c5e1-4f81-919b-7ddfd774add5/%E1%84%87%E1%85%B5%E1%86%A8%E1%84%8B%E1%85%A9.jpeg)
        
2. 재귀 알고리즘에 대해 설명해주세요.
    - 정답
        
        재귀 알고리즘이란 함수 내부에서 함수가 자기 자신을 또 다시 호출하여 문제를 해결하는 알고리즘입니다.
        
        자기 자신을 계속해서 호출하여 끝없이 반복되게 되므로 반복을 중단할 조건이 반드시 필요합니다.
        
3. 팩토리얼의 N번째 값을 구하는 메소드에 대해 각각 재귀와 반복문으로 손코딩(또는 수도코딩) 해주세요.
    - 정답
        
        ```cpp
        private static int recursiveFactorial(int num) {
            if(num > 1) {
                return recursiveFactorial(num -1) * num;
            }
            return 1;
        }
         
        private static int loopFactorial(int num) {
            int answer = 1;
            for(int i = 2; i <= num; i++) {
                answer *= i;
            }
            return answer;
        }
        ```
