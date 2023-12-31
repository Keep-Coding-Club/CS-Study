## HTTP 헤더

- HTTP 전송에 필요한 모든 부가정보
- 표준 헤더 많음
- 필요시 임의로 추가 가능
- RFC2616 → RFC7230으로 변화
    - 엔티티 대신 표현이라고 함
    - 표현 - 요청이나 응답에서 전달할 실제 데이터
    - 표현 헤더는 표현 데이터를 해석할 수 있는 정보 제공
    

## 표현

- Content-Type - 형식
    - 미디어 타입, 문자 인코딩
- Content-Encoding - 압축방식
    - 표현 데이터를 압축하기 위해 사용
    - 데이터 읽는 쪽에서 확인 후 디코딩
- Content-Language - 자연 언어
    - 표현 데이터의 자연 언어 표현
- Content-Length - 길이
    - 바이트 단위
    - Transfer-Encoding 시에는 사용하면 안됨

## 협상 (콘텐츠 네고시에이션)

- Accept - 선호하는 미디어 타입 전달
- Accept-Charset - 선호하는 문자 인코딩
- Accept-Encoding - 선호하는 압축 인코딩
- Accept-Language - 선호하는 자연 언어
- 요청시에만 사용

## 협상과 우선순위

1. Quality Values(q) 값 사용
    - 0~1, 클수록 높은 우선순위
    - 생략하면 1
2. 구체적인 것이 우선
3. 구체적인 것을 기준으로 미디어 타입을 맞춤

## 전송 방식

- 단순 전송 - Content-Length
- 압축 전송 - Content-Encoding
- 분할 전송 - Transfer-Encoding
    - content-Length 사용하면 안됨!
- 범위 전송 - Range, Content-Range

## 일반 정보

- From - 유저 에이전트의 이메일 정보
- Referer - 이전 웹페이지 주소
- User-Agent - 유저 에이전트 애플리케이션 정보, 웹브라우저 정보
    - 요청에서 사용
- Server - 요청을 처리하는 ORIGIN 서버의 소프트웨어 정보
    - 응답에서 사용
- Date - 메시지가 발생한 날짜와 시간
    - 응답에서 사용

## 특별한 정보

- Host - 요청한 호스트 정보(도메인)
    - 필수
    - 요청에서 사용
    - 하나의 서버가 여러 도메인을 처리해야 할 때
- Location - 페이지 리다이렉션
- Allow - 허용 가능한 HTTP 메서드
- Retry-After - 유저 에이전트가 다음 요청을 하기까지 기다려야 하는 시간

## 인증

- Authorization - 클라이언트 인증 정보를 서버에 전달
- WWW-Authenticate - 리소스 접근시 필요한 인증 방법 정의

## 쿠키

- Set-Cookie - 서버에서 클라이언트로 쿠키 전달 (응답)
- Cookie - 클라이언트가 서버에서 받은 쿠키를 저장하고, HTTP 요청시 서버로 전달
- 사용처
    - 사용자 로그인 세션 관리
    - 광고 정보 트래킹
- 쿠키 정보는 항상 서버에 전송됨
    - 네트워크 트래픽 추가 유발
    - 최소한의 정보만 사용
    - 서버에 전송하지 않고, 웹 브라우저 내부에 저장하고 싶으면 웹 스토리지 참고

** 보안에 민감한 데이터는 저장하면 안됨

## 생명주기

- 세션 쿠키 : 만료 날짜를 생략하면 브라우저 종료시 까지만 유지
- 영속 쿠키 : 만료 날짜를 입력하면 해당 날짜까지 유지

## 도메인

- 명시 - 명시한 문서 기준 도메인 + 서브 도메인 포함
- 생략 - 현재 문서 기준 도메인만 적용

## 경로

- 해당 경로를 포함한 하위 경로 페이지만 쿠키 접근
- 일반적으로 루트로 지정

## 보안

- Secure
    - https인 경우만 전송
- HttpOnly
    - 자바스크립트에서 접근 불가
    - HTTP 전송에만 사용
- SameSite
    - 요청한 도메인과 쿠키에 설정된 도메인이 같은 경우만 쿠키 전송
    - 최근 도입된 기술로 사용시 확인 필요
