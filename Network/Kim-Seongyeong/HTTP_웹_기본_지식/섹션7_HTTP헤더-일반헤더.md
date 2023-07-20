# 섹션7. HTTP 헤더1 - 일반 헤더


## HTTP 헤더 개요

### HTTP 헤더 분류

- General 헤더 : 메세지 전체에 적용되는 정보
- Request 헤더 : 요청 정보
- Response 헤더 : 응답 정보
- Entity 헤더 : 엔티티 바디 정보
    
    엔티티 본문의 데이터를 해석할 수 있는 정보 제공
    

## 표현

- Content-Type : 표현 데이터의 형식
- Content-Encoding : 표현 데이터의 압축 방식
- Content-Language : 표현 데이터의 자연 언어
- Content-Length : 표현 데이터의 길이

## 콘텐츠 협상

### 협상

- 클라이언트가 선호하는 표현 요청
    
    
- Accept : 클라이언트가 선호하는 미디어 타입 전달
- Accept-Charset : 클라이언트가 선호하는 문자 인코딩
- Accept-Encoding : 클라이언트가 선호하는 압축 인코딩
- Accept-Language : 클라이언트가 선호하는 자연 언어

- 협상 헤더는 요청 시에만 사용

### 협상과 우선순위

- Quality Values(q)
1. 0~1, 클수록 높은 우선순위
    
    생략하면 1
    
2. 구체적인 것이 우선한다.
3. 구체적인 것을 기준으로 미디어 타입을 맞춘다.

## 전송 방식

- 단순 전송
- 압축 전송
    
    Content-Encoding 꼭 넣어주어야 함
    
- 분할 전송
    
    Content-Length 넣으면 안됨
    
- 범위 전송

## 일반 정보

- From
    - 유저 에이전트의 이메일 정보
- Referer
    - 이전 웹 페이지 주소
    - A → B로 이동하는 경우 B를 요청할 때 Referer: A를 포함해서 요청
- User-Agent
    - 유저 에이전트 애플리케이션 정보
    - 클라이언트의 애플리케이션 정보(웹 브라우저 정보 등등)
- Server
    - 요청을 처리하는 ORIGIN 서버의 소프트웨어 정보
- Date
    - 메세지가 발생한 날짜와 시간
    - 응답에서 사용

## 특별한 정보

- **Host**
    - 요청한 호스트 정보(도메인)
    - 요청에서 사용
    - 필수적
    - 하나의 서버가 여러 도메인을 처리해야 할 때
    - 하나의 IP 주소에 여러 도메인이 적용되어 있을 때
- Location
    - 페이지 리다이렉션
    - 웹 브라우저는 3xx 응답의 결과에 Location 헤더가 있으면, Location 위치로 자동 이동(리다이렉트)
- Allow
    - 허용 가능한 HTTP 메서드
    - 405 (Method Not Allowed)에서 응답에 포함해야 함
- Retry-After
    - 유저 에이전트가 다음 요청을 하기까지 기다려야 하는 시간

## 인증

- Authorization
    - 클라이언트 인증 정보를 서버에 전달
- www-Authenticate
    - 리소스 접근시 필요한 인증 방법 정의

## 쿠키

> HTTP는 무상태 프로토콜임
이에 대한 대안으로 모든 요청에 정보를 넘길 수 있지만,

보안과 개발시 어려움이 있음

이를 해결하기 위해 Cookie 개발
> 

- Set-Cookie
    - 서버에서 클라이언트로 쿠키 전달(응답)
- Cookie
    - 클라이언트가 서버에서 받은 쿠키를 저장하고, HTTP 요청시 서버로 전달