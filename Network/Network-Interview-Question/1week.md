# 질문

## 김선경
1. Socket의 정의와 TCP의 Socket 통신 과정을 설명하시오.
2. 3-way-handshake 동작 과정을 설명하시오.

## 박은비

## 유다영

1. 네트워크가 Reliable하다는 것은 무엇일까?(TCP/IP 통신 기준으로)
2. transport-layer에서 한번에 하나의 패킷이 아니라 여러 패킷을 pipelining 하여 처리하는 방식을 설명하고, 장,단점을 설명하시오.

## 이희래

1. TCP와 UDP의 차이점을 설명하시오
2. TCP 흐름 제어와 혼잡 제어를 설명하시오
3. "www.naver.com" 또는 "www.google.com"에 접속할 때 일어나는 일에 대해 설명하세요.

# 모범답안

## 김선경
1. 
Socket 정의 : 네트워크 상에서 돌아가는 두 개의 프로그램 간 양방향 통신의 하나의 엔트 포인트

Socket 통신 과정 : 
   1. server - socket() : (TCP) socket 생성

   2. server - bind() : 생성한 소켓을 server의 특정 port에 bind

   3. server - listen() : 생성한 소켓을 listen 용도로 사용

   4. server - accept() : client로 부터 요청을 받을 준비 완료

   여기까지 수행되면 client로부터 connection이 들어올 때까지 block

   1. client - socket() : socket 생성

   2. client - connect() : 원하는 server의 socket에 connect

   server의 주소와 port 번호가 파라미터로 들어가야 함
   connect 후 client와 server 간 연결고리 형성

   이후로 wirte(), read()으로 통신 진행

2. 1. Client) TCP SYN send
    
    header의 SYN를 1로 하여 server와 TCP 통신을 하고 싶다고 전달
    
    client의 sequnece # 알려줌
    
   2. Server) SYN ACK send
   
   3. Client) ACK (SYN ACK에 관한 ACK)

## 박은비

## 유다영

1. 네트워크가 Reliable하다는 것은 무엇일까?(TCP/IP 통신 기준으로)

   네트워크가 reliable 하다는 것은 TCP/IP 통신에서의 pkt error와 pkt loss가 없는 상황을 말한다.

   pkt error와 pkt loss는 하위 채널들과 같은 unreliable한 상태에서 발생한다.

   각 상황을 해결해줄 수 있는 키워드들은 다음과 같다.

   - pkt error
     - error detection
     - feedback
     - retransmission
     - seq #
   - pkt loss
     - timeout

