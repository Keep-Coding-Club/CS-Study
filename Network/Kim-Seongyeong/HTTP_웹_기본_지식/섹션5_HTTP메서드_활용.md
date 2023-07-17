# 섹션5. HTTP 메서드 활용

주차: 3일차, 3주차

## 클라이언트에서 서버로 데이터 전송

### 데이터 전달 방식

1. 쿼리 파라미터를 통한 데이터 전송
    - GET
    - 주로 정렬 필터(검색어)
2. 메세지 바디를 통한 데이터 전송
    - POST, PUT, PATCH
    - 회원 가입, 상품 주문, 리소스 등록, 리소스 변경

### 클라이언트에서 서버로 데이터 전송 상황

1. 정적 데이터 조회
    - 쿼리 파라미터 미사용
2. 동적 데이터 조회
    - 쿼리 파라미터 사용
3. HTML Form을 통한 데이터 전송
    - POST 전송 - 저장
    - GET, POST만 지원 (GET은 저장 시 사용 X)
4. HTTP API를 통한 데이터 전송
    - POST, PUT, PATCH : 메세지 바디를 통해 데이터 전송
    - GET : 조회, 쿼리 파라미터로 데이터 전달

## HTTP API 설계 예시

## HTTP API

### 컬렉션

- POST 기반
- 서버가 관리하는 리소스 디렉토리
- 서버가 리소스의 URI를 생성하고 관리
    
    

### 스토어

- PUT 기반
- 클라이언트가 관리하는 리소스 저장소
- 클라이언트가 리소스의 URI를 알고 관리

### 컨트롤 URI

- HTTP Form은 GET, POST만 지원하므로 제약 있음
- 이런 제약을 해결하기 위해 동사로 된 리소스 경로 사용
    
    ex) POST의 /new, /edit, /delete
    

참고하면 좋은 사이트)

[REST API - URL Naming Conventions](https://restfulapi.net/resource-naming/)