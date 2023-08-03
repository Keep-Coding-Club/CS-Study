# 질문

## 김선경

## 박은비
1.  http 프로토콜에서 쿠키와 세션을 사용하는 이유를 설명하시오 
2.  Cache-Control 필드의 no-store와 no-chache의 차이점을 설명하시오 
3.  프록시 서버에 대해 설명하시오 

## 유다영


## 이희래


# 모범답안

## 김선경

## 박은비
1. 
http 프로토콜의 Connetionless, Stateless 특성을 보완하기 위해 사용한다 

1. Connetionless 
	request - response 이후 연결을 끊는 처리 방식 
	(자원 절약)
2. Stateless
	상태 정보를 유지하지 않는 특성 

Connetionless, Stateless가 단점이 되는 상황도 존재
	- 로그인
	- 상품 구매 후 상품 정보 업데이트 
	=> 이와 같은 상황들을 해결하기 위해 쿠키와 세션 사용 

쿠키 VS 세션 
쿠키: 클라이언트 (로컬 PC)에 데이터 저장 
세션: 서버에 데이터 저장, 보안성이 높다 

참고자료: [쿠키(Cookie)와 세션(Session)의 차이 (+캐시(Cache)) (tistory.com)](https://dev-coco.tistory.com/61)


2.     
no-chache는 캐시를 저장하되 캐시가 유효한지 매번 서버에 질의 하는 것 
no-store는 아예 캐시를 저장하지 않는 것 


3. 
#### 프록시 서버란?
- 클라이언트와 서버 사이에서 데이터를 전달해주는 서버 
- 클라이언트에서 서버로 접속할 대 직접적으로 접속하지 않고 중간에 대신 전달해주는 서
한국에서 미국 서버의 데이터를 전송 받을 때 
origin 서버에 바로 접속하는 것이 아니라 프록시 서버를 거쳐 데이터를 전달 받는다 

#### 작동 방식 
1. 클라이언트에서 프록시 서버로 전달할 요청을 보낸다.
2. 프록시 서버는 클라이언트로부터 전달 받은 요청을 서버에 요청한다.
3. 서버는 요청에 맞게 데이터를 프록시 서버로 전달한다.
4. 프록시 서버는 서버로부터 전달 받은 데이터를 클라이언트에 전달한다.

#### 필요성 
1. 보안 
2. 캐시 
	- 속도 향상 
3. 우회 

참고자료: [[Network] 프록시 서버란? (feat. 필요한 이유) (What is a Proxy server?) (tistory.com)](https://fomaios.tistory.com/entry/Network-%ED%94%84%EB%A1%9D%EC%8B%9C-%EC%84%9C%EB%B2%84%EB%9E%80-feat-%ED%95%84%EC%9A%94%ED%95%9C-%EC%9D%B4%EC%9C%A0-What-is-a-Proxy-server)

## 유다영

## 이희래