2. transport-layer에서 한번에 하나의 패킷이 아니라 여러 패킷을 pipelining 하여 처리하는 방식을 설명하고, 장,단점을 설명하시오.

    transport-layer에서 reliable한 패킷 교환을 위해 패킷을 보내고 ACK 응답을 받을때까지 기다리는 Stop and Wait 방식은 ACK가 올때까지 송신자는 계속해서 놀고있으므로 비효율적이다. 따라서 한번에 하나의 패킷이 아니라 여러 패킷을 pipelining 하여 처리하는 방식으로 Go Back N과 Selective repeat 방식이 있다.

    **Go Back N**

    Go-Back-N 방식은 receiver 측에서 순서대로 받지 못한 패킷이 있다면 sender가 **해당 패킷부터 다시 재전송** 하는 방식이다.

    go-back N의 ACK(n)에서 n의 의미는, n번째 pkt까지 잘 받았고, n+1번째를 기다리고 있는 상황이라는 뜻이다. 따라서, 제대로된 ACK가 들어오면 윈도우는 한칸씩 **슬라이딩** 하는 형태로 진행된다.

    만약 패킷이 유실되면 N개(윈도우 사이즈) 만큼 다시 돌아와 재전송한다 그래서 go-back N이라고 불리는 것이다!

    장점은 패킷 유실시 받은 데이터를 버리고, 다시 재전송을 하기 때문에 버퍼가 필요없다.
    단점은 만약 유실된건 하나라도, 그 하나 때문에 다른 애들도 모두 다 재전송해야 한다는 것이다. 윈도우가 작을 때는 무리가 안되지만, 윈도우 사이즈가 커지게 되면 무리가 된다.

    **Selective repeat**

    Selective Repeat 방식은 **receiver 측에서 받은 각각의 패킷들에 대해 ACK을 보내는 방식**이다.

    Selective Repeat은 유실된 것만 재전송 해준다. 이때 폐기 방식을 사용하지 않기 때문에 패킷을 넣어둘 버퍼가 필요하다.

    단점은, 모든 윈도우 안의 패킷에 타이머를 걸어야 한다는 것이기에, 프로세스의 개수가 엄청 많아질 경우 CPU 터질 위험이 있다.

    ![transport-layer-pipielig-protocol](https://github.com/Keep-Coding-Club/CS-Study/assets/71822139/741a52aa-3ada-42b7-b9eb-84231352948b)

## 이희래

1. TCP와 UDP의 차이점을 설명하시오

   **TCP**는 연결형 서비스로 3-way handshaking 과정을 통해 연결을 설정하기 때문에 높은 신뢰성을 보장하지만, 속도가 비교적 느리다는 단점이 있습니다.

   **UDP**는 비연결형 서비스로 3-way handshaking을 사용하지 않기 때문에 신뢰성이 떨어지는 단점이 있지만, 데이터 수신 여부를 확인하지 않기 때문에 속도가 빠르다는 장점이 있습니다.

   TCP는 신뢰성이 중요한 파일 교환과 같은 경우에 쓰이고 UDP는 실시간성이 중요한 스트리밍에 자주 사용됩니다.

   | 프로토콜 종류  | TCP                | UDP                       |
   | -------------- | ------------------ | ------------------------- |
   | 연결 방식      | 연결형 서비스      | 비연결형 서비스           |
   | 패킷 교환 방식 | 가상 회선 방식     | 데이터그램 방식           |
   | 전송 순서      | 전송 순서 보장     | 전송 순서가 바뀔 수 있음  |
   | 수신 여부 확인 | 수신 여부를 확인함 | 수신 여부를 확인하지 않음 |
   | 통신 방식      | 1:1 통신           | 1:1 OR 1:N OR N:N 통신    |
   | 신뢰성         | 높다.              | 낮다.                     |
   | 속도           | 느리다.            | 빠르다.                   |

2. TCP 흐름 제어와 혼잡 제어를 설명하시오

   흐름 제어 방법으로는 Stop and wait과 Sliding window가 있습니다. Stop and wait은 데이터 전송 후 매번 ACK을 통해 잘 도착했음을 확인하고 다음 데이터를 보내는 방식입니다. Sliding window는 버퍼가 사용되어서 window크기만큼 ACK 없이 데이터를 보낼 수 있는 방식입니다.

   혼잡 제어 방법으로는 Stop and Wait ARQ, Go-Back-N ARQ, Selective-Repeat ARQ가 있습니다. Stop and wait ARQ는 수신 측에서 NACK을 전송하거나 주어진 시간 안에 수신 측에서 ACK을 보내지 않으면 송신 측에서 데이터를 재전송하는 방식입니다. Go back N ARQ는 송신 측에서 데이터를 순차적으로 보내면 수신 측에서 지금까지 받은 데이터에 대한 ACK을 한 번만 보내는 방식입니다. 만약 NACK을 받으면 이전에 보낸 데이터들을 모두 다시 보냅니다. Selective repeat ARQ는 Go baCk N ARQ와 비슷하지만 NACK을 받은 데이터만 다시 보낸다는 차이점이 있습니다.

3. "www.naver.com" 또는 "www.google.com"에 접속할 때 일어나는 일에 대해 설명하세요.

   사용자가 '[www.naver.com](http://www.naver.com/)'을 입력하면 DNS를 통해 해당 도메인에 대한 IP 주소를 가지고 옵니다. URL 정보와 받아온 IP 주소를 통해 HTTP 요청 메세지를 생성하고, 요청 메시지는 HTTP 프로토콜을 사용하여 웹 페이지 URL 정보로 변환됩니다. 웹 서버에서는 도착한 웹 페이지 URL정보에 해당하는 데이터를 검색하여 HTTP 응답 메세지를 생성합니다. 이 HTTP 응답 메세지가 HTTP 프로토콜에 의해 사용자에게 네이버 화면으로 보여지게 됩니다.
